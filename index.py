import os

naam = input("Hallo wat is je naam: ")
os.system("clear")
begin = input("Welkom {} type (a) om een woordenlijst te maken of (b) om de woorden te leren ".format(naam))
global woordenlijst_naam
global mape
global taal
global nederlands

if (begin == "a"):
    print("woordenlijst maken")
    woordenlijst_naam = input("geef het bestand een naam ")
    mape = os.path.join('woordenlijsten',woordenlijst_naam)
    taal = input("Welke taal ben ja aan het leren(woorden stampen) ")
    os.system("clear")

   # with open(mape,"w+") as f:
    #    bestand_lezen = f.write("hallo ")

elif (begin == "b"):
    print("woorden leren")
else:
    print("hey hey hey de ingevoerde letter is niet geldig")
