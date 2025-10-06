def binary_search(tab, szukana):
 
    l = 0                      # K1
    p = len(tab) - 1          # K2
    sr = (l + p) // 2         # K3
 
    while l <= p:             # K4
        if tab[sr] == szukana:  # K5
            return sr
        elif tab[sr] > szukana:  # K6
            p = sr - 1
        else:
            l = sr + 1
        sr = (l + p) // 2     # K7
 
    return -1  # K8
 
 
# Główna część programu
if __name__ == "__main__":
    # Tablica posortowana według opisu
    tablica = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47]
 
    # Wyświetlenie tablicy
    print("Zbiór danych (posortowana tablica):")
    print(tablica)
 
    # Wejście użytkownika
    try:
        szukana_liczba = int(input("Podaj liczbe, ktora chcesz znalezc: "))
        wynik = binary_search(tablica, szukana_liczba)
 
        if wynik != -1:
            print(f"Liczba {szukana_liczba} wystepuje w zbiorze w komórce o indeksie: {wynik}")
        else:
            print(f"Liczba {szukana_liczba} NIE wystepuje w zbiorze.")
    except ValueError:
        print("Błąd: Wprowadź poprawną liczbę całkowitą.")