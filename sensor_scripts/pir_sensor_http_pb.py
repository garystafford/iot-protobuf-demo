import logging
import os
import socket
import sys
import time

import requests
import sensors_pb2
from gpiozero import MotionSensor, LED

URL = os.environ.get('GCF_PIR_URL')
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
    while True:
        led.off()
        pir.wait_for_no_motion()
        while True:
            try:
                pir.wait_for_motion()
                led.on()

                sensor_pir = sensors_pb2.SensorPIR()
                sensor_pir.device = device_id
                sensor_pir.type = TYPE
                sensor_pir.timestamp = time.time()
                sensor_pir.data.motion = True

                payload = sensor_pir.SerializeToString()
                post_data(payload)
                time.sleep(1)
                led.off()
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
