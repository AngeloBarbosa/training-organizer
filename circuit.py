import time

class Circuit(Training):

    reps = 0

    def __init__(self, reps, rest_time):
        self.reps = reps
        self.rest_time = rest_time

    def __init__(self):
        pass

    def train(self):
        for rep in range(self.reps):
            print(str(rep + 1) + '# Série do circuito\n')

            for index in len(self.exercises):
                self.exercises[index].train()

    def add_exercise(self, exercise):
        self.exercises.append(exercise)
