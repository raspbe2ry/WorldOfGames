import time
import os

from Game import Game
import random

class MemoryGame(Game):
    def __init__(self, difficulty):
        Game.__init__(self, difficulty)

    def generate_sequence(self):
        generated_numbers = []
        for i in range(self.difficulty):
            generated_numbers.append(random.randint(1, 101))
        return generated_numbers

    def get_list_from_user(self):
        selected_numbers = []
        while len(selected_numbers) < self.difficulty:
            selected_number = -1
            while selected_number == -1:
                print(f"Please choose a number between 1 and 101")
                selected_number = int(input())
                if 1 <= selected_number <= 101:
                    selected_numbers.append(selected_number)
        return selected_numbers

    def is_list_equal(self, generated_numbers, selected_numbers):
        for i in range(self.difficulty):
            if generated_numbers[i] != selected_numbers[i]:
                return False
        return True

    def play(self):
        generated_sequence = self.generate_sequence()
        print(generated_sequence, end="", flush=True)
        time.sleep(0.7)
        print("\r" + " " * 30, end="", flush=True)
        selected_numbers = self.get_list_from_user()
        return self.is_list_equal(generated_sequence, selected_numbers)