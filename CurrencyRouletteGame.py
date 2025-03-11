from Game import Game
import requests
import random

class CurrencyRouletteGame(Game):
    def __init__(self, difficulty):
        Game.__init__(self, difficulty)

    def get_money_interval(self, t):
        response = requests.get('https://api.fastforex.io//fetch-multi?from=USD&to=ILS&api_key=439d2a6d8c-5bbe1530bf-spzw42')
        rate = response.json()["results"]["ILS"]
        return [t * rate - (5 - self.difficulty), t * rate + (5 - self.difficulty)]

    def get_guess_from_user(self, t):
        print(f"Guess the value of {t} shekels in USD")
        user_input = input()
        float_number = float(user_input)
        return float_number

    def play(self):
        random_value = random.random()
        interval= self.get_money_interval(random_value)
        user_guess = self.get_guess_from_user(random_value)
        if interval[0] <= user_guess <= interval[1]:
            return True
        return False
