#!/usr/bin/env python3
"""
FaaS function to calculate the surface area of a cube.
Formula: surface_area = 6 * side^2
"""

import json

def handle(event, context):
    """
    Handle the FaaS request to calculate cube surface area.
    
    Expected input JSON:
    {
        "side": float
    }
    
    Returns JSON:
    {
        "statusCode": int,
        "body": str
    }
    """
    try:
        req_data = json.loads(event.body.decode('utf8'))
        
        # Validate input
        if "side" not in req_data:
            return {
                "statusCode": 400,
                "body": "Missing required parameter: side"
            }
        
        side = float(req_data["side"])
        
        # Validate side length
        if side <= 0:
            return {
                "statusCode": 400,
                "body": "Side length must be positive"
            }
        
        # Calculate surface area (6 faces, each with area = side^2)
        surface_area = 6 * (side ** 2)
        
        # Return result
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
