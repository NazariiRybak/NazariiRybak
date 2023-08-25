from flask import Flask, render_template
import random

app = Flask(__name__)

# list of cat images
images = [
    "https://images.saymedia-content.com/.image/c_limit%2Ccs_srgb%2Cq_auto:eco%2Cw_760/MTk2NzY3MjA5ODc0MjY5ODI2/top-10-cutest-cat-photos-of-all-time.webp",
    "https://i.pinimg.com/736x/54/f7/48/54f74884dca10f350ce2e445a5c454c8.jpg"
]

@app.route('/')
def index():
    url = random.choice(images)
    return render_template('index.html', url=url)

if __name__ == "__main__":
    app.run(host="0.0.0.0")
