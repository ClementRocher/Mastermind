import tkinter as tk
import tkinter as tk

def changement_couleur(b):
    couleur_suivante = couleur_suivante_dict[couleur_actuelle.get()]
    b.config(bg=couleur_suivante)
    couleur_actuelle.set(couleur_suivante)

# Création de la fenêtre principale
root = tk.Tk()
root.title("Changement de couleur")

# Dictionnaire pour définir les couleurs suivantes
couleur_suivante_dict = {"green": "yellow", "yellow": "red", "red": "green"}

# Variable pour suivre la couleur actuelle
couleur_actuelle = tk.StringVar()
couleur_actuelle.set("green")


#Crée des widgets (par exemple, des boutons) et les positionne dans la grille
compteur=0
while compteur<10:
    for row in range(10):
        for col in range(4):
            if row==compteur:
                button = tk.Button(root, text=f"(couleur)",bg ='red')
                button.config(command=lambda b=button : changement_couleur(b))

                button.grid(row=row, column=col, padx=10, pady=10)
            else:
                button = tk.Button(root, bg="white", text=f"(couleur)",state="disabled")
                button.grid(row=row, column=col, padx=10, pady=10)
    var = tk.IntVar()
    buttonWait = tk.Button(root, text="Click Me", command=lambda: var.set(1))
    buttonWait.place(relx=.5, rely=1, anchor="c")
    buttonWait.wait_variable(var)
    compteur+=1


#Lance la boucle principale de l'application
root.mainloop()