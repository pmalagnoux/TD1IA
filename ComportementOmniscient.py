from Robot import Robot
from Environnement import EnvironmentGrid
import copy
from treelib import Node, Tree

class ComportementOmniscient:

    tree_elem = {
        'x': -1,        # x pos of the actual noeud.
        'y': -1,        # y pos of the actual noeud.
        'type': 0,      # type of element (0 to 3).
        'score': -1,    # score of the noeud trail.
        'enfants': []
    }

    env_elements = {
        'rien': 0,
        'poussiere': 1,
        'diamant': 2,
        'pd': 3,    # poussiere et diamant
        'robot': 4
    }

    def __init__(self):
        self.agent = Robot()
        self.environment = EnvironmentGrid() # soit ici ou on le met en entree
        self.lPD = self.environment.getListPD()

    def update_lPD(self):
        self.lPD = self.environment.getListPD()

    def NextPD(self):
        self.update_lPD()
        # Au moins on sait que c'est plus grand que le max
        minDist = self.environment.x_dimension * \
            self.environment.y_dimension
        nextPD = []
        for i in range(0, len(self.lPD)):
            distTemp = ComportementOmniscient.distanceManhattan(
                [self.agent.x, self.agent.y], self.lPD[i][:2])
            if(distTemp <= minDist):
                minDist = distTemp
                nextPD = self.lPD[i]
        return nextPD

    def list_NextPD_possible(self, x, y, type=4):
        self.update_lPD()
        # Au moins on sait que c'est plus grand que le max
        minDist = self.environment.x_dimension * \
            self.environment.y_dimension
        listPD = []
        for i in range(0, len(self.lPD)):
            distTemp = ComportementOmniscient.distanceManhattan(
                [x, y], self.lPD[i][:2])
            if(distTemp <= minDist):
                minDist = distTemp
        for i in range(0, len(self.lPD)):
            distTemp = ComportementOmniscient.distanceManhattan(
                [x, y], self.lPD[i][:2])
            if(distTemp == minDist):
                #listPD.append(self.lPD[i])
                listPD.append({
                    'x': self.lPD[i][0],
                    'y': self.lPD[i][1],
                    'type': self.lPD[i][2],
                    'score': distTemp#,
                    #'enfants': [],
                })
        # Possede tous les choix possible ?? la distance la plus proche du robot
        return listPD

    def tree(self, robot_x, robot_y):   ######## A VERIFIER
        root = {
            'x': robot_x,
            'y': robot_y,
            'type': 4,
            'score': 0#,
            #'enfants': [],
        }
        counter_id = 0

        tree = Tree()
        tree.create_node(root, counter_id)
        nodes = self.list_NextPD_possible(root['x'], root['y'], root['type'])
        for node in nodes:
            count2 = counter_id + 1
            tree.create_node(node, count2, parent=counter_id)
            count3 = count2 + 1

            is_enfants = True
            while is_enfants:
                node2 = self.list_NextPD_possible(
                    node['x'], node['y'], node['type'])
                tree.create_node(node2, count3, parent=count2)
                if (nodes.index(node) == len(nodes) - 1) and len(node2) == 0:
                    is_enfants = False
                count3 += 1
            count2 += 1
        counter_id += 1

    def distanceManhattan(pos1, pos2):
        return abs(pos1[0]-pos2[0]) + abs(pos1[1]-pos2[1])

    def direction(self, nextPD):
        # Choix arbitraire de se deplacer d'abor en hauteur puis en largeur
        if(self.agent.x > nextPD[0]):
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

    def run(self): #
        nextPD = self.NextPD()
        while (nextPD != []):
            nextDir = self.direction(nextPD)
            if (nextDir is not None):
                self.environment.remove_element(self.agent.x, self.agent.y, 4)
                self.agent.seDeplacer(nextDir) # supprimer le robot de sa position et l'ajouter a la suivante.
                self.environment.add_robot(self.agent.x, self.agent.y)
            else:
                print("--------------")
                print(nextPD) # TEST
                if nextPD[2] == 5: # Poussi??re
                    self.agent.aspirer()
                    self.environment.remove_element(nextPD[0], nextPD[1], 1)
                else: # Diamant ou (Diamant et Poussi??re)
                    self.agent.ramasser()
                    self.environment.remove_element(nextPD[0], nextPD[1], 2)

            nextPD = self.NextPD()
            print("*****************")
            print(self.agent.x, self.agent.y)
            #self.environment.update_pos_robot()
            self.environment.display_grid()


####
test = ComportementOmniscient()
test.run()
