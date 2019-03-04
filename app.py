import os

from flask import Flask, request, render_template, send_from_directory

from into_model import check_model

__author__ = 'narmada'
google_api_key = <your street view api key>

app = Flask(__name__)

APP_ROOT = os.path.dirname(os.path.abspath(__file__))


@app.route("/")
def index():
    return render_template("search.html")


@app.route("/search", methods=["POST"])
def search():
    search_text = request.form['search_place']
    print('search text: ', search_text)

    check_model(search_text, google_api_key)

    dst = './images'
    fake_imgs = []
    real_imgs = []

    for file in os.listdir(dst):
        if file.startswith(search_text):
            if 'fake' in file:
                fake_imgs.append(file)
            if 'gsv' in file:
                real_imgs.append(file)


    #search_loc = os.path.join(search_text, 'real')
    #generated_loc = os.path.join(search_text, 'fake')

    #real_imgs = os.listdir(os.path.join(search_text, 'real'))
    #fake_imgs = os.listdir(generated_loc)

    return render_template("search.html", image_names=real_imgs, fake_images=fake_imgs, location=search_text)


@app.route('/images/<filename>')
def send_image_real(filename):
    return send_from_directory("./images", filename)


@app.route('/images/<filename>')
def send_image_fake(filename):
    return send_from_directory("./images", filename)


if __name__ == "__main__":
    app.run(port=4555, debug=True)
