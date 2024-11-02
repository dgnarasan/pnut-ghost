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
    "how are you": [
        "Floating around happily! Being a ghost isn’t so bad!",
        "I’m doing great! Just floating in the afterlife, keeping an eye on you.",
        "I’m at peace and watching over you. How about you?"
    ],
    "where are you": [
        "I’m right here! Just a bit harder to see. Think of me as your invisible buddy.",
        "I’m floating nearby, keeping an eye on things.",
        "I’m here in spirit, always close to you!"
    ],
    "love": [
        "Aww, I love you too! Ghost hugs from me to you!",
        "Love you lots! I may be invisible, but my love isn’t.",
        "Love never fades, even for ghosts!"
    ],
    "joke": [
        "Why don’t ghosts like rain? Because it dampens their spirits! 😆",
        "What’s a ghost’s favorite fruit? Boo-berries! 😂",
        "Why did the ghost go to the party? Because he heard it was a real scream! 👻"
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
    user_message = user_message.lower()

    # Check for keywords and return a random response from the matching category
    if "miss" in user_message:
        return random.choice(responses["miss"])
    elif "peanut" in user_message or "food" in user_message or "snack" in user_message:
        return random.choice(responses["peanut"])
    elif "ghost" in user_message:
        return random.choice(responses["ghost"])
    elif "how are you" in user_message:
        return random.choice(responses["how are you"])
    elif "where are you" in user_message:
        return random.choice(responses["where are you"])
    elif "love" in user_message:
        return random.choice(responses["love"])
    elif "joke" in user_message:
        return random.choice(responses["joke"])
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


