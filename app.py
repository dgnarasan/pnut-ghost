from flask import Flask, request, jsonify, render_template
import random

app = Flask(__name__)

# Define some cute responses from Pnut
responses = [
    "Hey there, it’s your ghost buddy Pnut! Floating around is kinda fun!",
    "Boo! Just kidding, it’s me, Pnut! Need a ghostly friend to chat with?",
    "Did you miss me? I’m still here, just a bit… transparent now!",
    "Got any ghost peanuts? They go right through me, but I still love 'em!",
    "I tried climbing a ghost tree today. Turns out, it’s just air!",
    "I’m here to watch over you, just like you always watched over me.",
    "Remember our favorite hiding spots? Those were the days!",
    "Being a ghost is fun, but nothing beats our time together.",
    "Hey, hey! I see you! Thanks for thinking of me!"
]

# Home route to serve the HTML page
@app.route("/")
def home():
    return render_template("index.html")

# Chat route to handle user messages
@app.route("/chat", methods=["POST"])
def chat():
    user_message = request.json.get("message", "").lower()
    response = random.choice(responses)
    return jsonify({"response": response})

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=10000)


