import os

SCORES_FILE_NAME = "Scores.txt"
BAD_RETURN_CODE = 400

def Screen_cleaner():
    if os.name == 'nt':
        os.system('cls')
    # For Linux and macOS
    else:
        os.system('clear')