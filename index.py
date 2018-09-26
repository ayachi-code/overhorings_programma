import os

def leesInput(tekst):
    resultaat = input(tekst)
    return resultaat

def welkom():
    os.system("clear")
    welkom.begin = leesInput(" (a) om een woordenlijst te maken \n (b) om de woorden te leren \n (c) voor help \n (e) voor exit type \n (r) om een bestand te verwijderen \n (o) om een bestand te overhoren ")

def woordenlijst_maken():
    # leesInput("woordenlijst maken")
    print("woordenlijst maken")
    woordenlijst_naam = leesInput("geef het bestand een naam ")
    mape = os.path.join('woordenlijsten',woordenlijst_naam)    
    vertaal = leesInput("Van welke taal wil je het vertalen ")
    taal = leesInput("Welke taal ben ja aan het leren(woorden stampen) ")
    os.system("clear")
    woorden2 = {vertaal:[],taal:[]}
    woorden = leesInput("type je {} woord ".format(vertaal))
    while woorden != "/stop":
        woorden_die_je_stampt = leesInput("type je {} woord ".format(taal))
        woorden2[vertaal].append(woorden)
        woorden2[taal].append(woorden_die_je_stampt)
        with open(mape,"w+") as f:
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
        

def main():
    welkom()
    if  welkom.begin == "a":
        woordenlijst_maken()
    elif welkom.begin == "e":
        exit()
    elif welkom.begin == "r":
        bestand_verwijderen()
       

        

main()