from boggle import Boggle
from flask import Flask, request, render_template, session, jsonify
from flask_debugtoolbar import DebugToolbarExtension

boggle_game = Boggle()

app = Flask (__name__)
app.config['SECRET_KEY'] = "secretttt"
debug = DebugToolbarExtension(app)

@app.route("/")
def show_board():
    # boggle_board = Boggle()
    board = boggle_game.make_board()
    session['board'] = board

    html = render_template("home.html" , board=board)
    return html

@app.route("/check", methods=["POST"])
def check_word():
    """Returns JSON like {result:"ok"} or {result:"not-a-word"}"""

    # word = request.args.get("data")
    word = request.json.get("data")

    board = session['board']

    valid_word = boggle_game.check_valid_word(board, word)
    # import pdb; pdb.set_trace()
    result = jsonify({"result": valid_word})
    return result



