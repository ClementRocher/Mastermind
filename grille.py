import tkinter as tk

def changement_couleur():
    print("ha")

#Crée une fenêtre principale
root = tk.Tk()

#Crée des widgets (par exemple, des boutons) et les positionne dans la grille
compteur=0
while compteur<10:
    for row in range(10):
        for col in range(4):
            if row==compteur:
                button = tk.Button(root, width=10,bg="green", command=changement_couleur)
                button.grid(row=row, column=col, padx=10, pady=10)
            else:
                button = tk.Button(root, bg="white",state="disabled")
                button.grid(row=row, column=col, padx=10, pady=10)
    var = tk.IntVar()
    buttonWait = tk.Button(root, text="Click Me", command=lambda: var.set(1))
    buttonWait.place(relx=.5, rely=1, anchor="c")
    buttonWait.wait_variable(var)
    compteur+=1


#Lance la boucle principale de l'application
root.mainloop()