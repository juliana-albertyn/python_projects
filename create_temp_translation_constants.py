"""
Module: create_temp_translation_constants
Purpose: Create a temporary copy, to be used by xgettext,
of all str constants in a file.
For now only for use on files in this project.
Can later be generatlised
"""

__author__ = "Juliana Albertyn"
__email__ = "julie_albertyn@yahoo.com"
__status__ = "development"  # or testing or production
__date__ = "2026-01-04"

import pathlib


def create_temp_file(filename: str) -> None:
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
    if pathlib.Path(filename).suffix != ".py":
        raise ValueError("Must be a python file")
    lines = []
    try:
        in_docstr = False
        f = open(filename)
        lines = f.readlines()
        ignores = ["#", "_", "import"]
        for i in range(0, len(lines)):
            # initialise, stripping leading and trailing spaces
            line = lines[i].strip().replace("\n", "")
            # empty string
            if line.isspace():
                continue
            # ignore docstrings
            if line.startswith('"""') and line.endswith('"""') and len(line) > 6:
                continue
            if line.endswith('"""') and in_docstr:
                in_docstr = False
                continue
            if line.startswith('"""'):
                in_docstr = True
            if in_docstr:
                continue
            # single line ignores
            ignore = False
            for s in ignores:
                if line.startswith(s):
                    ignore = True
                    break
            if ignore:
                continue    
            if line.find("=") == -1:
                continue

            # re-initialise with spaces
            line = lines[i]

            # very specific to how I code
            line = line.replace(' "', ' _("', 1)
            line = line.replace('"\n', '")\n')

            lines[i] = line
    except FileNotFoundError or PermissionError or OSError as e:
        print(f"ERROR {filename}: {e}")
    except ValueError as e:
        print(f"ERROR {filename}: {e}")

    # now write the updated lines to the temp file
    filename = pathlib.Path(filename).stem + "_temp" + pathlib.Path(filename).suffix
    try:
        f = open(filename, "w")
        f.writelines(lines)
        f.close()
    except FileNotFoundError or PermissionError or OSError as e:
        print(f"ERROR {filename}: {e}")


if __name__ == "__main__":
    create_temp_file("d:/python_projects/language_constants.py")
