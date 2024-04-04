
from tkinter import *
from tkinter.ttk import *
import customtkinter
import webbrowser

master = customtkinter.CTk()
master.geometry("900x700")

def button_callback():
    print("button clicked")



def afficher_regles_menu():
    """#newWindow = 
 
    # sets the title of the
    # Toplevel widget
    newWindow.title("Règles du jeu")
 
    # sets the geometry of toplevel
    newWindow.geometry("200x200")
 
    # A Label widget to show in toplevel
    Label(newWindow, 
          text ="This is a new window").pack()
    """

def quitter_jeu():
    exit()

new = 1
url = "https://www.google.com"
def openweb():
    webbrowser.open(url,new=new)


button = customtkinter.CTkButton(master, text="my button", command=openweb)
button.pack(padx=20, pady=20)
bouton_regles = customtkinter.CTkButton(master, text="Afficher les règles", command=afficher_regles_menu)
bouton_regles.pack(padx=20, pady=20)
bouton_quitter = customtkinter.CTkButton(master, text="Quitter le jeu", command=quitter_jeu)
bouton_quitter.pack(padx=20, pady=20)
#bouton_retour_regles = customtkinter.CTkButton(newWindow,text="Retour", command=quitter_jeu)


master.mainloop()