import os

naam = input("Hallo wat is je naam: ")
os.system("clear")
begin = input("Welkom {} type (a) om een woordenlijst te maken of (b) om de woorden te leren ".format(naam))
if (begin == "a"):
    print("woordenlijst maken")
elif (begin == "b"):
    print("woorden leren")
else:
    print("hey hey hey de ingevoerde letter is niet geldig")
