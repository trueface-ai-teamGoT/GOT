import requests
import base64
import json
import os
import time

headers = {
  "x-api-key":"key",
  "Content-Type":"application/json",
}

def createCollection():
    url = "https://api.chui.ai/v1/collection"

    data = {
      "name":"GameOfThronesCharacters",
      "unknowns":False,
    }

    r  = requests.post(url,data=json.dumps(data),headers=headers).json()
    #print(r)
    success = r['success']
    id = r['data']['collection_id']
    if not success:
        raise Exception('Not successful')
    return id

def identifyCharacter(collectionID, image):
    url = "https://api.chui.ai/v1/identify"


    data = {
      "img":image,
      "collection_id":collectionID
    }

    r  = requests.post(url,data=json.dumps(data),headers=headers).json()
    success = r['success']
    #print (r)
    if not success:
        raise Exception('Not successful')
    id = r['data'][0]['key']
    name = r['data'][0]['name']
    confidence = r['data'][0]['confidence']
    return id, name, confidence


def enrollCharacter(Name, collectionId):
    """ Enrolls Character and returns ID
    """

    url = "https://api.chui.ai/v1/enroll"

    data = {"name":Name, "collection_id":collectionId}
    images = []
    for file in os.listdir("Images/" + Name):
        if file.startswith('o'):
            images.append(file) 

    for i,image in enumerate(images[:3]):   
        data["img" + str(i)] = base64.b64encode(open('Images/' + Name + '/' + image,'rb').read()).decode('utf-8')
        print(Name + '/' + image)

    r0  = requests.post(url,data=json.dumps(data),headers=headers)
    r = r0.json()
    #print(r)
    success = r['success']
    if not success:
        raise Exception('Not successful')
    id = r['data']['enrollment_id']
    print('enrolled', Name)
    return id

def saveCollectionId(collection_id):
    with open('collectionid.txt', 'w') as cidfile:
        cidfile.write(collection_id)

def getCollectionId():
    try:
        with open('collectionid.txt', 'r') as cidfile:
            return cidfile.readlines()[0]
    except:
        setupCollectionAndEnroll()
    with open('collectionid.txt', 'r') as cidfile:
            return cidfile.readlines()[0]


def saveCharacterIds(chars):
    with open('characterids.txt', 'w') as charfile:
        for name, id in chars.items():
            charfile.write(name + ':' + id + '\n')

def getCharacterIds():
    chars = {}
    with open('characterids.txt', 'r') as charfile:
        for line in charfile.readlines():
            name, id = line.split(':')
            chars[name] = id
    return chars


def updateCharacter(Name, enrollment_id):
    url = "https://api.chui.ai/v1/enroll"

    images = []
    for file in os.listdir("Images/" + Name):
        if file.startswith('o'):
            images.append(file) 

    for i,image in enumerate(images[3:]):
        time.sleep(1)
        data = {"enrollment_id":enrollment_id}
        data["img" + str(i)] = base64.b64encode(open('Images/' + Name + '/' + image,'rb').read()).decode('utf-8')
        r0  = requests.put(url,data=json.dumps(data),headers=headers)
        #return r0
        r = r0.json()
        print(Name + '/' + image)
        success = r['success']
        if not success:
            raise Exception('Not successful')

    

def training(collection_id):
    url = "https://api.chui.ai/v1/train"


    data = {
      "collection_id": collection_id
    }

    r  = requests.post(url,data=json.dumps(data),headers=headers).json()
    
    #print(r)
    success = r['success']
    if not success:
        raise Exception('Not successful')
    print('trained')


def updateCollection(collection_id, enrollment_id):
      

    url = "https://api.chui.ai/v1/collection"


    data = {
      "enrollment_id":enrollment_id,
      "collection_id": collection_id
    }

    r  = requests.put(url,data=json.dumps(data),headers=headers).json()
    #print(r)
    success = r['success']
    if not success:
        raise Exception('Not successful')
    print('Collection updated')

def setupCollectionAndEnroll():
    collectionId = createCollection()
    print(collectionId)
    saveCollectionId(collectionId)

    #Get all character names
    chars = os.listdir('Images')
    characters = {}
    for name in chars:
        id = enrollCharacter(name, collectionId)
        characters[name] = id
        updateCollection(collectionId, id) 
        #updateCharacter(name, id)

    saveCharacterIds(characters)
    training(collectionId)
    time.sleep(5)

def apiIdentify(imageData):
    collectionId = getCollectionId()
    id, name, confidence = identifyCharacter(collectionId, imageData)
    return name, confidence


def testIdentify():
    collectionId = getCollectionId()
    id, name, confidence = identifyCharacter(collectionId, base64.b64encode(open('Testimages/jon.jpg','rb').read()).decode('utf-8'))
    print (name, confidence) 

