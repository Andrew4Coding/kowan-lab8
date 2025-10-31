#!/usr/bin/env python3
"""
FaaS function to calculate the surface area of a cube.
Formula: surface_area = 6 * side^2
"""

import json
import sys


def handle(req, context):
    """
    Handle the FaaS request to calculate cube surface area.
    
    Expected input JSON:
    {
        "side": float
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
        if "side" not in data:
            return {
                "error": "Missing required parameter: side"
            }
        
        side = float(data["side"])
        
        # Validate side length
        if side <= 0:
            return {
                "error": "Side length must be positive"
            }
        
        # Calculate surface area (6 faces, each with area = side^2)
        surface_area = 6 * (side ** 2)
        
        # Return result
        return {
            "surface_area": surface_area,
            "side": side,
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
