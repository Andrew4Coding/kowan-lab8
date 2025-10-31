#!/usr/bin/env python3
"""
FaaS function to calculate the surface area of a circle.
Formula: area = π * radius^2
"""

import json
import math
import sys


def handle(req, context):
    """
    Handle the FaaS request to calculate circle surface area.
    
    Expected input JSON:
    {
        "radius": float
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
        
        radius = float(data["radius"])
        
        # Validate radius
        if radius <= 0:
            return {
                "error": "Radius must be positive"
            }
        
        # Calculate surface area
        surface_area = math.pi * (radius ** 2)
        
        # Return result
        return {
            "surface_area": surface_area,
            "radius": radius,
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

