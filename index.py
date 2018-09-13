#Todo: mijn programma structuur geven


import os


class main(object):
    def __init__(self,woordenlijst_naam,map_naam,taal_2e,taal_die_je_weet,ingevoerde_woord,naam_van_gebruiker,object_van_talen):
        self.woordenlijst_naam = woordenlijst_naam
        self.map_naam = map_naam
        self.taal_2e = taal_2e 
        self.taal_die_je_weet = taal_die_je_weet
        self.ingevoerde_woord = ingevoerde_woord
        self.naam_van_gebruiker = naam_van_gebruiker
        self.object_van_talen = object_van_talen
    def begin_scherm(self,naam):
        self.naam = input("Hallo wat is je naam: ")
        os.system("clear")
        begin = input("Welkom {} type (a) om een woordenlijst te maken of (b) om de woorden te leren of (c) voor help ".format(naam))


'''
global woordenlijst_naam
global mape
global taal
global vertaal
global woorden
global naam
global vertaaaling
global woorden2

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
    print("Oke type nu eerst de {} woorden ".format(vertaal))
    woorden2 = {vertaal:[],taal:[]}
    while True:
        woorden = input("tgype je {} woord ".format(vertaal))
        woorden2[vertaal].append(woorden)
        print(woorden2[vertaal])
        if woorden == "!":
            break 

   # with open(mape,"w+") as f:
    #    bestand_lezen = f.write("hallo ")

elif (begin == "b"):
    print("woorden leren")
elif (begin == "c"):
    print("help krijgen")
else:
    print("hey hey hey de ingevoerde letter is niet geldig")


'''
