from flask import Flask, request, jsonify, session, render_template
from flask_cors import CORS
import random, os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

app = Flask(__name__)
app.secret_key = os.getenv("SECRET_KEY", "dev-secret")  # safer than hardcoding
CORS(app)

@app.route('/')
def index():
    return render_template('page.html')

@app.route('/start', methods=['POST'])
def start_game():
    session['number'] = random.randint(1, 100)
    session['attempts'] = 0
    return jsonify({"message": "Game started! Guess a number between 1 and 100."})

@app.route('/guess', methods=['POST'])
def guess():
    data = request.get_json()
    guess = int(data['guess'])
    number = session.get('number')
    attempts = session.get('attempts', 0) + 1
    session['attempts'] = attempts

    if guess < number:
        result = "Too low!"
    elif guess > number:
        result = "Too high!"
    else:
        result = f"Correct! The number was {number}. Attempts: {attempts}"

    # Game over if 10 attempts used or number guessed
    game_over = attempts >= 10 or guess == number
    if game_over and guess != number:
        result = f"Game Over! The number was {number}."

    return jsonify({"result": result, "attempts": attempts, "game_over": game_over})

if __name__ == '__main__':
    app.run(debug=True)
