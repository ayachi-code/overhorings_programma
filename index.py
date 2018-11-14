import os
import random
import time 

def o_lezen(overschrijven):
    print(overschrijven)
    with open("woordenlijsten/{}".format(overschrijven),"r+") as m:
        regel1 = m.readlines(1)
        a = regel1[0].split("\n")
        bestand_in_array = {} 
        bestand_in_array[1] = a[0]
        lengte = 1
        bestand = m.read()
        bestand_geen_regel = bestand.split("\n")
        index_spatie = bestand_geen_regel.index('')
        del bestand_geen_regel[index_spatie]
        for woorden in bestand_geen_regel:
              lengte += 1
              print(str(lengte) + " " + woorden)
              bestand_in_array[lengte] = woorden
        m.close()
    return bestand_in_array

def o_schrijven(overschrijven):
    os.system("clear")
    bestand_in_array = o_lezen(overschrijven)
    print(bestand_in_array)
    print(overschrijven)
    with open("woordenlijsten/{}".format(overschrijven),"w") as c:
        welke = int(input("Welke lijn wil je wijzigen: "))
        naar = input("Naar welke waarde wil je {}: ".format(bestand_in_array[welke]))
        bestand_in_array[welke] = naar
        for index in bestand_in_array:
             print(index)
             print(bestand_in_array[index])
             c.write(bestand_in_array[index] + "\n")
        c.close()
        main()   

def prepare_overhoren(naam):
    with open("woordenlijsten/{}".format(naam),"r+") as f:
        regel1 = f.readlines(1)
        bestand = f.read()
        bestandstring = "".join(regel1)
        isgaatweg = bestandstring.replace("="," ")
        geenspatie = isgaatweg.split(" ")
        leren_taal = geenspatie[1].replace("\n","")
        lezen_lijst_van_woorden = bestand.split("\n")
        index_van_lijst_woorden = len(lezen_lijst_van_woorden) - 1
        lezen_lijst_van_woorden.remove(lezen_lijst_van_woorden[index_van_lijst_woorden])
        lijst_die_de_woorden_apart_doet = []
        woordenlijst = {}
        f.close()
        for woord in lezen_lijst_van_woorden:
            woord_taal,woord_vertaal = woord.split("=")
            lijst_die_de_woorden_apart_doet.append(woord_taal)
            lijst_die_de_woorden_apart_doet.append(woord_vertaal)  
            woordenlijst[woord_taal] = woord_vertaal
    return woordenlijst,leren_taal


def overhoren_nu(naam):
    woordenlijst = prepare_overhoren(naam)
    random_key = random.choice(list(woordenlijst[0].keys()))
    woorden_user_overhoren = leesInput("Wat is {} in het {}: ".format(random_key,woordenlijst[1]))
    if woorden_user_overhoren == woordenlijst[0][random_key]:
        print("juist")
    elif woorden_user_overhoren == "/stop":
        main()
    else:
        print("fout hmmm")
    while woorden_user_overhoren != "/stop":
        random_key = random.choice(list(woordenlijst[0].keys()))
        woorden_user_overhoren = leesInput("Wat is {} in het {}: ".format(random_key,woordenlijst[1]))
        if woorden_user_overhoren == woordenlijst[0][random_key]:
            print("juist goedzo")
        elif woorden_user_overhoren == "/stop":
            main()
        else:
            print("fout hmmm")


def leesInput(tekst):
    resultaat = input(tekst)
    return resultaat

def welkom():
    os.system("clear")
    welkom.begin = leesInput(" (a) om een woordenlijst te maken  \n (e) voor exit type \n (r) om een bestand te verwijderen \n (o) om een bestand te overhoren ")

def bestaat_bestand(naam): 
    bestaat = os.path.isfile("woordenlijsten/{}".format(naam))
    if bestaat:
        return True
    else: 
        return False

def bestanden_van_woordenlijst_printen(naam):
    bestanden_in_woordenlijsten = os.listdir(naam)
    if not bestanden_in_woordenlijsten:
        print("Er zijn geen woordenlijsten te vinden dus je kan niks verwijderen")
    else:
        for bestand in bestanden_in_woordenlijsten:
            print(bestand)

def maken():
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

def overschrijven():
    os.system("clear")
    bestanden_van_woordenlijst_printen("woordenlijsten")
    overschrijven = leesInput("Welke bestand wil je overschrijven: ")
    bestaat = bestaat_bestand(overschrijven)
    if bestaat:
        bestand_in_array = o_lezen(overschrijven)
        print(bestand_in_array)
        o_schrijven(overschrijven)   
    else:
        print("bestand bestaat niet")
        main()

def woordenlijst_maken():
    check = leesInput("wil je een woordenlijst maken(m) of overschrijven(o): ")
    if check == "m":
        maken()
        os.system("clear")
    elif check == "o":
        overschrijven()
    elif check == "/stop":
        main()
    else:
        print("Er word een foute karakter ingevoerd")
        woordenlijst_maken()
     
def bestand_verwijderen():
    os.system("clear")
    bestanden_van_woordenlijst_printen("woordenlijsten")
    bestand_die_je_wilt_verwijderen_naam = leesInput("Hey welk bestand wil je verwijderen :) ")
    bestaat_het = bestaat_bestand(bestand_die_je_wilt_verwijderen_naam)
    if bestaat_het:
        os.remove("woordenlijsten/{}".format(bestand_die_je_wilt_verwijderen_naam))
        main()
    elif bestand_die_je_wilt_verwijderen_naam == "/stop":
        main()
    else:
        print("nee het bestand bestaat niet probeer het opnieuw")
        time.sleep(1)
        bestand_verwijderen()

def welkom_bestand_overhoren():
    os.system("clear")
    bestanden_van_woordenlijst_printen("woordenlijsten")
    bestand_die_je_wilt_gaan_overhoren = leesInput("Type het bestand naam die je wilt gaan overhoren: ")
    overhoren_bestaat = os.path.isfile("woordenlijsten/{}".format(bestand_die_je_wilt_gaan_overhoren))
    if bestand_die_je_wilt_gaan_overhoren == "/stop":
        main()
    else:
        if overhoren_bestaat:
            return bestand_die_je_wilt_gaan_overhoren,True
        else:
            return bestand_die_je_wilt_gaan_overhoren,False

def bestand_overhoren():
    bestaat_bestand = welkom_bestand_overhoren()
    if bestaat_bestand[1]:
          prepare_overhoren(bestaat_bestand[0])
          overhoren_nu(bestaat_bestand[0]) 
    else:
        print("hey bestand bestaat niet probeer het nog eens :) ")
        time.sleep(2)
        welkom_bestand_overhoren()

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
    else:
        print("hmm ingevoerede karakter bestaat niet ")
        time.sleep(1)
        main()

main()