import decimal
import json

class DecimalEncoder(json.JSONEncoder):
    """This is a hack around for JSONencoder not being able to encode decimals.

    found here: https://github.com/serverless/examples/blob/master/aws-python-rest-api-with-dynamodb/todos/decimalencoder.py
    """
    def default(self, obj):
        if isinstance(obj, decimal.Decimal):
            return int(obj)
        return super(DecimalEncoder, self).default(obj)
    
