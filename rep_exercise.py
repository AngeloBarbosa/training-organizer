import time
from training_organizer.exercise import *
from playsound import playsound

class Rep_exercise(Exercise):

    reps = 0
    rep_time = 0

    def __init__(self):
        
        super().__init__()
        pass

    def __init__(self, name, worked_muscles, movement_type, rest_time, sets, reps, rep_time):
        
        self.reps = reps
        self.rep_time = rep_time
        super().__init__(name, worked_muscles, movement_type, rest_time, sets)

    

    def train(self):
        print('O exercício começará em 10 segundos. Prepare-se.')
        time.sleep(10)

        for set_ in range(self.sets):

            if set_ != self.sets - 1:
                print('\n#' + str(set_ + 1), 'série\n')
            else:
                print('ÚLTIMA SÉRIE. DÊ TODO SEU GÁS.\n')

            for rep in range(self.reps):

                print(rep)
                time.sleep(self.rep_time)

            print(self.reps)

            if set_ == self.sets - 1:
                break

            print('\nDescanse por', self.rest_time, 'segundos. \n')
            time.sleep(self.rest_time)

        print('')

