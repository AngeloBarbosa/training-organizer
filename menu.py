from abc import ABC
import training

class Menu(ABC):

    quit = False

    def menu(self):
        while not quit:
            print('O que desejas fazer?')
            print('1 - Treinar')

