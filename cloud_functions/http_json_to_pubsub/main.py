import logging
import os

import jwt
from flask import make_response, jsonify
from flask_api import status
from google.cloud import pubsub_v1

TOPIC = os.environ.get('TOPIC')
SECRET_KEY = os.getenv('SECRET_KEY')
ID = os.getenv('ID')
PASSWORD = os.getenv('PASSWORD')


def incoming_message(request):
    if not validate_token(request):
        return make_response(jsonify({'success': False}),
                             status.HTTP_401_UNAUTHORIZED,
                             {'ContentType': 'application/json'})

    request_json = request.get_json()
    if not request_json:
        return make_response(jsonify({'success': False}),
                             status.HTTP_400_BAD_REQUEST,
                             {'ContentType': 'application/json'})

    logging.info(request_json)
    logging.info(len(request_json))

    send_message(request_json)

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
            logging.info(payload)
            return True
    except jwt.ExpiredSignatureError:
        return False
    except jwt.InvalidTokenError:
        return False


def send_message(message):
    publisher = pubsub_v1.PublisherClient()
    publisher.publish(topic=TOPIC, data=bytes(str(message), 'utf-8'))
    logging.info(str(message))
