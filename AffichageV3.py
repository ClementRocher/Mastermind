import tkinter as tk
import customtkinter as ctf
from random import randint


# Dictionnaire pour définir les couleurs suivantes
couleur_suivante_dict = {"green": "yellow", "yellow": "red", "red": "blue","blue": "coral","coral": "purple","purple": "green"}
dictionnaire_couleurs = {0 : "black", 1 : "coral", 2 : "blue", 3 : "yellow", 4 : "red", 5 : "green", 6 : "purple", 7 : "grey", 8 : "white"}
stockage_choix_joueur = {"Premier Coup":(),"Deuxieme Coup":(),"Troisieme Coup":(),"Quatrieme Coup":(),"Cinquieme Coup":(),"Sixieme Coup":()}

###Fonction qui recoit une liste de nombres et qui parcourt le dictionnaire des couleurs pour renvoyer une liste des couleurs correspondantes
def correspondance_chiffres_couleurs(liste_chiffres):
    taille_liste_chiffres = len(liste_chiffres)
    liste_couleurs = list()

    #Boucle qui parcourt la liste
    for i in range(taille_liste_chiffres):
        correspondance=dictionnaire_couleurs.get(liste_chiffres[i])                 #Pour chaque valeur dans la liste, on récupère dans correspondance la valeur associée à la clé entière
        liste_couleurs.append(correspondance)                                       #On rajoute la correspondance dans une liste liste_couleurs
    return liste_couleurs 

###Fonction permettant de générer le choix des 4 couleurs de l'ordinateur
def choisir_aleatoire_ordinateur():         
    liste_choix_aleatoire = list()
    
    #Boucle qui tourne 4 fois
    for i in range(4):
        nombre_random=randint(1,6)                                                  #génération d'un entier aléatoire entre 1 et 6 compris
        liste_choix_aleatoire.append(nombre_random)                                 #ce nombre est stocké dans une liste liste_choix_aleatoire
    liste_choix_aleatoire = correspondance_chiffres_couleurs(liste_choix_aleatoire) #Appel de la fonction pour remplacer les nombres par leur couleur associée
    return liste_choix_aleatoire                                                    #On renvoie liste_choix_aleatoire

###Fonction qui recoit les listes des choix de l'ordinateur et du joueur, les compare et renvoie une liste d'indices en conséquence
def comparaison_joueur_ordinateur(ordinateur,joueur):
    indices=list()
    #Boucle qui tourne 4 fois
    for i in range(4):
        if ordinateur[i] == joueur[i]:                                              #Si le choix du joueur et de l'ordinateur sont identiques et au même indice
            indices.append(0)                                                       #Alors on stocke 0 (Correspond à Noir dans le dictionnaire) dans la liste indices
        elif joueur[i] in ordinateur:                                               #Sinon si le choix du joueur est présent dans la liste de l'ordinateur mais pas à la même position
            indices.append(8)                                                       #Alors on stocke 1 (Correspond à Blanc dans le dictionnaire) dans la liste indices
        else: indices.append(7)                                                     #Sinon on stocke l'indice 7 (Correspond à Vide dans le dictionnaire) dans la liste indices
    return indices                                                                  #On renvoie la liste indices   

###Fonction pour gérer le changement de couleur des boutons
def changement_couleur(b):
    couleur_suivante = couleur_suivante_dict[couleur_actuelle.get()]
    b.config(bg=couleur_suivante)
    couleur_actuelle.set(couleur_suivante)

def gagne(liste_indices):
    taille_liste_indices= len(liste_indices)
    nombre_d_indices_correct=0
    for i in range(taille_liste_indices):
        if liste_indices[i]== "black":
            nombre_d_indices_correct+=1
    if nombre_d_indices_correct==4:
        return(True)
    else: return(False)

# def rejouer():
#     choix_rejouer = input("Appuyez sur R pour rejouer, M pour menu et Q pour quitter : ")
#     if choix_rejouer == "R" or choix_rejouer == "r":
#         play()
#     elif choix_rejouer == "Q" or choix_rejouer == "q":
#         exit()
#     else: print("Le menu n'existe pas")

def envoyer_essai(compteur):

    ###récupérer les couleurs des boutons en cours
    #c'est ici qu'on utilise le dico stockage des valeurs
    essai_joueur = list()                                                       ##On crée une liste vide
    for col in range(4):                                                        ##On itère sur les quatre boutons
        bouton = frame_grille_couleur.grid_slaves(row=compteur,column=col)[0]   ##On récupère les couleurs des boutons de l'essai
        bouton.configure(state="disabled")                                      ##On fige les boutons de l'essai fait
        essai_joueur.append(bouton.cget("bg"))                                  ##On stocke les couleurs dans la liste
   
   
    print(essai_joueur)
    print(choix_ordinateur)


    ###Comparer avec l'ordinateur ce qui nous donne les indices
    liste_indices =comparaison_joueur_ordinateur(choix_ordinateur,essai_joueur)
    liste_indices =correspondance_chiffres_couleurs(liste_indices)
    print(liste_indices)
    is_gagne = gagne(liste_indices)
    if is_gagne:
        print("C'est gagné !")
        texte_regles.delete("1.0",tk.END)
        texte_regles.insert(tk.END,"C'est gagné !!!!")

    ###afficher les indices
    for i in range(4):
        bouton_indice = frame_grille_indices.grid_slaves(row=compteur,column=i)[0]
        bouton_indice.config(bg=liste_indices[i])

    var.set(1)
    #print(row,col)


def quitter():
    exit()

# Création de la fenêtre principale
root = tk.Tk()
root.geometry("1200x1000")
root.title("Changement de couleur")

# Choix de l'ordinateur
choix_ordinateur = choisir_aleatoire_ordinateur()

# Variable pour suivre la couleur actuelle
couleur_actuelle = tk.StringVar()
couleur_actuelle.set("red")

#Frame contenant la grille
frame_grille_couleur=tk.Frame(root,bd=2, relief="sunken")
frame_grille_couleur.grid(row=0, column=0, padx=5, pady=5)

frame_grille_indices=tk.Frame(root,bd=2, relief="sunken")
frame_grille_indices.grid(row=0, column=1, padx=5, pady=5)

frame_texte_regles=tk.Frame(root, bd=2, relief="sunken")
frame_texte_regles.grid(row=0, column=2,padx=5,pady=5)

###Creation du texte des règles
texte_regles = tk.Text(frame_texte_regles, height = 50, width = 52)
string_texte_regles = "Pour chaque couleur correcte et placée au bon endroit, l’ordinateur affiche un jeton noir. \nPour chaque couleur correcte mais placée au mauvais endroit, l’ordinateur affiche un jeton blanc.\n Pour une proposition totalement incorrecte, il affiche du gris."
texte_regles.insert(tk.END,string_texte_regles)
texte_regles.grid(row=0, column=0,padx=5,pady=5)


bouton_quitter_jeu = tk.Button(root,text="Quitter", command=quitter)
bouton_quitter_jeu.place(x=800, y=800)

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
    buttonWait = tk.Button(root, text="Essai", command=lambda c=compteur : envoyer_essai(c))
    buttonWait.place(x=900, y=800, anchor="c")
    buttonWait.wait_variable(var)
    compteur+=1

'''
frame_grille_couleur.pack(x=0, y=0)
frame_grille_couleur.pack(x=1, y=0)

'''
#Lance la boucle principale de l'application
root.mainloop()
