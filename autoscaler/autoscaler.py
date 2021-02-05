import exoscale
import signal
import os
import sys
import logging as log

from flask import Flask
from flask import jsonify
app = Flask(__name__)

poolID = os.environ.get('INSTANCE_POOL_ID')
listenPort = os.environ.get('LISTEN_PORT')
#key = os.environ.get('EXOSCALE_KEY')
key = 'EXO724f563dc38a1017c5b8c4e5'
#secret = os.environ.get('EXOSCALE_SECRET')
secret = 'HFmu0pQ6ZDzQU3a-V84L5vebQdqM_uYvDE_R8Qhk44Q'
#zone = os.environ.get('EXOSCALE_ZONE')
zone = 'at-vie-1'
#zoneID = os.environ.get('EXOSCALE_ZONE_ID')
zoneID = '4da1b188-dcd6-4ff5-b7fd-bde984055548'
exo = exoscale.Exoscale(api_key=key, api_secret=secret)
#exoscaleKeyAndSecret = exo.Exoscale(api_key=key, api_secret=secret) 
exoZone = exo.compute.get_zone('at-vie-1')

signal.signal(signal.SIGINT, sys.exit(0))
signal.signal(signal.SIGTERM, sys.exit(0))

@app.route('/up', methods = ['POST', 'GET'])
def up():
    log.info(changeNumOfInstances(True))
    #return 'OK', 200
    data = {'message' : 'OK'}
    return data, 200

@app.route('/down', methods = ['POST', 'GET'])
def down():
    log.info(changeNumOfInstances(False))
    #return 'OK', 200
    data = {'message' : 'OK'}
    return data, 200

def changeNumOfInstances(flag):
    addOrSubstr = 0
    if flag == True:
        addOrSubstr = 1
    elif flag == False:
        addOrSubstr = -1
    instancePool = exo.compute.get_instance_pool(id="997d5676-1af3-2bb9-e112-8791e6f08817", zone=exoZone)

    if instancePool.size + addOrSubstr > 0:
        instancePool.scale(instancePool.size + addOrSubstr)
    else:
        log.info("Reached Minimum!!")
    
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=int(6000))