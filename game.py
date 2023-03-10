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

    
    def play_game(self):
        players_input = input("How many players will be playing, 1 or 2? ")
        if players_input == "1":
            self.game_one()
        else:
            self.game_two()



    def game_one(self):
        self.player_one = Human("Player One")  
        self.player_two = AI("Player Two")
        self.game_play()
        while self.player_one.score <= 1 and self.player_two.score <= 1:
            self.player_one.choose_gesture()
            self.player_two.choose_gesture()
            self.game_play()
        else: 
            self.display_winner()
                


    def game_two(self):     
        self.player_one = Human("Player One")  
        self.player_two = Human("Player Two")
        self.game_play()
        while self.player_one.score <= 1 and self.player_two.score <= 1:
            self.player_one.choose_gesture()
            self.player_two.choose_gesture()
            self.game_play()
        else: 
            self.display_winner()
        


    def display_winner(self):
        if self.player_one.score > self.player_two.score:
            print(f'{self.player_one.name} wins!')
        else:
            print(f'{self.player_two.name} wins!')


    def game_play(self):
        if self.player_one.chosen_gesture == self.player_two.chosen_gesture:
            print("Same option chosen by both players. No points") 

        elif self.player_one.chosen_gesture == 0 and self.player_two.chosen_gesture == 1:
            self.player_two.score += 1
            print(f'{self.player_two.name} wins a point!')
        elif self.player_one.chosen_gesture == 1 and self.player_two.chosen_gesture == 0:
            self.player_one.score += 1
            print(f'{self.player_one.name} wins a point!')  

        elif self.player_one.chosen_gesture == 0 and self.player_two.chosen_gesture == 2:
            self.player_one.score += 1
            print(f'{self.player_one.name} wins a point!')
        elif self.player_one.chosen_gesture == 2 and self.player_two.chosen_gesture == 0:
            self.player_two.score += 1
            print(f'{self.player_two.name} wins a point!')

        elif self.player_one.chosen_gesture == 0 and self.player_two.chosen_gesture == 3:
            self.player_one.score += 1
            print(f'{self.player_one.name} wins a point!')
        elif self.player_one.chosen_gesture == 3 and self.player_two.chosen_gesture == 0:
            self.player_two.score += 1
            print(f'{self.player_two.name} wins a point!')

        elif self.player_one.chosen_gesture == 0 and self.player_two.chosen_gesture == 4:
            self.player_two.score += 1
            print(f'{self.player_two.name} wins a point!')
        elif self.player_one.chosen_gesture == 4 and self.player_two.chosen_gesture == 0:
            self.player_one.score += 1
            print(f'{self.player_one.name} wins a point!')  

        elif self.player_one.chosen_gesture == 1 and self.player_two.chosen_gesture == 2:
            self.player_two.score += 1
            print(f'{self.player_two.name} wins a point!')
        elif self.player_one.chosen_gesture == 2 and self.player_two.chosen_gesture == 1:
            self.player_one.score += 1
            print(f'{self.player_one.name} wins a point!')  

        elif self.player_one.chosen_gesture == 1 and self.player_two.chosen_gesture == 3:
            self.player_two.score += 1
            print(f'{self.player_two.name} wins a point!')
        elif self.player_one.chosen_gesture == 3 and self.player_two.chosen_gesture == 1:
            self.player_one.score += 1
            print(f'{self.player_one.name} wins a point!')

        elif self.player_one.chosen_gesture == 1 and self.player_two.chosen_gesture == 4:
            self.player_one.score += 1
            print(f'{self.player_one.name} wins a point!')
        elif self.player_one.chosen_gesture == 4 and self.player_two.chosen_gesture == 1:
            self.player_two.score += 1
            print(f'{self.player_two.name} wins a point!')

        elif self.player_one.chosen_gesture == 2 and self.player_two.chosen_gesture == 3:
            self.player_one.score += 1
            print(f'{self.player_one.name} wins a point!')
        elif self.player_one.chosen_gesture == 3 and self.player_two.chosen_gesture == 2:
            self.player_two.score += 1
            print(f'{self.player_two.name} wins a point!')

        elif self.player_one.chosen_gesture == 2 and self.player_two.chosen_gesture == 4:
            self.player_two.score += 1
            print(f'{self.player_two.name} wins a point!')
        elif self.player_one.chosen_gesture == 4 and self.player_two.chosen_gesture == 2:
            self.player_one.score += 1
            print(f'{self.player_one.name} wins a point!')

        elif self.player_one.chosen_gesture == 3 and self.player_two.chosen_gesture == 4:
            self.player_one.score += 1
            print(f'{self.player_one.name} wins a point!')
        elif self.player_one.chosen_gesture == 4 and self.player_two.chosen_gesture == 3:
            self.player_two.score += 1
            print(f'{self.player_two.name} wins a point!')






    


