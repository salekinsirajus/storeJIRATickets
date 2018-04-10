import os
import json
import boto3
import logging

from item import Item

dynamodb = boto3.resource('dynamodb')

def create(event, context):
    table= dynamodb.Table(os.environ['DYNAMODB_TABLE'])

    try:
        data = json.loads(event['body'])
    except Exception as e:
        logging.error("Empty POST request")
        return {'statusCode': 422,
                'body':json.dumps({"Bad Request": "Recieved no body elements"})}
    
    if "created" not in data:
        logging.error("Item without a `created` value.")
        
        return {'statusCode': 422,
                'body':json.dumps({"Error Message": "missing `created` attribute"})}
    try:
        raw_item = Item(data)
        valid_item = raw_item.validate()
    except Exception as e:
        print(e)
        return {'statusCode': 422,
                'body':json.dumps({"Failed to validate input fields"})
            }
 
    table.put_item(Item=valid_item)

    response = {
        "statusCode": 200,
        "body": json.dumps(valid_item)
    }

    return response

