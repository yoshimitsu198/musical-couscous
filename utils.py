# Util 3
# Helper 8
# Util 13
# Helper 18
# Util 23
# Helper 28
# Util 33
# Helper 38
# Util 43
# Helper 48


"""
Musical Couscous - Bug Fix
"""

def safe_divide(a, b):
    """Safely divide two numbers with error handling"""
    if b == 0:
        raise ValueError("Division by zero is not allowed")
    return a / b

def parse_config(config_str):
    """Parse configuration string with improved error handling"""
    if not config_str:
        return {}
    
    try:
        import json
        return json.loads(config_str)
    except json.JSONDecodeError as e:
        print(f"Warning: Invalid JSON config: {e}")
        return {}
