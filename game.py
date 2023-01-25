from ai import AI
from human import Human 

class Game:
    def __init__(self):
        self.player_one = ""
        self.player_two = ""

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
        print("")

    def game_one(self):
        self.player_one = Human("Player One")  
        self.player_two = AI("Player Two")
        


    def game_two(self):
        self.player_one = Human("Player One")  
        self.player_two = Human("Player Two")
        
 

    def play_game(self):
        players_input = input("How many players will be playing, 1 or 2? ")
        if players_input == "1":
            self.game_one()
        else:
            self.game_two()







    


