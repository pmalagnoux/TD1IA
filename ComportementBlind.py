
import time
from Robot import Robot
from Environnement import EnvironmentGrid
import numpy as np
import random

class ComportementBlind:


    def __init__(self, environment, robot):
        self.agent = robot
        self.environment = environment
        self.environment.add_robot(self.agent.x,self.agent.y)
        self.gridPoids = np.zeros((self.environment.x_dimension, self.environment.y_dimension))
        self.gridPoids[self.agent.x, self.agent.y] += 1

    def detecter(self): #Fonction du capteur du robot A déplacer dans le Robot
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
        pass
    def run(self, timer):
        t1 = time.time()
        while(time.time()-t1 < timer):
         #condition à définir
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
            print()
            print("************************")
            print("*****Environnement******")
            print()
            print(self.environment.env_grid)
            print()
            print("*********Poids**********")
            print()
            print(self.gridPoids)
            time.sleep(1)

####TEST#####

#test = ComportementBlind()
#test.run()

