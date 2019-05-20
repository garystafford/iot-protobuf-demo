import logging
import os
import socket
import sys
import time

import requests
import sensors_pb2
from gpiozero import LightSensor

URL = os.environ.get('GCF_LIGHT_URL')
JWT = os.environ.get('JWT')
FREQUENCY = 15
TYPE = 'Anmbest_MD46N'

ls = LightSensor(24)


def main():
    if not URL or not JWT:
        sys.exit("Are the Environment Variables set?")
    get_sensor_data(socket.gethostname())


def get_sensor_data(device_id):
    while True:
        try:
            if ls.value == 0.0:
                sensor_dli = sensors_pb2.SensorDLI()
                sensor_dli.device = device_id
                sensor_dli.type = TYPE
                sensor_dli.timestamp = time.time()
                sensor_dli.data.light = True

                payload = sensor_dli.SerializeToString()
                post_data(payload)
            time.sleep(FREQUENCY)
        except TypeError:
            logging.error('Error getting sensor data!')


def post_data(payload):
    logging.info(payload)

    headers = {
        'Content-Type': 'application/x-protobuf',
        'Authorization': JWT
    }

    try:
        requests.post(URL, data=payload, headers=headers)
    except requests.exceptions.ConnectionError:
        logging.error('Error posting data to Cloud Function!')
    except requests.exceptions.MissingSchema:
        logging.error('Error posting data to Cloud Function! Are Environment Variables set?')


if __name__ == '__main__':
    sys.exit(main())
