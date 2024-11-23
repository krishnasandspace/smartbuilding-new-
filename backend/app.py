import json
import boto3

def lambda_handler(event, context):
    # Log incoming data
    print("Received event: ", event)
    
    # Extract temperature data
    temperature = event['temperature']
    device_id = event['device_id']
    
    # Check temperature threshold
    if temperature > 30:
        sns_client = boto3.client('sns')
        sns_client.publish(
            TopicArn="arn:aws:sns:<us-east-1>:<9825-3438-7133>:HighTempAlerts",
            Message=f"Temperature Alert! Device {device_id} reported {temperature}°C.",
            Subject="High Temperature Alert"
        )
        return {"message": "Alert sent!"}
    else:
        return {"message": "Temperature is normal."}
