import requests
import base64
import json
import io

headers = {
  "x-api-key":"lFxBTdfFslAFtFKzPohk53q9ZJhp3nD9tr3VfSv9 ",
  "Content-Type":"application/json",
}

def createCollection():
    url = "https://api.chui.ai/v1/collection"

    data = {
      "name":"GameOfThronesCharacters",
      "unknowns":False,
    }

    r  = requests.post(url,data=json.dumps(data),headers=headers).json()
    success = r['success']
    id = r['data']['collection_id']
    if not success:
        raise Exception('Not successful')
    return id

def identifyCharacter(collectionID, image):
    url = "https://api.chui.ai/v1/identify"


    data = {
      "img":base64.b64encode(image),
      "collection_id":collectionID
    }

    r  = requests.post(url,data=json.dumps(data),headers=headers).json()
    success = r['success']


def enrollCharacter():
    """ Enrolls Character and returns ID
    """

    url = "https://api.chui.ai/v1/enroll"

    data = {
    "img0":base64.b64encode(open('/image/o1.jpg','rb').read()),
    "img1":base64.b64encode(open('/image/o2.jpg','rb').read()),
    "img2":base64.b64encode(open('/image/o3.jpg','rb').read()),
    "name":"John Snow"
    }

    r  = requests.post(url,data=json.dumps(data),headers=headers)

    return r.json()

def startTraining():
    pass

def getImages():
    pass
