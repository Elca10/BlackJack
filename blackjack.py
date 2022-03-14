class Card():
    def __init__(self, rank:str, suit:str, value:int, ct):
        self.rank = rank
        self.suit = suit
        self.value = value
        self.cardType = ct
        textSuits = ['♠','♦','♥','♣']
        textRanks = ['2','3','4','5','6','7','8','9','10','J','Q','K','A']
        uniSuits = ['D', 'F', 'B', 'A']
        uniRanks = ['2','3','4','5','6','7','8','9','A','B','D','E','1']
        textSuits = ['♠','♦','♥','♣']
        textRanks = ['2','3','4','5','6','7','8','9','10','J','Q','K','A']
        suits = ['Clubs', 'Diamonds', 'Hearts', 'Spades']
        ranks = ['Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine', 'Ten', 'Jack', 'Queen', 'King', 'Ace']
        
        if self.cardType == 1:
            self.cardFront = f'{self.rank.title()} of {self.suit.title()}'
        elif self.cardType == 2:
            self.cardFront = f'{textRanks[ranks.index(self.rank.title())]}{textSuits[suits.index(self.suit.title())]}'
        else:
           pic = f"\n _______ \n|{f'{textRanks[ranks.index(self.rank.title())]}':<7}|\n|       |\n|   {textSuits[suits.index(self.suit.title())]}   |\n|       |\n|{f'{textRanks[ranks.index(self.rank.title())]}':>7}|\n ‾‾‾‾‾‾‾ \n"
           self.cardFront =  pic
            


    def __str__(self):
        uniSuits = ['D', 'F', 'B', 'A']
        uniRanks = ['2','3','4','5','6','7','8','9','A','B','D','E','1']
        textSuits = ['♠','♦','♥','♣']
        textRanks = ['2','3','4','5','6','7','8','9','10','J','Q','K','A']
        suits = ['Clubs', 'Diamonds', 'Hearts', 'Spades']
        ranks = ['Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine', 'Ten', 'Jack', 'Queen', 'King', 'Ace']
        if self.cardType == 1:
            return f'{self.rank.title()} of {self.suit.title()}'
        elif self.cardType == 2:
            return f'{textRanks[ranks.index(self.rank.title())]}{textSuits[suits.index(self.suit.title())]}'
        else:           
            pic = f"\n _______ \n|{f'{textRanks[ranks.index(self.rank.title())]}':<7}|\n|       |\n|   {textSuits[suits.index(self.suit.title())]}   |\n|       |\n|{f'{textRanks[ranks.index(self.rank.title())]}':>7}|\n ‾‾‾‾‾‾‾ \n"
            return pic
            
    
    def __repr__(self):
        uniSuits = ['D', 'F', 'B', 'A']
        uniRanks = ['2','3','4','5','6','7','8','9','A','B','D','E','1']
        textSuits = ['♠','♦','♥','♣']
        textRanks = ['2','3','4','5','6','7','8','9','10','J','Q','K','A']
        suits = ['Clubs', 'Diamonds', 'Hearts', 'Spades']
        ranks = ['Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine', 'Ten', 'Jack', 'Queen', 'King', 'Ace']
        if self.cardType == 1:
            return f'{self.rank.title()} of {self.suit.title()} (value of {self.value})'
        elif self.cardType == 2:
            return f'{textRanks[ranks.index(self.rank.title())]}{textSuits[suits.index(self.suit.title())]}'
        elif self.cardType == 3:
            pic = f"\n _______ \n|{f'{textRanks[ranks.index(self.rank.title())]}':<7}|\n|       |\n|   {textSuits[suits.index(self.suit.title())]}   |\n|       |\n|{f'{textRanks[ranks.index(self.rank.title())]}':>7}|\n ‾‾‾‾‾‾‾ \n"
            return pic

          
          
class Deck():
    def __init__(self, ranks, suits, values, cType):
        cards = []
        
        
        for rank in ranks:
            value = values[ranks.index(rank)]
            for suit in suits:
                cards.append(Card(rank, suit, value, cType))
                
                
        self.cards = cards
    
    def shuffle(self):
        import random as r
        r.shuffle(self.cards)
        
   
    def get_top_card(self):
        return self.cards.pop(0)
      
      
      
      
      
class Hand():
    '''Class that stores the cards a player is holding'''
    def __init__(self, *cards):
        self.cards = list(cards)
        
    def get_tally(self):
        tally = 0
        for card in self.cards:
            tally += card.value
        return tally
    
    
    def add_card(self, card):
        self.cards.append(card)
    
    def __str__(self):
        
        to_print = []
        if self.cards[0].cardType == 3:
            splitCards = [card.cardFront.split('\n') for card in self.cards]
            for i in range(8):
                for card in splitCards:
                    to_print.append(card[i] + '  ')
                to_print.append('\n')
            return ''.join(to_print)

        
        return str(self.cards)

class Blackjack:
        def card_type(self):
            ''' asks the user how they would like to view cards (three visual options)'''
            print("___________________CARD DISPLAY OPTIONS___________________\n")
            print("1:     Ten of clubs")
            print("2:     10♠")
            print(f"3:     A larger version of \U0001F0BA")
            import time as t
            t.sleep(1)
            choice = int(input("Which card type would you like to use?"))
            return choice
        
        
        def deal(self, hand, deck, tally):
            '''deals a single card and returns the new tally of all that player/'s cards'''
            card = deck.get_top_card()
            hand.add_card(card)
            return hand.get_tally()
        
        
        def ace_value(self, hand, card, tally):
            # the default value for an ace is 11
            print(f"You drew an ace. Your hand can be either {tally-10} or {tally} points.")
            
            choice = int(input("Would you like it to have a value of 1 or 11?"))
            while choice != 1 and choice != 11:
                choice = int(input("Please enter either 1 or 11: "))
            card.value = choice
            tally = (tally - 11) + choice
            return tally

                
        def check_bust(self, tally):
            '''returns True or False based on whether the tally is greater than 21'''
            if tally > 21:
                return True
            return False
        
        
        def check_blackjack(self, tally):
            '''returns True or False based on whether the tally is equal to 21'''
            if tally == 21:
                return True
            return False
            
            
        #player method
        def player_turn(self, hand, deck, player_sum):
            '''Continues to ask the user if they want to choose a new card (and then chooses a card)
            until the player busts or chooses to stop receiving more cards. It then returns the player_sum.'''
            print("----------YOUR TURN----------")
            import time as t
            hit = True
            no_bust = self.check_bust(player_sum)
            no_bjack = self.check_blackjack(player_sum)
            
            # draws cards until the player doesn't want to or can't
            while hit and no_bust == False and no_bjack == False:
                print(f'Your hand: {hand}')
                print(f'Your card total: {player_sum}')
                choice = input("Would you like another card? (Y/N)").lower().strip()
                # accounts for several possible inputs
                t.sleep(1)
                if choice in ['yes', 'y', 'ya', 'yea', 'yeah', 'yep', 'yes please', 'of course', 'hell yeah', 'hit', 'hit me']: 
                    # adds card to hand and checks for bust
                    player_sum = self.deal(hand, deck, player_sum)
                    print(f'You were dealt a {hand.cards[-1]}')
                    if hand.cards[-1].rank == 'Ace':
                        player_sum = self.ace_value(hand, card, player_sum)
                    no_bust = self.check_bust(player_sum)
                    no_bjack = self.check_blackjack(player_sum)
                    
                elif choice in ['no', 'n', 'nope', 'nah', 'no thanks', 'absolutely not', 'hell no', 'of course not','stand']:
                    # exits loop
                    hit = False
                else:
                    # in case of invalid response
                    choice = input("Not a valid response. Would you like another card? (Y/N)").lower().strip()
                    
            # extra print statements for special cases (bust and blackjack)
            if no_bust:
                print(f'BUST! Your total ({player_sum}) is over 21')
            if no_bjack:
                print(f'BLACKJACK! Your sum is exactly 21.')
            return player_sum
            
        
        #computer method
        def computer_turn(self, hand, deck, comp_sum):
            print("----------DEALER'S TURN----------")
            '''Continues to choose a new card
            until the computer busts or the comp_sum becomes 17 or higher. It then returns the comp_sum.'''
            bust = self.check_bust(comp_sum)
            # draws cards until it can't (bust or count over 16)
            while comp_sum < 17 and bust == False:
                comp_sum = self.deal(hand, deck, comp_sum)
                print(f'The dealer was dealt a {hand.cards[-1]}')
            print(f"The dealer's sum is {comp_sum}.\n")
            return comp_sum
        
        
        def find_winner(self, player_sum, comp_sum):
            '''Returns the winner of the game.'''
            comp_bust = self.check_bust(comp_sum)
            # this function only runs if the player hasn't busted (automatic loss in that case)
            
            # automatic win for dealer if player busts
            if self.check_bust(player_sum):
                return 'Dealer'
            # automatic win for player if dealer busts
            elif comp_bust:
                return 'You'
            # otherwise it's whoever had the larger (thus closer to 21) sum
            elif player_sum < comp_sum:
                return 'Dealer'
            elif comp_sum < player_sum:
                return 'You'
            elif player_sum == comp_sum:
                return 'Tie!'
            # the code below should never run, if all goes well
            return f'UNKNOWN (P: {player_sum}, C: {comp_sum})'
        
        
        def play_again(self):
            '''Asks if the user would like to play again'''
            choice = input("Play again? (Y/N)").lower()
            if choice in ['yes', 'y', 'ya', 'yea', 'yeah', 'yep', 'yes please', 'of course', 'hell yeah',"why not"]:
                return True
            else:
                return False
        
        
        def start_screen(self):
            '''prints ASCII intro splash screen'''
            s000 = ' ' + '_'*58 + ' '
            s00 = '|' +' '*58 + '|'
            s0 = "|                  Welcome to the game of                  |"
            s1 = '|              _           _              _                |'
            s2 = '|      \      |_) |   /\  /  |/   |  /\  /  |/      /      |'
            s3 = '|      /      |_) |_ /--\ \_ |\ \_| /--\ \_ |\      \      |'
            s4 = '|' +'_'*58 + '|'
            
            ss = [s000,s00,s0,s1,s2,s3,s4,'\n','\n']
            for s in ss:
                print(s)
        
        
        def game_rules(self):
            '''Displays overview of game rules for 30 seconds '''
            import time as t
            from IPython.display import clear_output
            clear_output()
            for i in sorted([j+1 for j in range(30)], reverse=True):
                print("_______________________GAME RULES OVERVIEW_______________________\n")
                print("OBJECTIVE: Get a hand with a count (obtained by adding the values of the cards) of 21 without going over 21.")
                print("SETUP: Two cards are dealt face up to each player and the dealer. From there, on a player's turn, a player can decide to take another card.")
                print("SCORING: Whoever had a count closest to 21 wins.")
                print('\n For more detailed rules you can watch this video: https://www.youtube.com/watch?v=0-XIjDr33Mo')
                print("You can also read the rules online here: https://bicyclecards.com/how-to-play/blackjack/")

                print(f"\n\nClosing in {i}", end = "")
                t.sleep(1)
                clear_output()
            print('\n\n')
            
            clear_output()
            
            
        def intro(self):
            # Asks if user knows how to play
            rules = input("Do you know how to play? (Y/N)").lower().strip()
            # if new to the game, loads game rules page
            if rules not in ['yes', 'y', 'ya', 'yea', 'yeah', 'yep', 'yes please', 'of course', 'hell yeah']:
                self.game_rules()
            
            # sets card type based on player's choice
            cType = self.card_type()
            print('\n\n')
            
            
            # Extras just for fun 
            print("Let's get started!\n")
            import time as t
            for i in '.....Setting table up.....':
                print(i, end="")
                t.sleep(0.1)
            print('\n\n')
            t.sleep(2)
            
            # Clears screen
            from IPython.display import clear_output
            clear_output()
            
            
            return cType

            
        def save_results(self, data):
            '''Saves (writes) user's game results to a file'''
            from datetime import date as d
            
            with open(f'BLACKJACK_{d.today()}.txt', 'a') as f:
                for info in data:
                    f.write(info + '\n')

                    
            
        def end_screen(self, wins, losses, ties, streaks,balance, gain, loss):
            ''' Displays game results with an option to save them. Then shows closing splash screen. '''
            import time as t
            from IPython.display import clear_output
            print("_______________________RESULTS_______________________\n")
            print("GAME DATA:")
            print(f'Rounds played: {sum([wins, losses, ties])}')
            print(f'Wins: {wins}\nLosses: {losses}\nTies: {ties}')
            print(f'Win percentage: {((wins)/(sum([wins, losses, ties])))*100}%')
            print(f'Longest streak: {max(streaks)}')
            print(f'\n\nBETTING DATA:')
            print(f'Starting balance: {(balance + loss)-gain}')
            print(f'Final balance: {balance}')
            print(f'Total $$$ gains: {gain}')
            print(f'Total $$$ loss: {loss}')
            print('\n\n')
            
            save = input("Would you like to save your results? (Y/N)").lower().strip()
            if save in ['yes', 'y', 'ya', 'yea', 'yeah', 'yep', 'yes please', 'of course', 'hell yeah']:
                data = ['_______________________',f'ROUNDS PLAYED: {sum([wins, losses, ties])}', f'WINS: {wins}', f'LOSSES: {losses}', f'TIES: {ties}', f'WIN PERCENTAGE: {((wins)/(sum([wins, losses, ties])))*100}%', f'LONGEST STREAK: {max(streaks)}',f'STARTING BALANCE: {(balance + loss)-gain}', f'FINAL BALANCE: {balance}', f'TOTAL $ GAINS: {gain}', f'TOTAL $ LOSS: {loss}','_______________________']
                self.save_results(data)

            
            t.sleep(5)
            # CODE BELOW IS BASED OFF OF SOME OF MATT'S CODE FROM A PREVIOUS UNIT
            close =  "           Thank you for playing!            "
            close2 = "            See you next time!               "
            for j in range(50):
                for i in range(len(close)+1):
                    print(f"{close[:i]:>50}")
                    print(f"{close2[:i]:>50}")
                    clear_output(wait = True)
                    t.sleep(.11)


        def main(self):
            from IPython.display import clear_output
            import time as t
            # Game intro
            self.start_screen()
            cType = self.intro()
            
            # var setup
            again = True
            rounds = 0
            wins = 0
            losses = 0
            ties = 0
            streak = 0
            streaks = []
            balance = int(input("How much money do you have to bet? (Starting balance in dollars)"))
            while balance == 0:
                balance = int(input("You must have at least 1 dollar to play. Please enter your starting balance: "))
            gain = 0
            loss = 0
            # while the player wants to continue playing
            while again:
                # create a runner class
                game = Blackjack()
                
                # new round
                rounds += 1
                print(f"_______________________ROUND {rounds}_______________________")
                
                # DECK SETUP
                ranks = ['Two','Three','Four','Five','Six','Seven','Eight','Nine','Ten','Jack','Queen','King','Ace']
                suits = ['Clubs', 'Diamonds', 'Hearts', 'Spades']
                values = [2,3,4,5,6,7,8,9,10,10,10,10,11]
                # create a deck object 
                deck = Deck(ranks, suits, values, cType)
                # shuffle the deck
                deck.shuffle()

                # PLAYER/DEALER SETUP
                # initialize a player_sum and comp_sum to zero
                player_sum = 0
                comp_sum = 0
                # initialize player and comp hands
                player_hand = Hand()
                comp_hand = Hand()
                             

                # START GAME
                # betting
                print(f"Your balance: {balance}")
                
                # stops playing if player runs out of money
                if balance == 0:
                    print("You're broke! Hate to break it to ya, but that means the game's over.")
                    again = False
                    break
                bet = int(input("How much would you like to bet?"))
                while bet > balance:
                    bet = int(input("You can't bet more than you have. How much would you like to bet?"))
                if bet == balance:
                    print('Going all in! Well, you only live once after all!\n\n')
                balance -= bet
               
                
                # deal the first four cards (alternating player/comp/player/comp)
                for i in range(4):
                    if i % 2 == 0:
                        comp_sum = self.deal(comp_hand, deck, comp_sum)
                    else:
                        player_sum = self.deal(player_hand, deck, player_sum)
                
                print(f"DEALER'S STARTING HAND: {comp_hand}\n\n")

                # checks for ace in player's hand (aces dealt to dealer are defaulted to 11)
                for card in player_hand.cards:
                    if card.rank == 'Ace':
                        player_sum = self.ace_value(player_hand, card, player_sum)
                
                # PLAYER'S TURN
                # let the player take their turn (meaning they can choose more cards until they choose to stop or bust)
                player_sum = self.player_turn(player_hand, deck, player_sum)
                print()
                print("YOUR TOTAL:", player_sum)
                print("DEALER'S TOTAL:", comp_sum)
                print()
                
                
                # COMPUTER'S TURN
                comp_sum = self.computer_turn(comp_hand, deck, comp_sum)

                # FINDING WINNER
                # also adds game data 
                winner = self.find_winner(player_sum, comp_sum)
                if winner == "You":
                    print(f'{winner.title()} win!')
                    wins += 1
                    streak += 1
                    balance += bet*2 # gains money
                    gain += bet
                elif winner == 'Tie!':
                    print('Tie!')
                    ties += 1
                    streak += 1
                    balance += bet # doesn't lose money
                else: # if winner == 'Dealer'
                    print(f'{winner.title()} wins!')
                    losses += 1
                    streaks.append(streak)
                    if streak != 0:
                        print(f'**Streak of {streak} broken!**')
                    streak = 0
                    # balance doesn't change (bet already subtracted)
                    loss += bet
                    
                print(f"Your $$$: {balance}")
                    
                # PLAYING AGAIN AND/OR QUITTING AND/OR QUITTING
                import time as t
                t.sleep(2)
                again = self.play_again()
                
                t.sleep(2)
                clear_output()
                
                if balance == 0:
                    print("You're broke! Hate to break it to ya, but that means the game's over.")
                    again = False
            # ENDING THE GAME
            streaks.append(streak)
            
            self.end_screen(wins, losses, ties,streaks, balance, gain, loss)
    
# run the main program
if __name__ == '__main__':
    Blackjack().main()
