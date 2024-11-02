from flask import Flask, request, jsonify, render_template
import random

app = Flask(__name__)

# Define response categories based on keywords
responses = {
    "miss": [
        "I miss you too! Floating around here isn’t the same without you.",
        "Oh, you miss me? I’m right here! Let’s make some new ghostly memories together.",
        "I’m always here, just a bit… transparent now! But I still remember all our fun times."
    ],
    "peanut": [
        "Peanuts! My favorite snack! Got any ghost peanuts for me?",
        "Even as a ghost, I can't say no to peanuts! Thanks for offering.",
        "I would love a peanut… even if it goes right through me now!"
    ],
    "ghost": [
        "Boo! Just kidding, it’s just me, friendly ghost Pnut!",
        "Being a ghost is kinda fun. I can float through walls!",
        "Yep, I’m a ghost! But don’t worry, I’m still the same old Pnut you know and love."
    ],
    "default": [
        "Hey there, it’s your ghost buddy Pnut! I’m always around.",
        "Boo! Just kidding, it’s me, Pnut! Need a ghostly friend to chat with?",
        "Did you miss me? I’m still here, floating around and watching over you.",
        "I’m here to watch over you, just like you always watched over me. Thanks for thinking of me!",
        "I tried climbing a ghost tree today. Turns out it’s just air, but it’s still fun to try!",
        "Hey, hey! I see you! It feels good to chat with you again."
    ]
}


def get_response(user_message):
    # Convert message to lowercase to match keywords
    user_message = user_message.lower()

    # Check for keywords and return a random response from the matching category
    if "miss" in user_message:
        return random.choice(responses["miss"])
    elif "peanut" in user_message or "food" in user_message or "snack" in user_message:
        return random.choice(responses["peanut"])
    elif "ghost" in user_message:
        return random.choice(responses["ghost"])
    else:
        return random.choice(responses["default"])

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/chat", methods=["POST"])
def chat():
    user_message = request.json.get("message", "")
    response = get_response(user_message)
    return jsonify({"response": response})

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=10000)


