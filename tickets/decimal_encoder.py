import decimal
import json

class DecimalEncoder(json.JSONEncoder):
    """This is a hack around for JSONencoder not being able to encode decimals."""

    def default(self, obj):
        if isinstance(obj, decimal.Decimal):
            return int(obj)
        return super(DecimalEncoder, self).default(obj)
    
