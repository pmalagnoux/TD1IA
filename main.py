### Imports ###
from ComportementBlind import ComportementBlind
from ComportementBlindGraphique import ComportementBlindGraphique
from ComportementOmniscientGraphique import ComportementOmniscientGraphique
from Robot import Robot
from Environnement import EnvironmentGrid
import thread

choixFonctionnemnt = bool(input("Choissiez le mode :\n\t0: Affichage graphique (pour visualiser le comportement)\n\t1: Thread (vrai comportement avec les trheads d'environnement et de robot distict) \n"))

if choixFonctionnemnt: # Si Affichage Graphique
    choix = bool(input("Choissiez le mode du robot:\n\t0: Omniscient\n\t1: Blind \n"))
    if choix:
        script = ComportementBlindGraphique()
        script.run()
    else:
        script = ComportementOmniscientGraphique()
        script.run()
else:
    thread.executer()
