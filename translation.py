"""
Module: translation
Purpose: Handles translations

"""

__author__ = "Juliana Albertyn"
__email__ = "julie_albertyn@yahoo.com"
__status__ = "development"  # or testing or production
__date__ = "2026-01-06"


import gettext
from pathlib import Path

available_languages = ["en_ZA", "af_ZA", "zu_ZU", "pt_PT", "es_ES", "fr_FR"]


class LocaleError(Exception):
    """Custom exception for languages where translations haven't yet been supplied"""

    def __init__(self, language_code: str) -> None:
        """Creates an instance of LocaleError"""
        self._language_code = language_code

    def __str__(self):
        return f"Unsupported locale: {self._language_code}"


class Translator:
    """Handle setting of languages globally."""

    def __init__(self, default_lang="en_ZA"):
        """Create an instance of the Translator class"""
        self._language_code = default_lang
        self._translator = gettext.NullTranslations()
        self._ = self._translator.gettext

    def set_locale(self, language_code: str) -> None:
        """Handles all translations for a language code"""
        if language_code not in available_languages:
            raise LocaleError(language_code)

        mo_path = Path(f"locales/{language_code}/LC_MESSAGES/messages.mo")
        if not mo_path.exists():
            raise FileNotFoundError(f"Missing translations: {mo_path}")

        self._translator = gettext.translation(
            "messages",
            localedir="locales",
            languages=[language_code],
            fallback=False,
        )
        self._ = self._translator.gettext
        self._language_code = language_code


# Create a shared instance
translator = Translator()
