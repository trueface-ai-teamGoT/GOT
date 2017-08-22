from flask import Flask, redirect, url_for, render_template, request
import os


app = Flask(__name__)

from Backend import trueface
import requests
import time
import base64



@app.route('/', methods=['POST', 'GET'])
def index():
    return render_template("index.html")


@app.route('/heros', methods=['POST', 'GET'])
def heros():
        image = request.files['img']
        to_send_image = base64.b64encode(image.read()).decode('utf-8')
        name, conf = trueface.apiIdentify(to_send_image)   
        try:
            return render_template("heros.html", data=(name, conf))
        except Exception as e:
            # print e
            # return redirect("http://gameofthrones.wikia.com/wiki/Game_of_Thrones_Wiki", code=302)
            return redirect(url_for('error'))

@app.errorhandler(Exception)
@app.route('/error')
def error(e):
    return render_template("error.html")

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)

