from Utils import SCORES_FILE_NAME, BAD_RETURN_CODE
from flask import Flask

app = Flask(__name__)

@app.route("/score")
def score_server():
    content = ''
    try:
        with open(SCORES_FILE_NAME, "r") as file:
            content = file.read()
            score = int(content)
            content = '''<html>
                        <head>
                        <title>Scores Game</title>
                        </head>
                        <body>
                        <h1>The score is <div id="score">'''+str(score)+'''</div></h1>
                        </body>
                        </html>'''
    except:
        content = '''<html>
                        <head>
                        <title>Scores Game</title>
                        </head>
                        <body>
                        <body>
                        <h1><div id="score" style="color:red">'''+str(BAD_RETURN_CODE)+'''</div></h1>
                        </body>
                        </html>'''
    return content

app.run(debug=True)