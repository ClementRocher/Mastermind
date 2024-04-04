import tkinter as tk
import customtkinter as ctf

def changement_couleur(b):
    couleur_suivante = couleur_suivante_dict[couleur_actuelle.get()]
    b.config(bg=couleur_suivante,text=f"{couleur_suivante}")
    couleur_actuelle.set(couleur_suivante)

def envoyer_essai():
    
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
#frame_grille=tk.Frame(root)

bouton_quitter_jeu = tk.Button(root,text="Quitter", command=quitter)
bouton_quitter_jeu.place(x=800, y=800, anchor="e")


#Crée des boutons et les positionne dans la grille
compteur=0
while compteur<10:
    for row in range(10):
        for col in range(4):
            if row==compteur:
                button = tk.Button(root, text=f"{couleur_actuelle.get()}",bg ='red',height= 5, width=15)
                button.config(command=lambda b=button : changement_couleur(b))

                button.grid(row=row, column=col)
            elif row<compteur:
                button = tk.Button(root, text="Couleur fixe",bg ='yellow',state="disabled",height= 5, width=15)
                button.grid(row=row, column=col)
            else:
                button = tk.Button(root, bg="white", text=f"Désactivé",state="disabled",height= 5, width=15)
                button.grid(row=row, column=col)
    var = tk.IntVar()
    buttonWait = tk.Button(root, text="Essai", command=envoyer_essai)
    buttonWait.place(x=500, y=500, anchor="c")
    buttonWait.wait_variable(var)
    compteur+=1




#frame_grille.pack()
#Lance la boucle principale de l'application
root.mainloop()





# button = ctk.CTkButton(master=root, corner_radius=10,text=f"{couleur_actuelle.get()}",bg_color ='red')
#                 button.configure(command=lambda b=button : changement_couleur(b))
