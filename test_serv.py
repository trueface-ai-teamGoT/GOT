
# from flask import Flask, redirect, url_for, render_template
# import os

# app = Flask(__name__)

# from Backend import trueface
# import requests
# import time
# import base64



# @app.route('/', methods=["GET","POST"])
# def index():
     
#     # return  base64.b64encode(open('Testimages/jon.jpg','rb').read()).decode('utf-8')
#     # name, conf =  trueface.apiIdentify(base64.b64encode(open('Testimages/jon.jpg','rb').read()).decode('utf-8'))
#     # return render_template("index.html", data=conf)

#     # if requests['img']:
#         image = requests.form.post('img')
#         try:
#             name = trueface.apiIdentify(base64.b64encode(image.read()).decode('utf-8'))	
#             return render_template("index.html", data=name)
#         except:
#             jsonify({"sorry": "Sorry, no results! Please try again."}, 500)


# if __name__ == '__main__':
#     port = int(os.environ.get('PORT', 5000))
#     app.run(host='0.0.0.0', port=port, debug=True)

