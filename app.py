from flask import Flask, request, jsonify, session, render_template
import random

app = Flask(__name__)
app.secret_key = "920-380-714"  # needed for session storage , enter your key

# Serve the HTML page
@app.route("/")
def index():
    return render_template("page.html")

# Start game
@app.route("/start", methods=["POST"])
def start_game():
    session["number"] = random.randint(1, 100)
    session["attempts"] = 0
    return jsonify({"message": "Game started! Guess a number between 1 and 100 and only 10 attempts."})

# Guess route
@app.route("/guess", methods=["POST"])
def guess():
    data = request.get_json()
    try:
        user_guess = int(data["guess"])
    except (ValueError, TypeError):
        return jsonify({"result": "❌ Please enter a valid number.", "attempts": session.get("attempts", 0)})

    number = session.get("number")
    if number is None:
        return jsonify({"result": "⚠️ Game not started yet!"})

    # Track attempts
    attempts = session.get("attempts", 0) + 1
    session["attempts"] = attempts

    # Validate range
    if not (1 <= user_guess <= 100):
        return jsonify({"result": "❌ Invalid guess! Enter a number between 1 and 100.", "attempts": attempts})

    # Compare guess
    if user_guess < number:
        result = "Too low!"
    elif user_guess > number:
        result = "Too high!"
    else:
        result = f"🎉 Correct! The number was {number}. Attempts: {attempts}"
        return jsonify({"result": result, "attempts": attempts})

    # 🔥 If max attempts reached → game over, reveal number
    if attempts >= 10:
        result = f"❌ Game Over! The number was {number}."
        return jsonify({"result": result, "attempts": attempts, "game_over": True})

    return jsonify({"result": result, "attempts": attempts})

if __name__ == "__main__":
    app.run(debug=True)
