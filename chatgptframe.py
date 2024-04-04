import tkinter as tk

def create_grid(frame):
    for i in range(10):
        for j in range(4):
            label = tk.Label(frame, text=f"({i},{j})", borderwidth=1, relief="solid", width=7, height=2)
            label.grid(row=i, column=j, padx=1, pady=1)

root = tk.Tk()
root.title("Deux grilles de 4 par 10")

# Création du premier cadre et de sa grille
frame1 = tk.Frame(root, bd=2, relief="sunken")
frame1.grid(row=0, column=0, padx=5, pady=5)
create_grid(frame1)

# Création du deuxième cadre et de sa grille
frame2 = tk.Frame(root, bd=2, relief="sunken")
frame2.grid(row=0, column=1, padx=5, pady=5)
create_grid(frame2)

root.mainloop()