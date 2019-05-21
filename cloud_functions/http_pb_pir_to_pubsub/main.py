import logging
import os

import jwt
import sensors_pb2
from flask import make_response, jsonify
from flask_api import status
from google.cloud import pubsub_v1
from google.protobuf.json_format import MessageToJson

TOPIC = os.environ.get('TOPIC')
SECRET_KEY = os.getenv('SECRET_KEY')
ID = os.getenv('ID')
PASSWORD = os.getenv('PASSWORD')


def incoming_message(request):
    if not validate_token(request):
        return make_response(jsonify({'success': False}),
                             status.HTTP_401_UNAUTHORIZED,
                             {'ContentType': 'application/json'})

    data = request.get_data()
    if not data:
        return make_response(jsonify({'success': False}),
                             status.HTTP_400_BAD_REQUEST,
                             {'ContentType': 'application/json'})
    logging.debug(str(data))

    sensor_pb = sensors_pb2.SensorPIR()
    sensor_pb.ParseFromString(data)

    sensor_json = MessageToJson(sensor_pb)
    send_message(sensor_json)

    return make_response(jsonify({'success': True}),
                         status.HTTP_201_CREATED,
                         {'ContentType': 'application/json'})


def validate_token(request):
    auth_header = request.headers.get('Authorization')
    if not auth_header:
        return False
    auth_token = auth_header.split(" ")[1]

    if not auth_token:
        return False
    try:
        payload = jwt.decode(auth_token, SECRET_KEY)
        if payload['id'] == ID and payload['password'] == PASSWORD:
            logging.debug(payload)
            return True
    except jwt.ExpiredSignatureError:
        return False
    except jwt.InvalidTokenError:
        return False


def send_message(message):
    publisher = pubsub_v1.PublisherClient()
    publisher.publish(topic=TOPIC, data=bytes(str(message), 'utf-8'))
    logging.debug(str(message))
