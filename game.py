from ai import AI
from human import Human 

class Game:
    def __init__(self):
        self.ai = AI('ai')
        self.human = Human 

    def run_game(self):
        self.display_rules()
        self.play_game()

    def display_rules(self):
        print('Welcome to Rock Paper Scissors Lizard Spock. As seen on the Big Bang Theory!')
        print("")
        print('Each match will be a best of three games')
        print('Use the number keys to enter your selction when prompted')
        print("")
        print('Here are the rules:')
        print('Scissors cut Paper')
        print('Paper covers Rock')
        print('Rock crushes Lizard')
        print('Lizard poisons Spock')
        print('Spock smashes Scissors')
        print('Scissors decapitates Lizard')
        print('Lizard eats Paper')
        print('Paper disproves Spock')
        print('Spock vaporizes Rock')
        print('Rock crushes Scissors')
        players = input("How many players will be playing, 1 or 2? ")

    def play_game(self):
       self.ai.choose_gesture()


