"""
Module: create_temp_translation_constants
Purpose: Create a temporary copy, to be used by xgettext,
of all str constants in a file.
"""

__author__ = "Juliana Albertyn"
__email__ = "julie_albertyn@yahoo.com"
__status__ = "development"  # or testing or production
__date__ = "2026-01-04"

from pathlib import Path
import re


# def replace_quotes(text: str) -> str:
#     """
#     Replace the quotes in text to allow translation of str constants
#     Assumption - only 1 double quote or single quote pair per line
#     """
#     count = 0

#     def repl(match):
#         nonlocal count
#         count += 1
#         return '_("' if count == 1 else '")'

#     return re.sub(r'"', repl, text, count=2)  # only replace first 2 quotes

import re


def replace_quotes(text: str) -> str:
    """
    Replace the first pair of matching quotes (single or double) in a line
    with gettext-style markers: _("...") or _('...').
    Assumption: only one pair of quotes per line, and they must match.
    """
    count = 0
    quote_char = None

    def repl(match):
        nonlocal count, quote_char
        char = match.group(0)

        # First match: record which quote type we saw
        if count == 0:
            quote_char = char
            count += 1
            return f"_({quote_char}"
        else:
            # Second match: must be same type
            if char != quote_char:
                raise ValueError("Mixed quote types on line are not supported")
            return f"{quote_char})"

    # Match either single or double quote
    return re.sub(r'["\']', repl, text, count=2)


def create_temp_file(filename: str, file_encoding: str = "utf-8") -> None:
    """Create a temporary copy of filename, naming it filename_temp.py.
    All str constants will be changed to enable them to be used by xgettext:
        THIS_MESSAGE = "This is a message" -> THIS_MESSAGE = _("This is a message")

    Args:
    filename (str): name of file containing the str constants to be updated

    Raises:
    ValueError: if filename does not end with .py
    Traps FileNotFoundError, PermissionError, and OSError when opening files.
    Raises ValueError with a descriptive message if the file cannot be opened.
    """

    lines = []
    path = Path(filename).resolve(strict=True)
    try:
        if path.suffix != ".py":
            raise ValueError("Must be a python file")
        with open(path, "r", encoding=file_encoding) as f:
            lines = f.readlines()
    except (FileNotFoundError, PermissionError, OSError) as e:
        print(f"ERROR {path}: {e}")
    except ValueError as e:
        print(f"ERROR {path}: {e}")
    ignores = ["#", "_", "import"]
    in_docstr = False
    for i in range(0, len(lines)):
        # initialise, stripping leading and trailing spaces
        analysis_line = lines[i].strip().replace("\n", "")
        # empty string
        if not analysis_line:
            continue
        # ignore docstrings
        if (
            analysis_line.startswith('"""')
            and analysis_line.endswith('"""')
            and len(analysis_line) > 6
        ):
            continue
        if analysis_line.endswith('"""') and in_docstr:
            in_docstr = False
            continue
        if analysis_line.startswith('"""'):
            in_docstr = True
        if in_docstr:
            continue
        # single analysis_line ignores
        ignore = False
        for s in ignores:
            if analysis_line.startswith(s):
                ignore = True
                break
        if ignore:
            continue
        if analysis_line.find("=") == -1:
            continue

        # replace the original line with the updated line
        try:
            updated_line = replace_quotes(lines[i])
            lines[i] = updated_line
        except ValueError as e:
            print(f"ERROR {path}: {e}")

    # now write the updated lines to the temp file
    path = Path(filename).resolve(strict=True)
    temp_path = path.with_name(path.stem + "_temp" + path.suffix)
    try:
        with open(temp_path, "w", encoding=file_encoding) as f:
            f.writelines(lines)
    except (FileNotFoundError, PermissionError, OSError) as e:
        print(f"ERROR {path}: {e}")


if __name__ == "__main__":
    # create_temp_file("d:/python_projects/language_constants.py")
    create_temp_file("language_constants.py")
