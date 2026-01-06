# PowerShell script to extract strings, merge updates, and compile translations

# 1. Run a python script to create language_constants_temp.py from language_constants.py 
python "d:\python_projects\create_temp_translation_constants.py"

# 2. Extract translatable strings from Python source into a template (.pot)
xgettext --language=Python --keyword=_ `
    --output=locales/messages.pot `
    language_constants_temp.py

# 3. Define the languages you want to support
$languages = @("af_ZA", "en_ZA", "zu_ZU", "fr_FR", "pt_PT", "es_ES")

foreach ($lang in $languages) {
    $poDir = "locales\$lang\LC_MESSAGES"
    $poFile = "$poDir\messages.po"
    $moFile = "$poDir\messages.mo"

    # Ensure directory exists
    if (!(Test-Path $poDir)) {
        New-Item -ItemType Directory -Force -Path $poDir | Out-Null
    }

    # 4. If .po file exists, merge updates from .pot
    if (Test-Path $poFile) {
        Write-Host "Merging updates into $poFile..."
        msgmerge --update $poFile locales/messages.pot
    }
    else {
        Write-Host "Creating new $poFile from template..."
        Copy-Item locales/messages.pot $poFile
    }

    # 5. Compile .po into .mo
    Write-Host "Compiling $poFile -> $moFile"
    msgfmt $poFile -o $moFile
}

Write-Host "✅ All translations updated and compiled."