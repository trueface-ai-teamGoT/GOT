
from flask import Flask, redirect, url_for, render_template, request
import os


app = Flask(__name__)

from Backend import trueface
import requests
import time
import base64



@app.route('/', methods=['POST', 'GET'])
def index():
     
    # return  base64.b64encode(open('Testimages/jon.jpg','rb').read()).decode('utf-8')
    # name, conf =  base64.b64encode(open('Testimages/jon.jpg','rb').read()).decode('utf-8')

    if request.method == "POST":
        # image = request.form.post('img')
        image = request.files.to_dict()['no_pen.jpg']
        print request.files.to_dict()['no_pen.jpg']
        print 'after the try'
        name, conf = trueface.apiIdentify(base64.b64encode(image.read()).decode('utf-8'))	
        try:
            print 'try'
            return render_template("index.html", data=(name, conf))
        except Exception,e:
            print e
            # jsonify({"sorry": "Sorry, no results! Please try again."}, 500)
            # print ("error")
            return 'error'
    if request.method == "GET":
        return 'get request'

    return 'another thing'

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port, debug=True)

