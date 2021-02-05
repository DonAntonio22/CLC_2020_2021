#Source for first app: https://topherpedersen.blog/2019/12/28/how-to-setup-a-new-flask-app-on-a-mac/
#needed imports and flask-jsonify
import exoscale
import signal
import os
import sys
import logging as log


from flask import Flask, jsonify
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'This is a test'
#End first test


# Exoscale Definitions
poolID = os.environ.get('EXOSCALE_INSTANCEPOOL_ID')
#poolID = "8e444dc6-5a5b-2821-7c15-42ed4d5c9ef1"
listenPort = os.environ.get('LISTEN_PORT')
#listenPort = "6000"
key = os.environ.get('EXOSCALE_KEY')
#key = 'EXO724f563dc38a1017c5b8c4e5'
secret = os.environ.get('EXOSCALE_SECRET')
#secret = 'HFmu0pQ6ZDzQU3a-V84L5vebQdqM_uYvDE_R8Qhk44Q'
zone = os.environ.get('EXOSCALE_ZONE')
#zone = 'at-vie-1'
zoneID = os.environ.get('EXOSCALE_ZONE_ID')
#zoneID = '4da1b188-dcd6-4ff5-b7fd-bde984055548'
exo = exoscale.Exoscale(api_key=key, api_secret=secret)
exoZone = exo.compute.get_zone(zone)


def sig(signum, frame):
    sys.exit(0)
# Kill gracefully
signal.signal(signal.SIGTERM, sig)
signal.signal(signal.SIGINT, sig)

#Source: https://stackoverflow.com/questions/45412228/sending-json-and-status-code-with-a-flask-response/45412576
@app.route('/up', methods=['GET','POST'])
def up():
    #log.info(scale_up())
    poolsize=1
    instancePool = exo.compute.get_instance_pool(id=poolID, zone=exoZone)
    if instancePool.size < 3:
        instancePool.scale(instancePool.size + poolsize)    
        log.info('scaled instance pool up')
    else:
        log.info("Reached Minimum!!")
    return 'OK', 200

@app.route('/down', methods=['GET','POST'])
def down():
    #log.info(scale_down())
    poolsize=-1
    instancePool = exo.compute.get_instance_pool(id=poolID, zone=exoZone)
    if instancePool.size > 1:
        instancePool.scale(instancePool.size + poolsize)
        log.info('scaled instance pool down')
    else:
        log.info("Reached Minimum!!")
    return 'OK', 200
    

if __name__ == '__main__':
    log.info("Starting....")
    log.info(exo)
    log.info(exoZone)
    log.info(zone)
    log.info(zoneID)
    log.info(listenPort)
    log.info(poolID)
    app.run(host='0.0.0.0', port=int(listenPort))
    log.info("Ready....")
