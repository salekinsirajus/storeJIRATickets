import os
import json
import boto3

from decimal_encoder import DecimalEncoder

dynamodb = boto3.resource('dynamodb')

def list(event, context):
    table = dynamodb.Table(os.environ['DYNAMODB_TABLE'])

    result = table.scan()

    # This is a list of items, like the following:
    # [{"priority": "Major", "summary": "some bug", "created_at":
    # "2018-01-10T20:15:07.958Z"}]
    response = {
        "statusCode": 200,
        "body": json.dumps(result['Items'], cls=DecimalEncoder)
    }

    return response
