#Creates a planet
import random
import json
from path import cwd

class planet:
    def __init__(self,predecided=None):
        self.color=None
        self.moons=None
        self.size=None
        self.shape=None
        self.conditions=None
        