#  HW1 - CSS 532
#   Yasmine Subbagh
# part 4



from awscrt import mqtt, http
from awsiot import mqtt_connection_builder
import json


# Define MQTT connection details
mqtt_connection = mqtt_connection_builder.mtls_from_path(
    endpoint="a3qu0eqgl713bh-ats.iot.us-east-1.amazonaws.com",
    cert_filepath="/Users/yasminesubbagh/Documents/Secrets/css532/IoT_macbook/2510e3af5d450b8fc31e2d40887791594e52031e0ee15fdd1b8f0edbcc94220f-certificate.pem.crt",
    pri_key_filepath="/Users/yasminesubbagh/Documents/Secrets/css532/IoT_macbook/2510e3af5d450b8fc31e2d40887791594e52031e0ee15fdd1b8f0edbcc94220f-private.pem.key",
    ca_filepath="/Users/yasminesubbagh/Documents/Secrets/css532/IoT_macbook/AmazonRootCA1.pem",
    client_id="Yasmine_macbookpro",
    clean_session=False,
    keep_alive_secs=30
)

# Function to handle user commands
def on_command_received(topic, payload, **kwargs):
    command_data = json.loads(payload.decode('utf-8'))  # Decode and parse JSON
    command = command_data.get("message") 
    print(f"Received command: {command}")

    # Custom response logic based on command
    response_message = f"Device processed the command: {command}."
    if command == "AWS":
        response_message += f" Correct!"
    elif command == "Azure":
        response_message += f" Boooooooo!"
    else:
        response_message += f" Boring... play the game."
    
    # Publish response back to AWS IoT
    response_payload = json.dumps(response_message)
    mqtt_connection.publish(
        topic="user/response",
        payload=response_payload,
        qos=mqtt.QoS.AT_LEAST_ONCE
    )
    print(f"Sent response: {response_message}")

    

# Connect and subscribe to the user commands topic
mqtt_connection.connect().result()
mqtt_connection.subscribe(topic="user/commands", qos=mqtt.QoS.AT_LEAST_ONCE, callback=on_command_received)

# Keep the script running to listen for commands
while True:
    pass
