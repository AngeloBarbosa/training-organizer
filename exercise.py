import time
from abc import ABC, abstractmethod

class Exercise(ABC):

    name = ''
    worked_muscles = []
    movement_type = ''
    rest_time = 0
    sets = 0

    def __init__(self):
        pass

    def __init__(self, name, worked_muscles, movement_type, rest_time, sets):
        self.name = name
        self.worked_muscles = worked_muscles
        self.movement_type = movement_type
        self.rest_time = rest_time
        self.sets = sets
    
    @abstractmethod
    def train(self):
        pass

        
