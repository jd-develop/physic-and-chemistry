#!/usr/bin/env python3
# coding:utf-8
# lentilles minces convergentes

choix = "None"
while not choix.isdigit() or choix not in "12":
    choix = input(
        "taper 1 pour déterminer la position de l'image et le grandissement.\ntaper 2 pour déterminer la taille de l'image.\n")
choix = int(choix)

if choix == 1:
    d_focale = float(input("indiquer la distance focale de la lentille en cm \n"))
    X_A = float(input("indiquer la valeur de X_A de l'objet en cm \n"))

    while X_A > 0:
        print("Erreur, la valeur doit être négative")
        X_A = float(input("indiquer la valeur de X_A de l'objet en cm \n"))

    X_A_prime = 1 / (1 / d_focale + 1 / X_A)
    gamma = round(X_A_prime / X_A, 2)

    print("l'abscisse de A_prime est égale à", round(X_A_prime, 3), "cm et le grandissement est égal à ", gamma)

    if X_A_prime < 0:
        print("l'image est virtuelle")
    else:
        print("l'image est réelle")

    if abs(gamma) > 1:  # abs signifie valeur absolue
        print("l'image est agrandie")
    elif abs(gamma) < 1:
        print("l'image est réduite")
    else:
        print("l'image a la même taille que l'objet")

    if gamma > 0:
        print("l'image est droite")
    else:
        print("l'image est renversée")

elif choix == 2:
    d_focale = float(input("indiquer la distance focale de la lentille en cm \n"))
    X_A = float(input("indiquer la valeur de X_A de l'objet en cm \n"))
    AB = float(input("indiquer la valeur de AB algébrique en cm\n"))

    while X_A > 0:
        print("Erreur, la valeur doit être négative")
        X_A = float(input("indiquer la valeur de X_A de l'objet en cm \n"))

    X_A_prime = 1 / (1 / d_focale + 1 / X_A)
    gamma = round(X_A_prime / X_A, 2)

    A_prime_B_prime = round(gamma * AB, 3)
    print(f"la taille de l'image est {A_prime_B_prime}.")
