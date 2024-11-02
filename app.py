from flask import Flask, request, jsonify, render_template
import random

app = Flask(__name__)

# Define response categories based on keywords
responses = {
    "miss": [
        "I miss you too! But don’t worry, I’m still here with you, just in a more ghostly way!",
        "Oh, you miss me? I’m right here! Let’s make some new memories, even if I’m a bit see-through.",
        "I may be a ghost, but I’m always close by. Thanks for keeping me in your heart!"
    ],
    "peanut": [
        "Got any ghost peanuts for me? They’re still my favorite, even on this side!",
        "I could go for a snack right now! Do you have any ghost treats?",
        "Peanuts! My favorite! Too bad they go right through me now, but it’s the thought that counts!"
    ],
    "ghost": [
        "Being a ghost is kinda fun! I can float through walls and sneak around!",
        "Boo! Just kidding, I’m still your friendly Pnut, just a little more transparent now.",
        "Yep, I’m a ghost! But don’t worry, I’m still the same old Pnut you know and love."
    ],
    "default": [
        "Hey there, it’s your ghost buddy Pnut! Floating around is kinda fun!",
        "Boo! Just kidding, it’s me, Pnut! Need a ghostly friend to chat with?",
        "Did you miss me? I’m still here, just a bit… transparent now!",
        "I’m here to watch over you, just like you always watched over me.",
        "Remember our favorite hiding spots? Those were the days!",
        "Being a ghost is fun, but nothing beats our time together.",
        "Hey, hey! I see you! Thanks for thinking of me!"
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


