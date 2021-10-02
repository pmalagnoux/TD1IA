from Robot import Robot
from Environnement import EnvironmentGrid
import numpy as np
import random
import matplotlib
import matplotlib.pyplot as plt

class ComportementBlindGraphique:
    
    fig, ax = plt.subplots()


    def __init__(self):
        self.agent = Robot()
        self.environment = EnvironmentGrid()
        self.gridPoids = np.zeros((self.environment.x_dimension, self.environment.y_dimension))
        self.gridPoids[self.agent.x, self.agent.y] += 1

    def detecter(self,):
        return self.environment.getElementPos(self.agent.x, self.agent.y)

    def choixDep(self):
        
        choixPossible = self.directionPossible(self.agent.x,self.agent.y)
        minPoids = np.inf
        choixMin = []
        for choix in choixPossible:
            poidsChoix = self.gridPoids[choixPossible[choix][0] + self.agent.x, choixPossible[choix][1] + self.agent.y]
            if  poidsChoix < minPoids:
                minPoids = poidsChoix
                choixMin = [choix]
            elif poidsChoix == minPoids:
                choixMin.append(choix)
        if len(choixMin) == 1:
            return choixMin[0]
        else:
            return choixMin[random.randint(0,len(choixMin)-1)] #Choisi aléatoirement parmi les solution de même poids
        

    def directionPossible(self, x, y):
        pos = np.array([x, y])
        choix = {'HAUT': [1,0],
                'BAS': [-1,0],
                'GAUCHE': [0,-1],
                'DROITE': [0,1] }
        return { possibilite : choix[possibilite] for possibilite in choix  if (choix[possibilite] + pos)[0] >= 0 and (choix[possibilite] + pos)[0] < self.environment.x_dimension and (choix[possibilite] + pos)[1] >= 0 and (choix[possibilite] + pos)[1] < self.environment.y_dimension}

    def affichePoids(self):
        self.ax.imshow(np.zeros((5,5)), extent=[0, self.environment.x_dimension, 0, self.environment.y_dimension])
        plt.cla()
        plt.xticks(np.arange(0, self.environment.x_dimension + 1, 1))
        plt.yticks(np.arange(0, self.environment.y_dimension + 1, 1))
        self.ax.imshow(self.gridPoids, extent=[0, self.environment.x_dimension, 0, self.environment.y_dimension])
        for j in range(self.environment.x_dimension):
            for i in range(self.environment.y_dimension):
                text = self.ax.text(i+0.5, 4-j+0.5, self.gridPoids[j,i], ha="center", va="top", color="w",)
        self.ax.set_title("Poids")
        self.fig.tight_layout()
        plt.pause(0.01)
        
    def run(self):
        
        while (self.agent.energie < 100):
            action = self.detecter()
            if (action == 5): #Poussiere
                self.agent.aspirer()
                self.environment.remove_element(self.agent.x, self.agent.y, 1)
            elif (action == 6 or action == 7):
                self.agent.ramasser()
                self.environment.remove_element(self.agent.x, self.agent.y, 2)
            else : #Robot sur case vide
                nextDir = self.choixDep()
                self.environment.remove_element(self.agent.x, self.agent.y, 4)
                self.agent.seDeplacer(nextDir)
                self.environment.add_robot(self.agent.x, self.agent.y)
                self.gridPoids[self.agent.x, self.agent.y] += 1

            #Ajout de d'element dans l'environnement
            if random.random() < 0.15: # Choix du taux d'aparition à chaque action
                self.environment.add_element(self.agent.x,self.agent.y,random.randint(1,2))

            self.environment.display_grid() #Affichage
            print()
            print("*********Poids**********")
            print()
            print(self.gridPoids)
            self.affichePoids()
            
        print()
        print("###### Conclusion ######")
        print("Energie dépensée : ", self.agent.energie)
        print("Nombre de Poussières aspirées : ", self.agent.nbAspire)
        print("Nombre de Diamants rammassées : ", self.agent.nbRammase)