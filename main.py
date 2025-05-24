# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
from matematika import zbroji, oduzmi, pomnozi  # uvoz funkcija iz nove skripte


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

# See PyCharm help at https://www.jetbrains.com/help/pycharm/