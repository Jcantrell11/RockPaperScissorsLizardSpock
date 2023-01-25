from player import Player

class Human(Player):

    def __init__(self, name):
        super().__init__(name)
        self.choose_gesture()

    def choose_gesture(self):
        validation = True
        while validation:
            print("")
            print('Choose 0 for Rock.')
            print('Choose 1 for Paper.')
            print('Choose 2 for Scissors.')
            print('Choose 3 for Lizard.')
            print('Choose 4 for Spock.')
            print("")
            self.chosen_gesture = input("Enter your choice: ")
            options_list = ['0', '1', '2', '3', '4']
            if self.chosen_gesture in options_list: 
                self.chosen_gesture = int(self.chosen_gesture)
                validation = False
        print("")        
        print(f"{self.name} has picked {self.gesture_list[self.chosen_gesture]}")

    


        