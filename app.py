from flask import Flask, render_template, url_for
from random import shuffle
import os

app = Flask(__name__)

@app.route("/")
def index():
    # Get the list of all PNG files in the images directory
    images = [f for f in os.listdir("static\images") if f.endswith(".png")]
    shuffle(images) # randomize the order of images
    return render_template("index.html", image=images[0])

if __name__ == "__main__":
    app.run(debug=True)
