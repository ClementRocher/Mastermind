from random import randint

dictionnaire_couleurs = {0 : "Noir", 1 : "Blanc", 2 : "Bleu", 3 : "Jaune", 4 : "Rouge", 5 : "Vert", 6 : "Violet", 7 : "Vide", 8 : "Corail"}
stockage_choix_joueur = {"Premier Coup":(),"Deuxieme Coup":(),"Troisieme Coup":(),"Quatrieme Coup":(),"Cinquieme Coup":(),"Sixieme Coup":()}

###Fonction permettant de générer le choix des 4 couleurs de l'ordinateur
def choisir_aleatoire_ordinateur():         
    liste_choix_aleatoire = list()
    
    #Boucle qui tourne 4 fois
    for i in range(4):
        nombre_random=randint(1,6)                                                  #génération d'un entier aléatoire entre 1 et 6 compris
        liste_choix_aleatoire.append(nombre_random)                                 #ce nombre est stocké dans une liste liste_choix_aleatoire
    liste_choix_aleatoire = correspondance_chiffres_couleurs(liste_choix_aleatoire) #Appel de la fonction pour remplacer les nombres par leur couleur associée
    return liste_choix_aleatoire                                                    #On renvoie liste_choix_aleatoire


###Fonction permettant de faire choisir 4 couleurs au joueur
def choix_du_joueur():
    essai_joueur = list()  

    #Boucle qui tourne 4 fois
    for i in range(4):
        #On stocke l'input entré par le joueur dans une variable essai
        essai = int(input("Choisissez une couleur. 1 : Corail | 2 : Bleu | 3 : Jaune | 4 : Rouge | 5 : Vert | 6 : Violet :  "))
        essai_joueur.append(essai)                                                   #On stocke cet input dans une liste essai_joueur
    essai_joueur = correspondance_chiffres_couleurs(essai_joueur)                    #Appel de la fonction pour remplacer les nombres par leur couleur associée
    return essai_joueur                                                              #Retour de la liste essai_joueur

###Fonction qui recoit une liste de nombres et qui parcourt le dictionnaire des couleurs pour renvoyer une liste des couleurs correspondantes
def correspondance_chiffres_couleurs(liste_chiffres):
    taille_liste_chiffres = len(liste_chiffres)
    liste_couleurs = list()

    #Boucle qui parcourt la liste
    for i in range(taille_liste_chiffres):
        correspondance=dictionnaire_couleurs.get(liste_chiffres[i])                 #Pour chaque valeur dans la liste, on récupère dans correspondance la valeur associée à la clé entière
        liste_couleurs.append(correspondance)                                       #On rajoute la correspondance dans une liste liste_couleurs
    return liste_couleurs                                                           #On renvoie la liste liste_couleurs

###Fonction qui recoit les listes des choix de l'ordinateur et du joueur, les compare et renvoie une liste d'indices en conséquence
def comparaison_joueur_ordinateur(ordinateur,joueur):
    indices=list()
    #Boucle qui tourne 4 fois
    for i in range(4):
        if ordinateur[i] == joueur[i]:                                              #Si le choix du joueur et de l'ordinateur sont identiques et au même indice
            indices.append(0)                                                       #Alors on stocke 0 (Correspond à Noir dans le dictionnaire) dans la liste indices
        elif joueur[i] in ordinateur:                                               #Sinon si le choix du joueur est présent dans la liste de l'ordinateur mais pas à la même position
            indices.append(1)                                                       #Alors on stocke 1 (Correspond à Blanc dans le dictionnaire) dans la liste indices
        else: indices.append(7)                                                     #Sinon on stocke l'indice 7 (Correspond à Vide dans le dictionnaire) dans la liste indices
    return indices                                                                  #On renvoie la liste indices   

#Fonction temporaire permettant l'affichage console des indices
def affichage_console_indices(liste_indices):
    for i in range(len(liste_indices)):
        if liste_indices[i] == 'Noir':
            print(f"Votre tentative pour la case {i+1} est bonne")
        elif liste_indices[i] == 'Blanc':
            print(f"Cette couleur est bonne, mais elle ne se situe pas en case {i+1}")
        else: print(f"Votre proposition de couleur pour la case {i+1} est fausse, la couleur n'est pas dans les choix de l'ordinateur")

#
def gagne(liste_indices):
    taille_liste_indices= len(liste_indices)
    nombre_d_indices_correct=0
    for i in range(taille_liste_indices):
        if liste_indices[i]== "Noir":
            nombre_d_indices_correct+=1
    if nombre_d_indices_correct==4:
        return(True)
    else: return(False)

def rejouer():
    choix_rejouer = input("Appuyez sur R pour rejouer, M pour menu et Q pour quitter : ")
    if choix_rejouer == "R" or choix_rejouer == "r":
        play()
    elif choix_rejouer == "Q" or choix_rejouer == "q":
        exit()
    else: print("Le menu n'existe pas")


def play():

    #appel choix de l'ordinateur
    choix_de_l_ordinateur = choisir_aleatoire_ordinateur()
    print(f"L'ordinateur a choisi les couleurs {choix_de_l_ordinateur}")

    #Compteur de tour
    compteur=1

    while compteur<4:
        #choix du joueur
        print(f"Vous êtes au tour {compteur}")
        essai_joueur = choix_du_joueur()
        print(f"vous avez choisi les couleurs {essai_joueur}")

        #Comparaison des deux choix pour avoir une liste d'indices
        liste_indices =comparaison_joueur_ordinateur(choix_de_l_ordinateur,essai_joueur)
        liste_indices =correspondance_chiffres_couleurs(liste_indices)
        print(liste_indices)
        is_gagne = gagne(liste_indices)
        if is_gagne:
            print("C'est gagné !")
            rejouer()
            break
        
        affichage_console_indices(liste_indices)

        compteur+=1
    print("C'est perdu !")
    rejouer()

    
play()





