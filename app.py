from flask import Flask, render_template
import random

app = Flask(__name__)

# Predefined story elements
characters = ["a brave knight", "a curious scientist", "a clever thief", "a wandering wizard"]
settings = ["in a haunted forest", "in a futuristic city", "on a distant planet", "in an enchanted castle"]
conflicts = ["facing a fierce dragon", "solving an ancient mystery", "escaping a powerful enemy", "seeking a hidden treasure"]

# Function to generate a random story
def generate_story():
    character = random.choice(characters)
    setting = random.choice(settings)
    conflict = random.choice(conflicts)
    return f"Once upon a time, {character} found themselves {setting}, {conflict}."

@app.route("/")
def home():
    story = generate_story()
    return render_template("index.html", story=story)

if __name__ == "__main__":
    app.run(debug=True)
