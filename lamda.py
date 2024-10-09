#  HW1 - CSS 532
#   Yasmine Subbagh
# part 5


import json
import boto3

s3 = boto3.client('s3')
myBucket = "iothw1"

def processData(event, context):
    
    print(json.dumps(event))
    
    # get numbers from JSON
    payload = event
    numbers = payload['data']  

    # avergae values
    avg = sum(numbers) / len(numbers)

    # data back into JSON 
    raw_data = {"raw_data": numbers}
    processed_data = {"average": avg}

    # Save data to S3
    s3.put_object(Bucket=myBucket, Key='raw_data.json', Body=json.dumps(raw_data))
    s3.put_object(Bucket=myBucket, Key='processed_average_data.json', Body=json.dumps(processed_data))

    return {
        'statusCode': 200,
        'body': json.dumps('Data processed and saved successfully!')
    }
