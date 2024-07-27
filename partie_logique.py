from subprocess import *

import qrcode


def get_network_names():
    commande1 = ["netsh", "wlan", "show", "profiles"]
    process = run(commande1, capture_output=True, text=True, check=True)
    resulat = process.stdout
    liste_wifi = []
    try:
        resul = (resulat.split("Profils utilisateurs")[1]).strip().splitlines()
        for ligne in resul:
            if ":" in ligne:
                liste_wifi.append(ligne.split(":")[1])
    except:
        pass
    return liste_wifi

def show_passord(network_name):
    commande = ["netsh", "wlan", "show", "profile", "name=", str(network_name), "key=", "clear"]
    process = run(commande, capture_output=True, text=True)
    resultat ,result= process.stdout,""

    try:
        resultat = (resultat.split("Contenu de ")[1]).splitlines()
        resultat = resultat[0].split(":")[1]
        if resultat:
            result = resultat

    except:
        pass
    return result

def qrcode_generator(encryption, ssid, password):

    data = f"WIFI:T:{encryption};S:{ssid};P:{password};;"
    img = qrcode.make(data)
    img.show()


