import os
import random

def leesInput(tekst):
    resultaat = input(tekst)
    return resultaat

def welkom():
    os.system("clear")
    welkom.begin = leesInput(" (a) om een woordenlijst te maken \n (b) om de woorden te leren  (c) voor help \n (e) voor exit type \n (r) om een bestand te verwijderen \n (o) om een bestand te overhoren ")

def woordenlijst_maken():
    print("woordenlijst maken")
    woordenlijst_naam = leesInput("geef het bestand een naam ")
    mape = os.path.join('woordenlijsten',woordenlijst_naam)    
    vertaal = leesInput("Van welke taal wil je het vertalen ")
    taal = leesInput("Welke taal ben ja aan het leren(woorden stampen) ")
    mix = vertaal + "=" + taal
    os.system("clear")
    woorden2 = {vertaal:[],taal:[]}
    woorden = leesInput("type je {} woord ".format(vertaal))
    while woorden != "/stop":
        woorden_die_je_stampt = leesInput("type je {} woord ".format(taal))
        woorden2[vertaal].append(woorden)
        woorden2[taal].append(woorden_die_je_stampt)
        with open(mape,"w+") as f:
            f.write(mix + "\n")
            for vertaal_woorden,taal_woorden in zip(woorden2[vertaal],woorden2[taal]):
                voledige_woord = vertaal_woorden + "=" + taal_woorden
                f.write(voledige_woord + "\n")
                
            f.close()
        woorden = leesInput("type je {} woord ".format(vertaal))

    main()

def bestand_verwijderen():
    os.system("clear")
    bestanden_in_woordenlijsten = os.listdir("woordenlijsten")
    if not bestanden_in_woordenlijsten:
        print("Er zijn geen woordenlijsten te vinden dus je kan niks verwijderen")
    else:
        for bestand in bestanden_in_woordenlijsten:
            print(bestand);
    bestand_die_je_wilt_verwijderen_naam = leesInput("Hey welk bestand wil je verwijderen :) ")
    bestand_die_verwijderd_word = os.path.isfile("woordenlijsten/{}".format(bestand_die_je_wilt_verwijderen_naam))
    if bestand_die_verwijderd_word == True:
        os.remove("woordenlijsten/{}".format(bestand_die_je_wilt_verwijderen_naam))
        main()

    else:
        print("nee het bestand bestaat niet probeer het opnieuw")
        

def bestand_overhoren():
    os.system("clear")
    bestand_die_je_wilt_gaan_overhoren = leesInput("Type het bestand naam die je wilt gaan overhoren: ")
    bestand_die_verwijderd_word_overhoren = os.path.isfile("woordenlijsten/{}".format(bestand_die_je_wilt_gaan_overhoren))
    if bestand_die_verwijderd_word_overhoren:
        with open("woordenlijsten/{}".format(bestand_die_je_wilt_gaan_overhoren),"r+") as f:
          regel1 = f.readlines(1)
          bestand = f.read()
          bestandstring = "".join(regel1)
          isgaatweg = bestandstring.replace("="," ")
          geenspatie = isgaatweg.split(" ")
          leren_taal = geenspatie[1].replace("\n","")
          taal_begin = geenspatie[0]
          lezen_lijst_van_woorden = bestand.split("\n")
          index_van_lijst_woorden = len(lezen_lijst_van_woorden) - 1
          random_nummer_van_index_lijst = random.randint(0,index_van_lijst_woorden)
          woorden_user_overhoren = leesInput("Wat is hallo in het {}: ".format(leren_taal))
          while woorden_user_overhoren != "/stop":
              woorden_user_overhoren = leesInput("Wat is hallo in het {}: ".format(leren_taal))
          
     
    else:
        print("hey bestand bestaat niet ")


def main():
    welkom()
    if  welkom.begin == "a":
        woordenlijst_maken()
    elif welkom.begin == "e":
        exit()              
    elif welkom.begin == "r":
        bestand_verwijderen()
    elif welkom.begin == "o":
        bestand_overhoren()

main()