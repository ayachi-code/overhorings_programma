import os

naam = input("Hallo wat is je naam: ")
os.system("clear")
begin = input("Welkom {} type (a) om een woordenlijst te maken of (b) om de woorden te leren ".format(naam))
global woordenlijst_naam
global mape
global taal
global nederlands
global vertaal

if (begin == "a"):
    print("woordenlijst maken")
    woordenlijst_naam = input("geef het bestand een naam ")
    mape = os.path.join('woordenlijsten',woordenlijst_naam)
    vertaal = input("Van welke taal wil je het vertalen ")
    taal = input("Welke taal ben ja aan het leren(woorden stampen) ")
    os.system("clear")
    print("Oke type nu eerst de nederlandse woord")
   # with open(mape,"w+") as f:
    #    bestand_lezen = f.write("hallo ")

elif (begin == "b"):
    print("woorden leren")
else:
    print("hey hey hey de ingevoerde letter is niet geldig")
