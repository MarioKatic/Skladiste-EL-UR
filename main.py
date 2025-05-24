# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
from matematika import zbroji, oduzmi, pomnozi  # uvoz funkcija iz nove skripte
from csv_parser import ucitaj_csv, spremi_u_csv, filtriraj_podatke


def print_hi(name):
    print(f'Hi, {name}')


def test_csv():
    # Primjer podataka
    test_podaci = [
        {"dobavljac": "Farnell", "kataloska oznaka": "1", "kolicina": "12", "cjena(EUR)": "1.14", "opis": "otpornik"},
        {"dobavljac": "Mouser", "kataloska oznaka": "2", "kolicina": "11", "cjena(EUR)": "5.11", "opis": "kondenzator"},
        {"dobavljac": "Digykey", "kataloska oznaka": "3", "kolicina": "8", "cjena(EUR)": "7.30", "opis": "microcontroller"}
    ]

    # Spremanje podataka u CSV
    if spremi_u_csv(test_podaci, 'materijal.csv'):
        print("Podaci uspješno spremljeni u CSV")

    # Učitavanje podataka iz CSV-a
    ucitani_podaci = ucitaj_csv('materijal.csv')
    print("\nUčitani podaci iz CSV-a:")
    for red in ucitani_podaci:
        print(red)

    # Primjer filtriranja - samo dobavlkjać iz Digykey
    digykey_filter = lambda x: x['dobavljac'] == 'Digykey'
    digykey_filter = filtriraj_podatke(ucitani_podaci, digykey_filter)

    print("\nkomponente dobavljaca Digykey:")
    for opis in digykey_filter:
        print(opis)


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')

    # Poziv nove funkcije
    # Testiranje funkcija iz nove skripte
    print(f'Zbroj 5 i 3 je: {zbroji(5, 3)}')
    print(f'Razlika 10 i 4 je: {oduzmi(10, 4)}')
    print(f'Umnožak 6 i 7 je: {pomnozi(6, 7)}')

    print("\nTestiranje CSV funkcija:")
    test_csv()


# See PyCharm help at https://www.jetbrains.com/help/pycharm/