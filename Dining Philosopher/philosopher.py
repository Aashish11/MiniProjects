"""
Created on Tue May 4th, 2021.
@author: Ashish Singh

"""

import random
import threading
import time

from fork import Fork

# Creates an object Philosopher
class Philosopher(threading.Thread):
    """
    This object defines the names of the philosophers and the 
    type of activity they perform such as think, eat, and 
    clean up.
    """
    running = True

    def __init__(self, name: str, left_fork: Fork, right_fork: Fork):
        threading.Thread.__init__(self)
        self.name = name
        self.left_fork = left_fork
        self.right_fork = right_fork
        

    def run(self):
        while self.running:
            self.think()
            self.eat()
            print(f"{self.name} is cleaning up.")

    def think(self):
        thinking = random.uniform(3, 5)
        print(f"{self.name} is thinking for {thinking} seconds.")
        time.sleep(thinking)
        print(f"{self.name} is now hungry.")


    def eat(self):
        if self.left_fork.acquire_fork():
            if self.right_fork.acquire_fork():
                eating = random.uniform(3, 5)
                print(f"{self.name} is eating for {eating} seconds.")
                time.sleep(eating)

                self.left_fork.release_fork()
                print(f"{self.name} has put down his left fork.")
                self.right_fork.release_fork()
                print(f"{self.name} has put down his right fork.")
            
            else:
                return
