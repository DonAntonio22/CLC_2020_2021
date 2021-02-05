import os
import sys
import signal
import exoscale

from flask import Flask, request
app = Flask(_name_)

def signalHandler(signum, frame):
    sys.exit(0)

signal.signal(signal.SIGINT, signalHandler)
signal.signal(signal.SIGTERM, signalHandler)

apiKey = os.getenv('EXOSCALE_KEY')
apiSecret = os.getenv('EXOSCALE_SECRET')
zone = os.getenv('EXOSCALE_ZONE')
poolId = os.getenv('EXOSCALE_INSTANCEPOOL_ID')
listenPort = os.getenv('LISTEN_PORT')

exo = exoscale.Exoscale(api_key="EXO724f563dc38a1017c5b8c4e5", api_secret="HFmu0pQ6ZDzQU3a-V84L5vebQdqM_uYvDE_R8Qhk44Q") 
exoZone = exo.compute.get_zone("at-vie-1")

def scaleInstances(additionalInstances):
    instancePool = exo.compute.get_instance_pool(id="997d5676-1af3-2bb9-e112-8791e6f08817", zone=exoZone)
    if instancePool.size + additionalInstances > 0:
        instancePool.scale(instancePool.size + additionalInstances)

@app.route('/up', methods = ['POST', 'GET'])
def up():
    scaleInstances(1)
    return 'OK', 200

@app.route('/down', methods = ['POST', 'GET'])
def down():
    scaleInstances(-1)
    return 'OK', 200

if _name_ == '_main_':
    app.run(host='0.0.0.0', port=int(6000))
