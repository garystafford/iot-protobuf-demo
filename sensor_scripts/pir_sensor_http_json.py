import json
import logging
import os
import socket
import sys
import time

import requests
from gpiozero import MotionSensor, LED

URL = os.environ.get('GCF_URL')
JWT = os.environ.get('JWT')
FREQUENCY = 15
TYPE = 'Onyehn_PIR'

pir = MotionSensor(23)
led = LED(25)


def main():
    if not URL or not JWT:
        sys.exit("Are the Environment Variables set?")
    get_sensor_data(socket.gethostname())


def get_sensor_data(device_id):
    led.off()
    pir.wait_for_no_motion()
    while True:
        pir.wait_for_motion()
        led.on()
        payload = {'device': device_id,
                   'type': TYPE,
                   'timestamp': time.time(),
                   'data': {'motion': True}}
        post_data(payload)
        time.sleep(1)
        led.off()
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
