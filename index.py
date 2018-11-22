import os
import firebase_admin
from firebase_admin import credentials
from firebase_admin import db
import random
import time 

#initialiseer de firbase SDK
cred = credentials.Certificate('secret.json')

#Databse conecteren
firebase_admin.initialize_app(cred, {
    'databaseURL': 'https://overhoring-1d14b.firebaseio.com/',
    'databaseAuthVariableOverride': {
        'uid': 'my-service-worker'
    }
})

database = db.reference('tips')
database_lijsten = db.reference('lijsten')


def tipoftop_versturen(welke,zin):
    if zin:
        random_karakter = str(random.randint(1,123748904123789483021980232))
        tip = database.child(random_karakter + "tip")
        tip.set({
            "tip": {
                "tip": "test" + welke
            }
        })
    elif zin == False:
        random_karakter = str(random.randint(1,1237489041237894830219802328))
        top = database.child(random_karakter + "top")
        top.set({
            "top": {
                "top": welke
            }
        })

def tip_geven():
    os.system("clear")
    tip = input("Type je tip: ")
    if tip == "/stop":
        return
    else:
        tipoftop_versturen(tip,True)
        print("tip: ",format(tip))   
        print("Bedankt voor je tip \n ")
        time.sleep(1)
        return True

def top_geven():
    os.system("clear")
    top = input("Type je top: ")
    if top == "/stop":
        return
    else:
        tipoftop_versturen(top,False)
        print("tip: ",format(top))  
        print("Bedankt voor je top \n ")
        time.sleep(1)
        return False

def feedback():
    os.system("clear")
    keuzen = input("Hey type t om een tip te geven en p om ene top tegeven: ")
    if keuzen == "t":
        tip_geven()
    elif keuzen == "p":
        top_geven()
    elif keuzen == "/stop":
        main()

def o_lezen(overschrijven):
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
        return
    else:
        print("fout hmmm")
    while woorden_user_overhoren != "/stop":
        random_key = random.choice(list(woordenlijst[0].keys()))
        woorden_user_overhoren = leesInput("Wat is {} in het {}: ".format(random_key,woordenlijst[1]))
        if woorden_user_overhoren == woordenlijst[0][random_key]:
            print("juist goedzo")
        elif woorden_user_overhoren == "/stop":
            return
        else:
            print("fout hmmm")

def leesInput(tekst):
    resultaat = input(tekst)
    return resultaat

def welkom():
    os.system("clear")
    begin = leesInput(" (a) om een woordenlijst te maken  \n (e) voor exit type \n (r) om een bestand te verwijderen \n (o) om een bestand te overhoren \n (f) om een feedback tegeven \n (p) om een lijst te delen/importeren ")
    return begin

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
        return True
    else:
        print("Er word een foute karakter ingevoerd")
        return False
     
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


def woordenlijst_publish(naam):
    welke = input("Hoe zal het bestand heten als je het bestand wilt downloaden: ")
    with open("woordenlijsten/{}".format(naam),"r+") as x:
        regeaa = x.readlines()
        stringa = ''.join(regeaa)
        x.close()
    lijsten = database_lijsten.child(welke)
    lijsten.set({
            "lijst": stringa
    })
    os.system("clear")

def woorden_lijst_zelf_delen(naam):
    zeker = input("Weet je zeker als je het bestand " + naam + " wilt delen (y) of (n) : ")
    if zeker == "y":
        woordenlijst_publish(naam)
    elif zeker == "n":
        print("Oke niet erg.. ")
        time.sleep(1)
        return
    else:
        print("bestand bestata niet ")

def bestanden_beschikbaar():
    database_lijsten_ = database_lijsten.get()
    alle = list(database_lijsten_.keys())
    for bestanden in alle:
        print(bestanden)

def bestand_downloaden(naam):
    de_lijst = database_lijsten.get()
    print(de_lijst[naam])
    time.sleep(20)

def lijst_importeren():
    os.system("clear")
    bestanden_beschikbaar()
    welke = input("Welke bestand wil je gaan importeren: ")
    bestand_downloaden(welke)

def woorden_lijst_delen():
    os.system("clear")
    welke = input("(p) om te importeren en (v) een lijst te delen: ")
    if welke == "p":
        lijst_importeren()
    elif welke == "v":
        os.system("clear")
        bestanden_van_woordenlijst_printen("woordenlijsten")
        welke = input("Welk bestand wil je gaan delen ? ")
        bestaat = bestaat_bestand(welke)
        if bestaat:
            print("Bestand word gedeelt")
            woorden_lijst_zelf_delen(welke)
        else:
            print("Bestand bestaat niet :( ")
            time.sleep(2)
            return False
    else:
        print("karakter bestaat niet probeer opnieuw")
        time.sleep(1)

def main():
    keuzen = welkom()
    while True:
        if  keuzen == "a":
            while not (woordenlijst_maken()):
                woordenlijst_maken()
        elif keuzen == "f":
            feedback()
        elif keuzen == "e":
            exit()           
        elif keuzen == "r":
            bestand_verwijderen()
        elif keuzen == "o":
            bestand_overhoren()
        elif keuzen == "p":
            woorden_lijst_delen()
        else:
            print("hmm ingevoerede karakter bestaat niet ")
            time.sleep(1)
            keuzen = welkom()
            continue      

main()


#{'frans leren': {'hallo': {'lijst': 'nederlands=engels\na=l\neten=eat\n'}}, 'p': {'lijst': 'nederlands=engels\na=l\neten=eat\n'}}