import cv2
import os
import time
import requests
import base64
import json
#directories = ["./WillBodansky/","./ShaunMoore/","./EtienneBaudry/"]
directories = ["./Images_hackathon/"]#"./actors/"]

requests.adapters.DEFAULT_RETRIES = 5
#ahBzfmNodWlzcGRldGVjdG9ychcLEgpDb2xsZWN0aW9uGICAgID398kJDA MEN
#ahBzfmNodWlzcGRldGVjdG9ychcLEgpDb2xsZWN0aW9uGICAgMDg68AKDA WOMEN

def enrollAndAddToCollection():
	for x in directories:
		i = directories.index(x)
		enrollment_id = ""
		counterActor=0
		for y in os.listdir(x):
			print y
			counter = 0
			if y != '.DS_Store':
			  for z in os.listdir(x+y):
					#img2 = cv2.imread(x+y+'/'+z)
					url = "https://api.chui.ai/v1/enroll"
					#url = "http://localhost:39081/api/enroll"
					headers = {
					  "x-api-key":"X49IlMBNk28ldayruPrXo6GRTFpdccW7k8SYVwrd",
					  "Content-Type":"application/json",
					}
					print x+y+'/'+z
					if counter ==0 and z != '.DS_Store':
						data = {
						  "img0":base64.b64encode(open(x+y+'/'+z,'rb').read()),
						  "name":y
						}
						r  = requests.post(url,data=json.dumps(data),headers=headers)
						print r.json()
						if r.json()['data'] != 'no face detected':
							enrollment_id = r.json()['data']['enrollment_id']
							url = "https://api.chui.ai/v1/collection"
							#url = "http://localhost:39081/api/collection"
							print enrollment_id

							data = {
							  "enrollment_id":r.json()['data']['enrollment_id'],
							  "collection_id":"ahBzfmNodWlzcGRldGVjdG9ychcLEgpDb2xsZWN0aW9uGICAgKDGk70KDA",
							  #"unknowns":True
							}

							r  = requests.put(url,data=json.dumps(data),headers=headers)

							#print r.content
						counter += 1					
					elif enrollment_id != "":
						print enrollment_id
						url = "https://api.chui.ai/v1/collection"
						#url = "http://localhost:39081/api/enroll"

						data = {
						  "enrollment_id":enrollment_id,
						  "img0":base64.b64encode(open(x+y+'/'+z,'rb').read()),
						  "collection_id":"ahBzfmNodWlzcGRldGVjdG9ychcLEgpDb2xsZWN0aW9uGICAgKDGk70KDA",

						}

						r  = requests.put(url,data=json.dumps(data),headers=headers)

						print r.content

enrollAndAddToCollection()