#!/usr/bin/env python3
"""
FaaS function to calculate the surface area of a square.
Formula: area = side * side
"""

import json
import sys


def handle(req):
    """
    Handle the FaaS request to calculate square surface area.
    
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
            return json.dumps({
                "error": "Missing required parameter: side"
            })
        
        side = float(data["side"])
        
        # Validate side length
        if side <= 0:
            return json.dumps({
                "error": "Side length must be positive"
            })
        
        # Calculate surface area
        surface_area = side * side
        
        # Return result
        return json.dumps({
            "surface_area": surface_area,
            "side": side,
            "unit": "square units"
        })
        
    except ValueError as e:
        return json.dumps({
            "error": f"Invalid input: {str(e)}"
        })
    except Exception as e:
        return json.dumps({
            "error": f"Unexpected error: {str(e)}"
        })


if __name__ == "__main__":
    # Read from stdin (FaaS standard)
    req = sys.stdin.read()
    result = handle(req)
    print(result)
