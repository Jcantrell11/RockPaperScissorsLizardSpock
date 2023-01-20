from player import Player

class Human(Player):

    def __init__(self, name):
        super().__init__(name)
        self.name = name 
        self.score = 0

    def choose_gesture(self):
        print('Choose 0 for Rock.')
        print('Choose 1 for Paper.')
        print('Choose 2 for Scissors.')
        print('Choose 3 for Lizard.')
        print('Choose 4 for Spock.')
        self.chosen_gesture = input("Enter your choice: ")
        gesture_list = ["Rock", "Paper", "Scissors", "Lizard", "Spock"]
        print(f"{self.name} has picked {gesture_list[int(self.chosen_gesture)]}")

    


        