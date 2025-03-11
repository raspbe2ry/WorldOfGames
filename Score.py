from Utils import SCORES_FILE_NAME

def add_score(difficulty):
    points = (difficulty * 3) + 5
    try:
        with open(SCORES_FILE_NAME, 'r+') as file:
            content = file.read()
            score = int(content)
            new_score = score + points
            file.seek(0)
            file.truncate(0)
            file.write(str(new_score))
    except Exception as e:
        print(e)
        with open(SCORES_FILE_NAME, '+') as file:
            file.write(str(points))
