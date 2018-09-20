import os

def welkom():
    os.system("clear")
    welkom.begin = input("Welkom type (a) om een woordenlijst te maken of (b) om de woorden te leren of (c) voor help ")

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
            for taal_woorden,vertaal_woorden in zip(woorden2["vertaal"],woorden2["taal"])
                #f.write("\n".join(woorden2[taal])+ "\n")
                #print()
                
            f.close()

        if woorden == "/stop":
            break
    main()

def main():
    welkom()
    if  welkom.begin == "a":
        woordenlijst_maken()

main()