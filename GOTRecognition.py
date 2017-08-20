from flask import Flask,requests, redirect, url_for, render_template
import os


app = Flask(__name__)

from Backend import trueface
import time
import base64



@app.route('/', methods=['POST'])
def index():
 
    if request.method == "POST":
 
        image = request

        print request
 
        try:

			name, conf = trueface.apiIdentify(image).read()).decode('utf-8'))	

	    return name, conf
	 
        except:
            jsonify({"sorry": "Sorry, no results! Please try again."}), 500


if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)

