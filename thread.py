import threading
import time
from Robot import Robot
from Environnement import EnvironmentGrid


class threadEnvironement (threading.Thread):
    def __init__(self, threadID, name, objetEnvironment, objetRobot):
        threading.Thread.__init__(self)
        self.threadID = threadID
        self.name = name
    def run(self):
        print ("Starting " + self.name)
        # Get lock to synchronize threads
        # threadLock.acquire()
        objetEnvironement.lancerEnvironment(objetRobot) #TODO Fonction a faire
        time.sleep(1)
        # Free lock to release next thread
        # threadLock.release()

class threadRobot (threading.Thread):
    def __init__(self, threadID, name, objetEnvironment, objetRobot):
        threading.Thread.__init__(self)
        self.threadID = threadID
        self.name = name
    def run(self,objetEnvironment):
        print ("Starting " + self.name)
        # Get lock to synchronize threads
        # threadLock.acquire()
        objetRobot.lancerRobot(objetEnvironment)  #TODO Fonction a faire
        time.sleep(1)
        # Free lock to release next thread
        # threadLock.release()



#Exemple d'execution


# threadLock = threading.Lock()
threads = []

# Create new threads
objetEnvironement = EnvironmentGrid()
objetRobot = Robot()
threadeEnv = threadEnvironement(1, "Thread-Evironement", objetEnvironement, objetRobot)
threadRob = threadRobot(2, "Thread-robot", objetEnvironement, objetRobot)

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