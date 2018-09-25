import os

def welkom():
    os.system("clear")
    welkom.begin = input(" (a) om een woordenlijst te maken \n (b) om de woorden te leren \n (c) voor help \n (e) voor exit type \n (r) om een bestand te verwijderen ")

def woordenlijst_maken():
    print("woordenlijst maken")
    woordenlijst_naam = input("geef het bestand een naam ")
    mape = os.path.join('woordenlijsten',woordenlijst_naam)    
    vertaal = input("Van welke taal wil je het vertalen ")
    taal = input("Welke taal ben ja aan het leren(woorden stampen) ")
    os.system("clear")
    woorden2 = {vertaal:[],taal:[]}
    while True:
        woorden = input("type je {} woord ".format(vertaal))
        woorden_die_je_stampt = input("type je {} woord ".format(taal))
        woorden2[vertaal].append(woorden)
        woorden2[taal].append(woorden_die_je_stampt)
        with open(mape,"w+") as f:
            for vertaal_woorden,taal_woorden in zip(woorden2[vertaal],woorden2[taal]):
                voledige_woord = vertaal_woorden + "=" + taal_woorden
                f.write(voledige_woord + "\n")
                
            f.close()

        if woorden == "/stop":
            break
    main()

def bestand_verwijderen():
    bestanden_in_woordenlijsten = os.listdir("woordenlijsten")
    print(bestanden_in_woordenlijsten)

def main():
    welkom()
    if  welkom.begin == "a":
        woordenlijst_maken()
    elif welkom.begin == "e":
        exit()
    elif welkom.begin == "r":
        bestand_verwijderen()
       

        

main()