"""
Created on Tue May 4th, 2021.
@author: Ashish Singh

"""

import time
from fork import Fork
from philosopher import Philosopher

# The main executable code.
def diningphilosophers():

    names = ("Plato", "Kant", "Confucius", "Marx", "Nietzsche")

    fork = []
    for i in range(len(names)):
        fork.append(Fork(i))

    dining_list = []
    temp = []

    for number in range(len(fork)):
        temp.append(names[number])
        temp.append(fork[number])
        dining_list.append(temp)
        temp = []

    # Creates the individual philosopher objects.
    p1 = Philosopher(dining_list[0][0], dining_list[1][1], dining_list[0][1])
    p2 = Philosopher(dining_list[1][0], dining_list[2][1], dining_list[1][1])
    p3 = Philosopher(dining_list[2][0], dining_list[3][1], dining_list[2][1])
    p4 = Philosopher(dining_list[3][0], dining_list[4][1], dining_list[3][1])
    p5 = Philosopher(dining_list[4][0], dining_list[0][1], dining_list[4][1])


    # Starts the thread.
    p1.start()
    p2.start()
    p3.start()
    p4.start()
    p5.start()

    time.sleep(10)

    Philosopher.running = False


# Executable code.
if __name__ == "__main__":
    print()
    diningphilosophers()
