"""
volby.py: Třetí projekt do Engeto Online Python Akademie

Autor: Ondřej Malek
Email: ondrej.malek@dpb.cz
Discord: Arakorn67//76
"""
import csv
import requests

from argparse import ArgumentParser
from bs4 import BeautifulSoup
from urllib.parse import urljoin

# Aplikace používá jen pár externích knihoven a to konkrétně
# BeatifulSoup a requests. Potřebné závislosti byly vygenerovány pomocí příkazu
# `pip freeze > requiremenets.txt` a jsou uloženy v souboru `requirements.txt`.
# Pro jejich instalaci stačí použít `pip install -r requirements.txt` ve svém
# vlastním virtuálním prostředí.

# Pomocná třída, shromažďující informace o konkrétní obci
class Municipal:

    # Konstruktor třídy k inicializaci dat
    def __init__(
            self, code, name, url, voters_count, issued_envelopes, valid_votes,
            parties
    ):
        self.code = code
        self.name = name
        self.url = url
        self.voters_count = voters_count
        self.issued_envelopes = issued_envelopes
        self.valid_votes = valid_votes
        self.parties = parties

    # Metoda vrací list dat v pořadí, jak se objeví i v uloženém CSV
    def to_csv_line(self):
        return [
            self.code, self.name, self.voters_count, self.issued_envelopes,
            self.valid_votes
        ] + [votes for (name, votes) in self.parties]

# Sebere z URL všechny obce
def collect_municipalities(url):
    # Provede požadavek na URL z prvního argumentu aplikace
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    # Z vráceného HTML se vyberou všechny sloupce tabulky
    rows = soup.select('table tr')
    municipalities = []
    # Projde všechny řádky tabulky
    for row in rows:
        try:
            link = row.select('.cislo a')[0];
            code = str_to_int(link.string)
            href = urljoin(url, link['href'])
            name = row.select('.overflow_name')[0].string
            municipal = collect_votes(code, name, href)
            municipalities.append(municipal)
        except IndexError:
            # V případě, že index (0) pro `link` nebo `name` neexistuje
            # pokračuje se v cyklu. Neexistující index značí hlavičku tabulky.
            continue

    return municipalities

# Sebere z URL všechny hlasy a strany v obci
def collect_votes(code, name, url):
    # Provede další požadavek na konkrétní obec
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    # Z vráceného HTML se vyberou všechny tabulky s počtem hlasů
    tables = soup.select('table')
    # První tabulka se pomocí `pop` metody odstraní z listu a použije k získání
    # kompletního přehledu obce
    summary_table_columns = tables.pop(0).select('tr:nth-child(3) td')
    voters_count = str_to_int(summary_table_columns[3].string)
    issued_envelopes = str_to_int(summary_table_columns[4].string)
    valid_votes = str_to_int(summary_table_columns[7].string)
    parties = []

    # Ostatní tabulky se projdou a získají počty hlasů pro jednotlivé strany
    for table in tables:
        # Vyberou se všechny řádky od třetího a dál, první dva řádky jsou
        # součástí hlavičky tabulky
        rows = table.select('tr:nth-child(n + 3)')
        # Projdou se všechny řádky a uloží se strana s počtem hlasů
        for row in rows:
            columns = row.select('td')
            party_number = columns[0].string
            # Pouze ověření, že řádek tabulky je platný na první pozici obsahuje
            # pořadové číslo strany. Prázdné řádky obsahují například `-`.
            if not party_number.isdecimal():
                continue
            party_name = columns[1].string
            party_votes = str_to_int(columns[2].string)
            parties.append((party_name, party_votes))

    # Vytvoření pomocného objektu s hlasy obce
    return Municipal(
        code, name, url, voters_count, issued_envelopes, valid_votes, parties
    )

# Funkce pro uložení dat obcí do CSV souboru
def save_as_csv(csv_filename, municipalities):
    # List hodnot použit jako hlavička CSV souboru.
    # K listu je připojen generovaný list názvů politických stran
    csv_header = [
        'Kód obce', 'Název obce', 'Voliči v seznamu', 'Vydané obálky',
        'Platné hlasy',
    ] + [name for (name, votes) in municipalities[0].parties]

    # Otevření souboru dle zadaného argumentu při spuštění aplikace
    # a zapsání všech dat
    with open(csv_filename, 'w', newline='') as f:
        writer = csv.writer(f)
        writer.writerow(csv_header)

        for municipal in municipalities:
            writer.writerow(municipal.to_csv_line())

# Konverze řetězce na celé číslo. V HTML je použita nezalomitelné mezera `\xa0`,
# kterou je potřeba společně s obyčejnou mezerou odstranit před samotnou konverzí
def str_to_int(value):
    return int(value.replace(' ', '').replace('\xa0', ''))

if __name__ == '__main__':
    # Použití standardního parseru pro zadané argumenty při spuštění aplikace
    parser = ArgumentParser(prog='volby', description='Export výsledků voleb')
    # První argument je URL územního celku
    parser.add_argument('url')
    # Název výstupního souboru včetně `.csv`
    parser.add_argument('output')
    args = parser.parse_args()

    municipalities = collect_municipalities(args.url)
    save_as_csv(args.output, municipalities)
