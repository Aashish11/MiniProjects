"""
Created on Tue May 4th, 2021.
@author: Ashish Singh

"""

import threading

# Creates an object Fork.
class Fork:
    """
    A fork object is defined for the philosophers to 
    use while they eat. If all philosophers have their
    right or left forks, no one can eat. Only the philosophers
    that have both the right and left fork can eat.

    For other philosophers to eat, one must put down one of 
    their forks that they hold in their hands.
    """

    def __init__(self, val):
        self.val = val
        self.lock = threading.Lock()

    def acquire_fork(self):
        if self.lock.acquire():
            return True
        else:
            return False

    def release_fork(self):
        return self.lock.release()