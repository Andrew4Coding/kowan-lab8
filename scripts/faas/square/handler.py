"""
FaaS function to calculate the surface area of a square.
Formula: area = side * side
"""

import json

def lambda_handler(event, context):
    try:
        req_data = json.loads(event['body'])
        
        if "side" not in req_data:
            return {
                "statusCode": 400,
                "body": "Missing required parameter: side"
            }
        
        side = float(req_data["side"])
        
        if side <= 0:
            return {
                "statusCode": 400,
                "body": "Side length must be positive"
            }
        
        surface_area = side * side
        
        result = {
            "surface_area": surface_area,
            "side": side,
            "unit": "square units"
        }
        
        return {
            "statusCode": 200,
            "body": json.dumps(result)
        }
        
    except ValueError as e:
        return {
            "statusCode": 400,
            "body": f"Invalid input: {str(e)}"
        }
    except Exception as e:
        return {
            "statusCode": 500,
            "body": f"Internal Error: {str(e)}"
        }