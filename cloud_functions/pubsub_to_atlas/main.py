import base64
import json
import logging
import os

import pymongo

MONGODB_CONN = os.environ.get('MONGODB_CONN')
MONGODB_DB = os.environ.get('MONGODB_DB')
MONGODB_COL = os.environ.get('MONGODB_COL')


def read_message(event, context):
    message = base64.b64decode(event['data']).decode('utf-8')

    message = message.replace("'", '"')
    message = message.replace('True', 'true')
    message = json.loads(message)
    logging.debug(message)

    client = pymongo.MongoClient(MONGODB_CONN)
    db = client[MONGODB_DB]
    col = db[MONGODB_COL]
    col.insert_one(message)
