!/bin/bash

def kalkulator():
    print("Prosty kalkulator")
    print("Operacje: +, -, *, /")

    liczba1 = float(input("Podaj pierwszą liczbę: "))
    operator = input("Podaj operator (+, -, *, /): ")
    liczba2 = float(input("Podaj drugą liczbę: "))

    if operator == "+":
        wynik = liczba1 + liczba2
    elif operator == "-":
        wynik = liczba1 - liczba2
    elif operator == "*":
        wynik = liczba1 * liczba2
    elif operator == "/":
        if liczba2 == 0:
            print("Błąd: nie można dzielić przez zero.")
            return
        wynik = liczba1 / liczba2
    else:
        print("Nieprawidłowy operator.")
        return
