def function_with_uncommon_error(a, b):
    if a == 0 and b == 0:
        raise ValueError("Both inputs cannot be zero")  # Or return a specific value like None, inf, nan
    elif a == 0:
        return b
    elif b == 0:
        return a
    else:
        return a / b

try:
    result = function_with_uncommon_error(0, 0)
    print(result)
except ValueError as e:
    print(f"Error: {e}")
