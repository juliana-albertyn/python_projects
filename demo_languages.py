"""
Module: demo_languages
Purpose: Demostrate switching between languages
"""

__author__ = "Juliana Albertyn"
__email__ = "julie_albertyn@yahoo.com"
__status__ = "development"  # or testing or production
__date__ = "2026-01-03"

import gettext
import language_constants as lc


def run_demo(lang_code):
    # Load translations for the given language code
    lang = gettext.translation(
        "messages", localedir="locales", languages=[lang_code], fallback=True
    )
    lang.install()
    _ = lang.gettext

    print(f"\n--- Demo in {lang_code} ---")
    print(_(lc.QUEUE_IS_EMPTY))
    print(_(lc.QUEUE_IS_FULL))
    print(_(lc.QUEUE_ENQUEUE))
    print(_(lc.QUEUE_DEQUEUE))
    print(_(lc.ERROR_OVERFLOW))
    print(_(lc.ERROR_UNDERFLOW))


if __name__ == "__main__":
    # English (South Africa)
    run_demo("en_ZA")

    # Afrikaans
    run_demo("af_ZA")

    # Zulu
    run_demo("zu_ZU")

    # French
    run_demo("fr_FR")

    # Spanish
    run_demo("es_ES")

    # Portuguese
    run_demo("pt_PT")
