import time
import ssl
import paho.mqtt.client as mqtt

# aws setup
ENDPOINT = "a3qu0eqgl713bh-ats.iot.us-east-1.amazonaws.com"
TOPIC = "test/hw1"

# secrets
CA_PATH = "/Users/yasminesubbagh/Documents/Secrets/aws/AmazonRootCA1.pem"
CERT_PATH = "/Users/yasminesubbagh/Documents/Secrets/css532/IoT_macbook/2510e3af5d450b8fc31e2d40887791594e52031e0ee15fdd1b8f0edbcc94220f-certificate.pem.crt"
KEY_PATH = "/Users/yasminesubbagh/Documents/Secrets/css532/IoT_macbook/2510e3af5d450b8fc31e2d40887791594e52031e0ee15fdd1b8f0edbcc94220f-private.pem.key"
