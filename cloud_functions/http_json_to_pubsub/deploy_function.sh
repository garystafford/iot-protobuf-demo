#!/usr/bin/env bash

# get latest env vars file
cp -f ./../env_vars_file/env.yaml .

# deploy function
gcloud functions deploy http_json_to_pubsub \
  --runtime python37 \
  --trigger-http \
  --region us-central1 \
  --memory 256 \
  --entry-point incoming_message \
  --env-vars-file env.yaml