from player import Player
import random 

class AI(Player):

    def __init__(self, name):
        super().__init__(name)
        self.choose_gesture()

    def choose_gesture(self):
        self.chosen_gesture = random.randint(0,4)
        print(f"{self.name} has picked {self.gesture_list[self.chosen_gesture]}")
        


