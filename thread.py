import threading
import time
from ComportementBlind import ComportementBlind
from ComportementOmniscient import ComportementOmniscient
from Robot import Robot
from Environnement import EnvironmentGrid


class threadEnvironement (threading.Thread):
    def __init__(self, threadID, name, objetEnvironment, objetRobot, timer):
        threading.Thread.__init__(self)
        self.threadID = threadID
        self.name = name
        self.timer = timer
    def run(self):
        print ("Starting " + self.name)
        # Get lock to synchronize threads
        # threadLock.acquire()
        objetEnvironement.lancerEnvironmnent(objetRobot,self.timer) #TODO Fonction a faire
        time.sleep(1)
        # Free lock to release next thread
        # threadLock.release()

class threadRobot (threading.Thread):
    def __init__(self, threadID, name, objetEnvironment, objetRobot,timer, choix):
        threading.Thread.__init__(self)
        self.threadID = threadID
        self.name = name
        self.timer = timer
        if choix:
            self.comportement = ComportementBlind(objetEnvironment,objetRobot)
        else:
            self.comportement = ComportementOmniscient(objetEnvironment,objetRobot)
        
    def run(self):
        print ("Starting " + self.name)
        # Get lock to synchronize threads
        # threadLock.acquire()
        self.comportement.run(timer)  #TODO Fonction a faire
        time.sleep(1)
        # Free lock to release next thread
        # threadLock.release()



#Exemple d'execution

def executer():
    # threadLock = threading.Lock()
    threads = []

    # Create new threads
    timer = 10
    choix = bool(input("Choissiez le mode du robot:\n\t0: Omniscient\n\t1: Blind \n"))
    objetEnvironement = EnvironmentGrid()
    objetRobot = Robot()
    threadeEnv = threadEnvironement(1, "Thread-Evironement", objetEnvironement, objetRobot, timer)
    threadRob = threadRobot(2, "Thread-robot", objetEnvironement, objetRobot, timer, choix)

    # thread1 = myThread(1, "Thread-1", 1)
    # thread2 = myThread(2, "Thread-2", 2)

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
    print ("Exiting Main Thread")