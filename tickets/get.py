import json
import boto3
import os

from decimal_encoder import DecimalEncoder 

dynamodb = boto3.resource('dynamodb')

def get(event, context):
    table = dynamodb.Table(os.environ['DYNAMODB_TABLE'])

    desired_ticket = table.get_item(
        Key = {
            'id': event['pathParameters']['id']
        }

    )

    response = {
        "statusCode": 200,
        'body': json.dumps(desired_ticket['Item'], cls=DecimalEncoder)
    }

    return response
