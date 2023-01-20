from player import Player

class Human(Player):

    def __init__(self, name):
        super().__init__()
        self.name = name 
        self.score = 0

    #   def choose_gesture(self):
    #     self.chosen_gesture = str(input.randint(0,4))
    #     gesture_list = ["Rock", "Paper", "Scissors", "Lizard", "Spock"]
    #     print(f"{self.name} has picked {gesture_list[int(self.chosen_gesture)]}")


        