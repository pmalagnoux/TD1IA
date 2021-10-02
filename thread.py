import threading
import time
from ComportementBlind import ComportementBlind
from ComportementOmniscient import ComportementOmniscient
from Robot import Robot
from Environnement import EnvironmentGrid
import numpy as np


class threadEnvironement (threading.Thread):
    def __init__(self, threadID, name, objetEnvironment, objetRobot, timer):
        threading.Thread.__init__(self)
        self.threadID = threadID
        self.name = name
        self.timer = timer
        self.objetEnvironement = objetEnvironment
        self.objetRobot = objetRobot

    def run(self):
        print("Starting " + self.name)
        self.objetEnvironement.lancerEnvironmnent(self.objetRobot, self.timer)


class threadRobot (threading.Thread):
    def __init__(self, threadID, name, objetEnvironment, objetRobot, timer,
                 choix):
        threading.Thread.__init__(self)
        self.threadID = threadID
        self.name = name
        self.timer = timer
        if choix == "1":
            self.comportement = ComportementBlind(objetEnvironment, objetRobot)
        else:
            self.comportement = ComportementOmniscient(
                objetEnvironment, objetRobot)

    def run(self):
        print("Starting " + self.name)
        self.comportement.run(self.timer)  


def executer(timer=np.inf):

    threads = []

    # Create new threads

    choix = input(
        "Choissiez le mode du robot:\n\t0: Omniscient\n\t1: Blind \n")
    objetEnvironement = EnvironmentGrid()
    objetRobot = Robot()
    threadeEnv = threadEnvironement(
        1, "Thread-Evironement", objetEnvironement, objetRobot, timer)
    threadRob = threadRobot(
        2, "Thread-robot", objetEnvironement, objetRobot, timer, choix)

    # Start new Threads
    # Strat execute la fonction run() du thread
    threadeEnv.start()
    threadRob.start()

    # Add threads to thread list
    threads.append(threadeEnv)
    threads.append(threadRob)

    # Wait for all threads to complete
    for t in threads:
        t.join()
    print("Exiting Main Thread")