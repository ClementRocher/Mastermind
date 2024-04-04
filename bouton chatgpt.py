import tkinter as tk

def change_color():
    button.config(bg="blue")  # Changer la couleur de fond en bleu

# Création de la fenêtre
root = tk.Tk()
root.geometry("200x100")

# Création du bouton
button = tk.Button(root, text="Changer la couleur", command=change_color)
button.pack(pady=20)

root.mainloop()
