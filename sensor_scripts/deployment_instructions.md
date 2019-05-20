# Deploying Scripts

On local machine

```bash
# move to scripts directory
cd sensor_scripts/

# get last protobuf file
cp -f ./../sensors_pb/sensors_pb2.py .

# copy files to IoT devices
scp -i ~/.ssh/your_key *.py user@device_ip:/path/to/scripts
scp -i ~/.ssh/your_key requirements.txt user@device_ip:/path/to/scripts
```

On IoT Devices

```bash
# move to scripts directory
cd Documents/

# install required Python packages
pip3 install -r requirements.txt

# ** MUST CHANGE VALUES **
# set env vars local to device
export GCF_URL="https://us-central1-your-project.cloudfunctions.net/http_json_to_pubsub"
export GCF_DHT_URL="https://us-central1-your-project.cloudfunctions.net/http_pb_dht_to_pubsub"
export GCF_PIR_URL="https://us-central1-your-project.cloudfunctions.net/http_pb_pir_to_pubsub"
export GCF_LIGHT_URL="https://us-central1-your-project.cloudfunctions.net/http_pb_light_to_pubsub"
export JWT="Bearer CRc1XphcIGJIUieCn6IyIVOIsz5i9NiJIkbJ.ViQRU9MjUGzT1BnAzl9DHINR5JFXQyydiWWbYgbiIJjZLiEVt3i9OIHBiJZ1DwJQCEyCvRrVkXNGJhWa1Rmtj3N1iN33hUieNZo63ddY00dOjlbwSyUUYMgOQ2OaWhCydTzYY1IpxEJhyN2vk4i3YydwNjApSimWIRLGDdIp2QIi1ZebHJNncyVZ.XeeeghYHNtOH67ytm0vdfoP4vFgUZ3uT9oIlEk4UkcB"

# start scripts as background processes
# either use json over http
nohup python3 -u dht_sensor_http_pb.py > output_dht.log 2>&1 </dev/null &
nohup python3 -u pir_sensor_http_pb.py > output_pir.log 2>&1 </dev/null &
nohup python3 -u light_sensor_http_pb.py > output_ls.log 2>&1 </dev/null &

# or use protobuf over http
nohup python3 -u dht_sensor_http_pb.py > output_dht.log 2>&1 </dev/null &
nohup python3 -u pir_sensor_http_pb.py > output_pir.log 2>&1 </dev/null &
nohup python3 -u light_sensor_http_pb.py > output_ls.log 2>&1 </dev/null &

ps aux | grep '_sensor_http_pb.py'
```
