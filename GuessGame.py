from Game import Game
import random

class GuessGame(Game):
    def __init__(self, difficulty):
        Game.__init__(self, difficulty)

    def generate_number(self):
        self.secret_number = random.randint(1, self.difficulty)

    def get_guess_from_user(self):
        selected_number = -1
        while selected_number == -1:
            print(f"Please choose a number between 1 and {self.difficulty}")
            selected_number = int(input())
            if 1 <= selected_number <= self.difficulty:
                return selected_number

    def compare_results(self, selected_number):
        if selected_number == self.secret_number:
            return True
        return False

    def play(self):
        self.generate_number()
        selected_number = self.get_guess_from_user()
        return self.compare_results(selected_number)
