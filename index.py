import os

global woordenlijst_naam
global mape
global taal
global nederlands
global vertaal

naam = input("Hallo wat is je naam: ")
os.system("clear")
begin = input("Welkom {} type (a) om een woordenlijst te maken of (b) om de woorden te leren of (c) voor help ".format(naam))


if (begin == "a"):
    print("woordenlijst maken")
    woordenlijst_naam = input("geef het bestand een naam ")
    mape = os.path.join('woordenlijsten',woordenlijst_naam)
    vertaal = input("Van welke taal wil je het vertalen ")
    taal = input("Welke taal ben ja aan het leren(woorden stampen) ")
    os.system("clear")
    print("Oke type nu eerst de {} woord ".format(vertaal))
   # with open(mape,"w+") as f:
    #    bestand_lezen = f.write("hallo ")

elif (begin == "b"):
    print("woorden leren")
elif (begin == "c"):
    print("help krijgen")
else:
    print("hey hey hey de ingevoerde letter is niet geldig")
