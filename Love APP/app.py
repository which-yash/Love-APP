import os
from flask import Flask, render_template, request
import random

app = Flask(__name__, static_folder="static", template_folder="templates")

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/love", methods=["POST"])
def love():
    name1 = request.form.get("name1", "").strip()
    name2 = request.form.get("name2", "").strip()
    if not name1 or not name2:
        return render_template("index.html", error="Please enter both names 💕")
    score = random.randint(75, 100)
    message = "Perfect match made in heaven ✨" if score > 90 else "Strong bond, unbreakable 💕"
    return render_template("love_result.html", name1=name1, name2=name2, score=score, message=message)

@app.route("/date")
def date():
    return render_template("date.html")

@app.route("/date/sub/<choice>")
def date_sub(choice):
    return render_template("date_sub.html", choice=choice)

@app.route("/date/result/<choice>/<sub>")
def date_result(choice, sub):
    msgs = {
        "icecream": {
            "chocolate": "Sweet choice, just like you 😘",
            "vanilla": "Simple but perfect, just like us 💕",
            "strawberry": "Berry sweet, just like our love ❤️"
        },
        "movie": {
            "romantic": "A cozy romantic movie night with you sounds perfect 😍",
            "comedy": "Laughing with you is the best thing ever 💕",
            "horror": "I’d protect you when you get scared 😉"
        },
        "stars": {
            "stargaze": "Under the stars, I’d only see you ✨❤️",
            "wish": "My wish is always you 💫",
            "hands": "Best feeling in the world 💕"
        }
    }
    msg = msgs.get(choice, {}).get(sub, "You chose love — best choice ever 💖")
    return render_template("date_result.html", msg=msg)

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port, debug=True)
