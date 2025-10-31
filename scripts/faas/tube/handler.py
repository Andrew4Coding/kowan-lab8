#!/usr/bin/env python3
"""
FaaS function to calculate the surface area of a tube (cylinder).
Formula: surface_area = 2πr(r + h)
where r is radius and h is height
"""

import json
import math

def handle(event, context):
    """
    Handle the FaaS request to calculate tube/cylinder surface area.
    
    Expected input JSON:
    {
        "radius": float,
        "height": float
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
        
        if "height" not in req_data:
            return {
                "statusCode": 400,
                "body": "Missing required parameter: height"
            }
        
        radius = float(req_data["radius"])
        height = float(req_data["height"])
        
        # Validate dimensions
        if radius <= 0:
            return {
                "statusCode": 400,
                "body": "Radius must be positive"
            }
        
        if height <= 0:
            return {
                "statusCode": 400,
                "body": "Height must be positive"
            }
        
        # Calculate surface area
        # Surface area = 2πr² (top and bottom circles) + 2πrh (curved surface)
        # = 2πr(r + h)
        surface_area = 2 * math.pi * radius * (radius + height)
        
        # Return result
        result = {
            "surface_area": surface_area,
            "radius": radius,
            "height": height,
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
