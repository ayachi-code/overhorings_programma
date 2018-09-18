#Todo: mijn programma structuur geven

import os




def welkom():
    naam = input("Hallo wat is je naam: ")
    os.system("clear")
    welkom.begin = input("Welkom {} type (a) om een woordenlijst te maken of (b) om de woorden te leren of (c) voor help ".format(naam))


def woordenlijst_maken():
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
        if woorden == "/stop":
            break 



def main():
    welkom()
    if  welkom.begin == "a":
        woordenlijst_maken()

main()