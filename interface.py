from tkinter import *
from tkinter import ttk, filedialog, messagebox
from partie_logique import get_network_names, show_passord, qrcode_generator
import pyperclip as p
from tkinter import PhotoImage
root = Tk()
root.geometry("530x460")
icon=PhotoImage(file="wifi.png")
root.iconphoto(True,icon)
root.title("Find Connected WIFI Password" + " Powered by Edouard ZONGO 66169083")
root.minsize(width=530, height=420)
root.maxsize(width=650, height=500)
values = [i.strip() for i in get_network_names()]

number_call_qrcode_func=0

def show_qrcode():

    if find_pwd1()[0] or function1()[0]:
        if find_pwd1()[0]:
            qrcode_generator("WPA||WPA2", find_pwd1()[2], find_pwd1()[1])
            show_qrcode_button.config(state=DISABLED)

        elif function1()[0]:
            qrcode_generator("WPA", function1()[2], function1()[1])
            show_qrcode_button.config(state=DISABLED)




    elif not find_pwd1()[0] and   not function1()[0]:
        messagebox.showerror("Erreur de Qrcode"," impossible de generer Qrcode "+"\n"+"Mot de passe vide ")




def copy_password():
    if find_pwd1()[0] or function1()[0]:
        if find_pwd1()[0]:
            p.copy(find_pwd1()[1])
            messagebox.showinfo("copie du mot de passe sur presse papier","mot de passe copié" + "\n" + " sur le presse papier avec succès")
        if function1()[0]:
            p.copy(function1()[1])
            messagebox.showinfo("copie du mot de passe sur presse papier","mot de passe copié" + "\n" + " sur le presse papier avec succès")
    elif not find_pwd1()[0] and not function1()[0]:
        messagebox.showerror("ERREUR DE COPIE", "Erreur de copie " + "\n" + "Mot de passe vide")


def find_pwd():
    c = entry_wifi.get().strip()
    if find_pwd1()[0]:
        resultat_label.config(text=show_passord(str(c)), bg="green")
        message.config(text="Le Mot de Passe de " + str(c) + " est:")
    elif show_passord(c) == "":
        message.config(text="désole le réseau " + str(c) + " n'esxiste pas")
        resultat_label.config(text="", bg="green")
        

def function1(*args):
    c = combo.get().strip()
    status = False
    if show_passord(c) != "":
        status=True
        show_qrcode_button.config(state=ACTIVE)
    else:
        pass
    return status, show_passord(str(c)), c


def find_pwd1():
    c = entry_wifi.get().strip()
    status = False
    if show_passord(c) != "":
        status=True
    else:
        pass
    return status, show_passord(str(c)), c
        

def function(*args):
    c = combo.get().strip()
    if function1()[0]:
        resultat_label.config(text=show_passord(str(c)), bg="green")
        message.config(text="Le Mot de Passe de " + str(c) + " est:")
    else:
        message.config(text="désole le réseau " + str(c) + " n'esxiste pas")
        resultat_label.config(text="vous pouvez saisir le nom  du réseau pour verifier")


def get_file_name():
    file_path = filedialog.askdirectory()
    return file_path


def save():
    path = get_file_name()
    path=path+"/liste des wifi connectés.txt"
    print(path)
    try:
        with open(path, "w") as f:
            for i in get_network_names():
                f.writelines(i.strip() + " :" + str(show_passord(i.strip())) + "\n")
        f.close()
        messagebox.showinfo("Enregistrement", message="Enregistré avec succès")
    except:
            messagebox.showerror(title="Erreur de chemin de sauvegarde",message="chemin incorrect")
            pass


combo = ttk.Combobox(root, values=values, font="Arrial 15 bold", state="readonly")
combo.set("Selectionner le réseau ")
combo.bind("<<ComboboxSelected>>", function)
resultat_label = Label(root, text="", font="Helvetica 16 bold")
message = Label(root, text="", font="Helvetica 13 bold")
message.place(x=10, y=100)
resultat_label.place(x=10, y=150)
Label(root, text="liste des réseaux que vous vous êtes connectés(es)!", font="Helvetica 14 bold").place(x=0, y=10)
combo.place(x=50, y=60)
enregistrer_button = Button(root, text="Save Password", font="Helvetica 12 bold", command=save, fg="blue")
enregistrer_button.place(x=350, y=60)
message_en_cas_erreur_label = Label(root, text="Tapez le nom du wifi ici:", font="Helvetica 18 bold")
message_en_cas_erreur_label.place(x=10, y=330)
entry_wifi = Entry(root, width=17, font="Helvetica 15 bold")
entry_wifi.place(x=300, y=340)
button_trover_mot_de_passe = Button(root, text="find password", command=find_pwd, bg="#088A4b",
                                    font="Helvetica 14 bold")
button_trover_mot_de_passe.place(x=300, y=380)

copy_button = Button(root, text="copy password", font="Helvetica 12 bold", command=copy_password)
copy_button.place(x=60, y=200)
show_qrcode_button = Button(root, text="QR CODE", font="Helvetica 12 bold", command=show_qrcode)
show_qrcode_button.place(x=60, y=260)


root.mainloop()
