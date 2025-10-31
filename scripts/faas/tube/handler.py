#!/usr/bin/env python3
"""
FaaS function to calculate the surface area of a tube (cylinder).
Formula: surface_area = 2πr(r + h)
where r is radius and h is height
"""

import json
import math
import sys


def handle(req, context):
    """
    Handle the FaaS request to calculate tube/cylinder surface area.
    
    Expected input JSON:
    {
        "radius": float,
        "height": float
    }
    
    Returns JSON:
    {
        "surface_area": float,
        "unit": "square units"
    }
    """
    try:
        # Parse input JSON
        data = json.loads(req)
        
        # Validate input
        if "radius" not in data:
            return {
                "error": "Missing required parameter: radius"
            }
        
        if "height" not in data:
            return {
                "error": "Missing required parameter: height"
            }
        
        radius = float(data["radius"])
        height = float(data["height"])
        
        # Validate dimensions
        if radius <= 0:
            return {
                "error": "Radius must be positive"
            }
        
        if height <= 0:
            return {
                "error": "Height must be positive"
            }
        
        # Calculate surface area
        # Surface area = 2πr² (top and bottom circles) + 2πrh (curved surface)
        # = 2πr(r + h)
        surface_area = 2 * math.pi * radius * (radius + height)
        
        # Return result
        return {
            "surface_area": surface_area,
            "radius": radius,
            "height": height,
            "unit": "square units"
        }
        
    except ValueError as e:
        return {
            "error": f"Invalid input: {str(e)}"
        }   
    except Exception as e:
        return {
            "error": f"Unexpected error: {str(e)}"
        }
