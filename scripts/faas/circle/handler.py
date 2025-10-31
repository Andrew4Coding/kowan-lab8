#!/usr/bin/env python3
"""
FaaS function to calculate the surface area of a circle.
Formula: area = π * radius^2
"""

import json
import math

def handle(event, context):
    """
    Handle the FaaS request to calculate circle surface area.
    
    Expected input JSON:
    {
        "radius": float
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
        if "radius" not in req_data:
            return {
                "statusCode": 400,
                "body": "Missing required parameter: radius"
            }
        
        radius = float(req_data["radius"])
        
        # Validate radius
        if radius <= 0:
            return {
                "statusCode": 400,
                "body": "Radius must be positive"
            }
        
        # Calculate surface area
        surface_area = math.pi * (radius ** 2)
        
        # Return result
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

