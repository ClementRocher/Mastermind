import tkinter as tk
import customtkinter as ctf

###Fonction pour gérer le changement de couleur des boutons
def changement_couleur(b):
    couleur_suivante = couleur_suivante_dict[couleur_actuelle.get()]
    b.config(bg=couleur_suivante)
    couleur_actuelle.set(couleur_suivante)

def envoyer_essai():
    
    ###récupérer les couleurs des boutons en cours
    #c'est ici qu'on utilise le dico stockage des valeurs
    

    ###figer les boutons en cours

    ###Comparer avec l'ordinateur ce qui nous donne les indices

    ###afficher les indices


    var.set(1)
    #print(row,col)


def quitter():
    exit()

# Création de la fenêtre principale
root = tk.Tk()
root.geometry("1200x1000")
root.title("Changement de couleur")

# Dictionnaire pour définir les couleurs suivantes
couleur_suivante_dict = {"green": "yellow", "yellow": "red", "red": "blue","blue": "white","white": "purple","purple": "green"}

# Variable pour suivre la couleur actuelle
couleur_actuelle = tk.StringVar()
couleur_actuelle.set("red")

#Frame contenant la grille
frame_grille_couleur=tk.Frame(root,bd=2, relief="sunken")
frame_grille_indices=tk.Frame(root,bd=2, relief="sunken")
frame_grille_couleur.grid(row=0, column=0, padx=5, pady=5)
frame_grille_indices.grid(row=0, column=1, padx=5, pady=5)

bouton_quitter_jeu = tk.Button(root,text="Quitter", command=quitter)
bouton_quitter_jeu.place(x=800, y=800, anchor="e")


#Crée des boutons et les positionne dans la grille
compteur=0

#Création Frame Couleur
for row in range(10):
    for col in range(4):
        button = tk.Button(frame_grille_couleur, bg="grey", text="",state="disabled",height= 5, width=15)
        button.grid(row=row, column=col,padx=1, pady=1)

#Création Frame Indices
for row in range(10):
    for col in range(4):
        button = tk.Button(frame_grille_indices, bg="black", text="",state="disabled",height= 5, width=5)
        button.grid(row=row, column=col,padx=1, pady=1)

while compteur<10:

    button_recup1 = frame_grille_couleur.grid_slaves(row=compteur,column=0)[0]
    button_recup1.config(command=lambda b=button_recup1 : changement_couleur(b),state="active")
    
    button_recup2 = frame_grille_couleur.grid_slaves(row=compteur,column=1)[0]
    button_recup2.config(command=lambda b=button_recup2 : changement_couleur(b),state="active")

    button_recup3 = frame_grille_couleur.grid_slaves(row=compteur,column=2)[0]
    button_recup3.config(command=lambda b=button_recup3 : changement_couleur(b),state="active")

    button_recup4 = frame_grille_couleur.grid_slaves(row=compteur,column=3)[0]
    button_recup4.config(command=lambda b=button_recup4 : changement_couleur(b),state="active")

    var = tk.IntVar()
    buttonWait = tk.Button(root, text="Essai", command=envoyer_essai)
    buttonWait.place(x=500, y=500, anchor="c")
    buttonWait.wait_variable(var)
    compteur+=1


#Lance la boucle principale de l'application
root.mainloop()
