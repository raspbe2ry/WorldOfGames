from Game import Game
from MemoryGame import MemoryGame
from GuessGame import GuessGame
from CurrencyRouletteGame import CurrencyRouletteGame
from Score import add_score

def welcome(name):
    welcome_message = f"""Hello {name} and welcome to the World of Games (WoG)."
                          Here you can find many cool games to play."""
    return welcome_message

def load_game():
    game = -1
    while game == -1:
        print("""Please choose a game to play:
                1. Memory Game - a sequence of numbers will appear for 1 second and you have to
                guess it back
                2. Guess Game - guess a number and see if you chose like the computer
                3. Currency Roulette - try and guess the value of a random amount of USD in ILS""")
        game_number = int(input())
        if 1 <= game_number <= 3:
            game = game_number


    level = -1
    while level == -1:
        print("Please choose game difficulty from 1 to 5:")
        level_number = int(input())
        if 1 <= level_number <= 5:
            level = level_number

    selected_game = None
    try:
        if game == 1:
            selected_game = MemoryGame(level)
        elif game == 2:
            selected_game = GuessGame(level)
        elif game == 3:
            selected_game = CurrencyRouletteGame(level)

        if selected_game.play():
            print("Congrats, you won")
            add_score(level)
        else:
            print("More lucky next time")
    except:
        print("An error occurred during the game")


