import json
import boto3

def lambda_handler(event, context):
    # Example: Fetching data from DynamoDB
    dynamodb = boto3.resource('dynamodb')
    table = dynamodb.Table('EnergyData')
    response = table.scan()
    return {
        "statusCode": 200,
        "body": json.dumps(response['Items'])
    }
