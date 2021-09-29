from random import *

class Robot:
    """
    Constructeur de l'agent
    Sa position est determiné aléatoirement
    """
    def __init__(self):
        self.x = randint(0, 4)
        self.y = randint(0, 4)
        self.energie = 0


    """
    Fonction seDeplacer
    Déplace l'agent d'une pièce dans la direction indiqué en paramètre
    Paramètre : HAUT, BAS, GAUCHE, DROITE
    return 1 si l'agent à pu se déplacer correctement
    return 0 si l'agent n'as pas pu se déplacer (hors grille défini entre 0 et 4)
    """
    def seDeplacer(self, direction):
        if(direction=="HAUT"):
            if(self.x==4):
                print("mouvement impossible")
                return 0
            else:
                self.x+=1
                self.energie+=1
                return 1
        elif(direction=="BAS"):
            if(self.x==0):
                print("mouvement impossible")
                return 0
            else:
                self.x-=1
                self.energie+=1
                return 1
        elif(direction=="GAUCHE"):
            if(self.y==0):
                print("mouvement impossible")
                return 0
            else:
                self.y-=1
                self.energie+=1
                return 1
        elif(direction=="DROITE"):
            if(self.y==4):
                print("mouvement impossible")
                return 0
            else:
                self.y+=1
                self.energie+=1
                return 1
        else:
            print("direction inccorecte")
            return 0

    """
    Fonction afficherPosition
    Affiche dans la console la position courrante de l'agent
    return void
    """
    def afficherPosition(self):
        print("position de l'agent : (", self.x, " ; ", self.y, ")")
        print("Energie consomé : ", self.energie)

    """
    Fonction checkPieceCourante
    Vérifie la présence de pousiere et de bijou dans la pièce courante de l'agent
    return int {0 pour vide, 1 pour poussière, 2 pour bijou, 3 pour les deux}
    """
    def checkPieceCourante(self, objetGrille):
        self.energie += 1
        #return objetGrille.getContenuPiece(self.x, self.y) #TODO adapter au nom exacte de la fonction sur la grille
        return objetGrille.get_grid()

    """
    Fonction aspirer
    Retire la poussiere de la pièce de l'agent
    return void
    """
    def aspirer(self, objetGrille):
        self.energie += 1
        #objetGrille.retirerElementPosition(self.x, self.y, 1) #TODO adapter au nom exacte de la fonction sur la grille
        objetGrille.remove_element(self.x, self.y)

    """
    Fonction ramasser
    retire le bijou de la piece de l'agent
    return void
    """
    def ramasser(self, objetGrille):
        self.energie += 1
        #objetGrille.retirerElementPosition(self.x, self.y, 2) #TODO adapter au nom exacte de la fonction sur la grille
        objetGrille.remove_element(self.x, self.y)

    def getX(self):
        return self.x

    def getY(self):
        return self.y
    
    def getEnergie(self):
        return self.energie

"""
TEST
"""
agent = Robot()
agent.afficherPosition()
agent.seDeplacer("GAUCHE")
agent.afficherPosition()
