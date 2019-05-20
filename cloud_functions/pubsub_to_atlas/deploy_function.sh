#!/usr/bin/env bash

# get MongoDB connection string
# must be set in terminal session before running script!
export MONGODB_CONN

# if not set, fail...
if [[ $(echo ${MONGODB_CONN}) = '' ]]
then
    echo "variable MONGODB_CONN not set"
    exit 1
fi

# deploy function
gcloud functions deploy pubsub_to_atlas \
  --runtime python37 \
  --trigger-topic iot-data-demo \
  --region us-central1 \
  --memory 256 \
  --entry-point read_message \
  --set-env-vars MONGODB_CONN="${MONGODB_CONN}",MONGODB_DB="iot-data-demo",MONGODB_COL="iot_data"
