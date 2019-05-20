import logging
import os
import socket
import sys
import time

import Adafruit_DHT
import requests
import sensors_pb2

URL = os.environ.get('GCF_DHT_URL')
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
        try:
            humidity, temperature = Adafruit_DHT.read_retry(SENSOR, PIN)

            sensor_dht = sensors_pb2.SensorDHT()
            sensor_dht.device = device_id
            sensor_dht.type = TYPE
            sensor_dht.timestamp = time.time()
            sensor_dht.data.temperature = temperature
            sensor_dht.data.humidity = humidity

            payload = sensor_dht.SerializeToString()

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
