# Volby #

Třetí projekt do Engeto Online Python Akademie.

Aplikace slouží ke stažení výsledků voleb z webu volby.cz a uložením dat do formátu CSV. Konkrétní URL (územní celek) je předána jako první argument aplikace, která rozparsuje načtenou webovou stránku a získá URL adresy obcí v daném celku. Následně stejným způsobem načte a rozparsuje jednotlivé obce, z kterých získá výsledky voleb a uloží je do souboru zadaném jako druhý argument.

## Instalace ##

Doporučený postup je vytvoření si virtuálního Python prostředí a přepnutím se do něj.

`python -m venv projekt_volby`

Přepnutí se do virtuálního prostředí v Linux/OSX:

`source projekt_volby/bin/activate`

Přepnutí se do virtuálního prostředí ve Windows:

`source projekt_volby\Scripts\Activate.ps1`

Když jste přepnuti ve virtuálním prostředí (a nebo jste zvolili nevytvářet virtuální prostředí) můžete nainstalovat potřebné knihovny pomocí příkazu:

`pip install -r requirements.txt`

## Použití ##

`python volby.py url output`

Argument `url` je celá URL územního celku (například Kladno: [https://volby.cz/pls/ps2017nss/ps32?xjazyk=CZ&xkraj=2&xnumnuts=2103](https://volby.cz/pls/ps2017nss/ps32?xjazyk=CZ&xkraj=2&xnumnuts=2103))

Argument `output` je název souboru, do kterého se výsledná data uloží. Například: `volby_kladno.csv`.

Příklad použití aplikace:

`python volby.py "https://volby.cz/pls/ps2017nss/ps32?xjazyk=CZ&xkraj=2&xnumnuts=2103" volby_kladno.csv`
