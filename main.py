# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/

# Declararea unei liste
lista_initiala = [7, 8, 9, 2, 3, 1, 4, 10, 5, 6]

# Afișarea listei ordonate ascendent (fără a modifica lista inițială)
lista_ascendent = sorted(lista_initiala)
print("Lista ordonată ascendent:", lista_ascendent)

# Afișarea listei ordonate descendent (fără a modifica lista inițială)
lista_descendent = sorted(lista_initiala, reverse=True)
print("Lista ordonată descendent:", lista_descendent)

# Afișarea numerelor cu indici pari din listă (folosind slice)
numere_indici_pari = lista_initiala[::2]
print("Numere cu indici pari:", numere_indici_pari)

# Afișarea numerelor cu indici impari din listă (folosind slice)
numere_indici_impari = lista_initiala[1::2]
print("Numere cu indici impari:", numere_indici_impari)

# Afișarea elementelor multipli ai lui 3
multiplii_de_3 = [numar for numar in lista_initiala if numar % 3 == 0]
print("Elemente multipli ai lui 3:", multiplii_de_3)