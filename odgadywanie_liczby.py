import random

print("Odgadnij ukryta liczbe z przedziału od 0 do 10.")
print('')

wylosowana_liczba = random.randrange(0, 11)

for szanse in range(3, 0, -1):
    print('Masz', szanse, 'szanse')
    szanse -= 1

    liczba_uzytkownika = int(input('Podaj liczbe: '))

    if liczba_uzytkownika < wylosowana_liczba:
        print("Nie trafiles. Ukryta liczba jest wieksza")
    elif liczba_uzytkownika > wylosowana_liczba:
        print("Nie trafiles. Ukryta liczba jest mniejsza")
    else:
        print("Brawo!!! Trafiles!!! Wygrywasz 1 000 000 $ !!!")
        break

    if szanse == 0:
        print('Przegrales!!!')
        break
