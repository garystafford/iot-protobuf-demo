import json
import logging
import os
import socket
import sys
import time

import Adafruit_DHT
import requests

URL = os.environ.get('GCF_URL')
JWT = os.environ.get('JWT')
SENSOR = Adafruit_DHT.DHT22
TYPE = 'DHT22'
PIN = 18
FREQUENCY = 15


def main():
    if not URL or not JWT:
        sys.exit("Are the Environment Variables set?")
    get_sensor_data(socket.gethostname())


def get_sensor_data(device_id):
    while True:
        humidity, temperature = Adafruit_DHT.read_retry(SENSOR, PIN)
        payload = {'device': device_id,
                   'type': TYPE,
                   'timestamp': time.time(),
                   'data': {'temperature': temperature,
                            'humidity': humidity}}
        post_data(payload)
        time.sleep(FREQUENCY)


def post_data(payload):
    payload = json.dumps(payload)
    logging.info(payload)

    headers = {
        'Content-Type': 'application/json; charset=utf-8',
        'Authorization': JWT
    }

    try:
        requests.post(URL, json=payload, headers=headers)
    except requests.exceptions.ConnectionError:
        logging.error('Error posting data to Cloud Function!')
    except requests.exceptions.MissingSchema:
        logging.error('Error posting data to Cloud Function! Are Environment Variables set?')


if __name__ == '__main__':
    sys.exit(main())
