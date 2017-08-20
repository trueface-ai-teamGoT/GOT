from Backend import trueface
import time
import base64

name, conf = trueface.apiIdentify(base64.b64encode(open('Testimages/jon.jpg','rb').read()).decode('utf-8'))
print(name, conf)
#time.sleep(10)
#trueface.testIdentify()