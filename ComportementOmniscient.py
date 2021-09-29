from Robot import Robot
from Environnement import EnvironmentGrid


class ComportementOmniscient:
    
    def __init__(self):
        self.agent = Robot()
        self.environment = EnvironmentGrid() #soit ici soit on le met en entrée
        self.lPD = self.environment.getListPD()
    
    def update_lPD(self):
        self.lPD = self.environment.getListPD()
    
    def NextPD(self):
        self.update_lPD()
        minDist = self.environment.x_dimension*self.environment.y_dimension # Au moins on sait que c'est plus grand que le max
        nextPD = []
        for i in range(0, len(self.lPD)):
            distTemp = ComportementOmniscient.distanceManhattan([self.agent.x,self.agent.y], self.lPD[i][:2])
            if(distTemp <= minDist):
                minDist = distTemp
                nextPD = self.lPD[i]
        return nextPD
    def distanceManhattan(pos1, pos2):
        return abs(pos1[0]-pos2[0]) + abs(pos1[1]-pos2[1])



    def direction(self, nextPD):
        if(self.agent.x > nextPD[0]): #Choix arbitraire de se déplacer d'abor en hauteur puis en largeur
            return "BAS"
        elif (self.agent.x < nextPD[0]):
            return "HAUT"
        else:
            if (self.agent.y > nextPD[1]):
                return "GAUCHE"
            elif(self.agent.y < nextPD[1]):
                return "DROITE"
            else:
                return None


    def run(self):
        nextPD = self.NextPD()
        while (nextPD != []):
            nextDir = self.direction(nextPD)
            if ( nextDir != None):
                self.agent.seDeplacer(nextDir)
            else:
                print(nextPD) #TEST
                if nextPD[2] == 1: #Poussière
                    self.agent.aspirer()
                    self.environment.remove_element(nextPD[0],nextPD[1])
                elif nextPD[2] == 2: #Diamant
                    self.agent.ramasser()
                    self.environment.remove_element(nextPD[0],nextPD[1])
                else: # Les 2
                    self.agent.ramasser()
                    self.agent.aspirer()
                    self.environment.remove_element(nextPD[0],nextPD[1])
            nextPD = self.NextPD()
            print(self.agent.x,self.agent.y)
            self.environment.display_grid()

####
test = ComportementOmniscient()
test.run()