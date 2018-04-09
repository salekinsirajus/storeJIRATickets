import os
import json
import boto3

dynamodb = boto3.resource('dynamodb')

def store(event, context):
    table= dynamodb.Table(os.environ['DYNAMODB_TABLE'])

    # Make sure to do error checking here

    # hardcoding item
    # DYNAMODB CANT ACCEPT AN EMPTY STRING
    # DEAL WITH IT BEFORE ANYTHING
    item = {
        "summary" : "some bug",

        "created_at": "2018-01-10T20:15:07.958Z",

        "priority" : "Major" 
    }

    table.put_item(Item=item)

    response = {
        "statusCode": 200,
        "body": json.dumps(item)
    }

    return response
