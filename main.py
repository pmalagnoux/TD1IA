### Imports ###
from threading import Timer
from ComportementBlind import ComportementBlind
from ComportementBlindGraphique import ComportementBlindGraphique
from ComportementOmniscientGraphique import ComportementOmniscientGraphique
from Robot import Robot
from Environnement import EnvironmentGrid
import thread

choixFonctionnemnt = input("Choissiez le mode :\n\t0: Affichage graphique (pour visualiser le comportement)\n\t1: Thread (vrai comportement avec les trheads d'environnement et de robot distict) \n")
print(choixFonctionnemnt)
if choixFonctionnemnt == "0": # Si Affichage Graphique
    choix = input("Choissiez le mode du robot:\n\t0: Omniscient\n\t1: Blind \n")
    if choix == "1":
        script = ComportementBlindGraphique()
    else:
        script = ComportementOmniscientGraphique()
    script.run()
else:
    timer = int(input("Veuillez saisir le temps (en s) d'éxécution du Thread :"))
    thread.executer(timer)
