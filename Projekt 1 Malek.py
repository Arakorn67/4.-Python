# projekt_1.py: první projekt do Engeto Online Python Akademie
# author: Ondrej Malek
# email: ondrej.malek@dpb.cz
# discord: Arakorn67//76

# Přihlašovací údaje
users = {
    'bob': '123',
    'ann': 'pass123',
    'mike': 'password123',
    'liz': 'pass123'
}

# Texty k analýze
TEXTS = ['''
Situated about 10 miles west of Kemmerer,
Fossil Butte is a ruggedly impressive
topographic feature that rises sharply
some 1000 feet above Twin Creek Valley
to an elevation of more than 7500 feet
above sea level. The butte is located just
north of US 30N and the Union Pacific Railroad,
which traverse the valley. ''',
'''At the base of Fossil Butte are the bright
red, purple, yellow and gray beds of the Wasatch
Formation. Eroded portions of these horizontal
beds slope gradually upward from the valley floor
and steepen abruptly. Overlying them and extending
to the top of the butte are the much steeper
buff-to-white beds of the Green River Formation,
which are about 300 feet thick.''',
'''The monument contains 8198 acres and protects
a portion of the largest deposit of freshwater fish
fossils in the world. The richest fossil fish deposits
are found in multiple limestone layers, which lie some
100 feet below the top of the butte. The fossils
represent several varieties of perch, as well as
other freshwater genera and herring similar to those
in modern oceans. Other fish such as paddlefish,
garpike and stingray are also present.''']  

# Přihlašování uživatele
username = input('username: ')
password = input('password: ')

if users.get(username) == password:
    print(f"----------------------------------------\nWelcome to the app, {username}")
else:
    print("unregistered user, terminating the program..")
    exit()

# Výběr textu
print("We have 3 texts to be analyzed.")
text_choice = input("Enter a number btw. 1 and 3 to select: ")
if not text_choice.isdigit() or not 1 <= int(text_choice) <= 3:
    print("Invalid input, terminating the program..")
    exit()

# Analýza textu
text = TEXTS[int(text_choice) - 1]
words = text.split()
word_count = len(words)
titlecase = sum(1 for word in words if word.istitle())
uppercase = sum(1 for word in words if word.isupper() and not word.isdigit())
lowercase = sum(1 for word in words if word.islower())
numeric = sum(1 for word in words if word.isdigit())
sum_numbers = sum(int(word) for word in words if word.isdigit())

# Zobrazení statistik
print(f"There are {word_count} words in the selected text.")
print(f"There are {titlecase} titlecase words.")
print(f"There are {uppercase} uppercase words.")
print(f"There are {lowercase} lowercase words.")
print(f"There are {numeric} numeric strings.")
print(f"The sum of all the numbers {sum_numbers}")

# Graf délek slov
word_lengths = {}
for word in words:
    length = len(word)
    word_lengths[length] = word_lengths.get(length, 0) + 1

# Výpočet maximální délky sloupce pro graf
max_length_count = max(word_lengths.values())

print("----------------------------------------")
print("LEN|  OCCURENCES  |NR.")
for length in range(1, max(word_lengths.keys()) + 1):
    occurrences = word_lengths.get(length, 0)
    # Vykreslení grafu s využitím zarovnání vpravo
    print(f"{length:3}|{'*' * occurrences: <{max_length_count}}|{occurrences}")

