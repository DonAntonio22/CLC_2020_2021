import json
import os
import pprint
import signal
import time

import exoscale
from exoscale import Exoscale
from exoscale.api.compute import Zone


def service_discovery(exo: Exoscale, zone: Zone, pool_id: str, port: int, file: str):
    instance_pool = exo.compute.get_instance_pool(pool_id, zone=zone)
    instances = instance_pool.instances
    targets = []
    for instance in instances:
        if instance.ipv4_address is not None:
            targets.append(instance.ipv4_address + ":" + str(port))

    with open(file, "w") as f:
        f.write(json.dumps(
            [
                {
                    "targets": targets,
                    "labels": {}
                }
            ]
        ))


finished = False


def finish(signum, frame):
    global finished
    finished = True


signal.signal(signal.SIGTERM, finish)


def loop_service_discovery(
        key: str,
        secret: str,
        zone_name: str,
        pool_id: str,
        port: int,
        file: str
):
    global finished
    exo = exoscale.Exoscale(api_key=key, api_secret=secret, config_file="")

    zone = exo.compute.get_zone(zone_name)

    failed_sd = 0

    while not finished:
        if failed_sd > 10:
            raise Exception("Too many service discovery failures.")
        try:
            service_discovery(exo, zone, pool_id, port, file)
            failed_sd = 0
        except Exception as err:
            pprint.pprint(err)
            failed_sd = failed_sd + 1
        time.sleep(5)


if __name__ == "__main__":
    api_key = os.environ["EXOSCALE_KEY"]
    api_secret = os.environ["EXOSCALE_SECRET"]
    api_zone = os.environ["EXOSCALE_ZONE"]
    instance_pool_id = os.environ["EXOSCALE_INSTANCEPOOL_ID"]
    target_port = int(os.environ["TARGET_PORT"])
    sd_file = "/srv/service-discovery/config.json"

    print("Starting service discovery")
    loop_service_discovery(api_key, api_secret, api_zone, instance_pool_id, target_port, sd_file)
