import time
from exercise import *
from playsound import playsound


class Time_exercise(Exercise):

    set_time = 0

    def __init__(self):

        super().__init__()
        pass

    def  __init__(self, name, worked_muscles, movement_type, rest_time, sets, set_time):
    
        self.set_time = set_time
        self.sets = sets
        super().__init__(name, worked_muscles, movement_type, rest_time, sets)


    def train(self):
        for set_ in range(self.sets - 1):
            print('#' + str(set_+1), ' série\n')

            print('TREINE!\n')
            playsound('sfx/go.mp3')
            time.sleep(self.set_time)

            print('Descanse por', self.rest_time, ' segundos.\n')
            time.sleep(self.rest_time)
        
        print('ÚLTIMA SÉRIE. DÊ TODO SEU GÁS.\n')
        time.sleep(self.set_time)

prancha = Time_exercise('prancha', ['core'], 'isometrico', 5, 3, 10)
prancha.train()
