from tkinter import *
 
# Création de la fenêtre principale 
master = Tk() 
master.geometry("400x200")
 

def change():
    #Création d'un frame d'arrière plan vert 
    frm2 = Frame(master, bg='red')
    # Emplacement du frame 
    frm2.place(x=0, y=0, width=400,height=200)
    # Création d'un bouton au sein du frame 
    b2 = Button(frm2, text="un autre",bg='red', fg='white') 
    b2.place(x=10, y=10, width=100,height=30) 


#Création d'un frame d'arrière plan vert 
frm = Frame(master, bg='green')
 
# Emplacement du frame 
frm.place(x=0, y=0, width=400,height=200)
 
# Création d'un bouton au sein du frame 
b = Button(frm, text="un bouton",bg='red', fg='white',command=change()) 
b.place(x=10, y=10, width=100,height=30) 






master.mainloop()