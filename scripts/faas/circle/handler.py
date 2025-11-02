import json
import math

def lambda_handler(event, context):
    try:
        req_data = json.loads(event['body'])
        
        if "radius" not in req_data:
            return {
                "statusCode": 400,
                "body": "Missing required parameter: radius"
            }
        
        radius = float(req_data["radius"])
        
        if radius <= 0:
            return {
                "statusCode": 400,
                "body": "Radius must be positive"
            }
        
        surface_area = math.pi * (radius ** 2)
        
        result = {
            "surface_area": surface_area,
            "radius": radius,
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
