import os

naam = input("Hallo wat is je naam: ")
os.system("clear")
begin = input("Welkom {} type (a) om een woordenlijst te maken of (b) om de woorden te leren ".format(naam))
global woordenlijst_naam

if (begin == "a"):
    print("woordenlijst maken")
    woordenlijst_naam = input("geef het bestand een naam ")
    with open(woordenlijst_naam,"w+") as f:
        bestand_lezen = f.write("hey")


elif (begin == "b"):
    print("woorden leren")
else:
    print("hey hey hey de ingevoerde letter is niet geldig")
