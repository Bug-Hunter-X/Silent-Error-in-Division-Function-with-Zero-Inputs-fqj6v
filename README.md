# Silent Error in Division Function

This repository demonstrates a subtle error in a Python function that handles division. The function doesn't explicitly raise an exception when both inputs are zero, leading to unexpected behavior.

## The Bug
The `function_with_uncommon_error` function has a flaw.  If both `a` and `b` are 0, a ZeroDivisionError is raised in Python 3.11 and above. However in previous versions of Python, this would silently return 0.  This silent error can be difficult to detect, especially in larger programs. 

## The Solution
The solution explicitly checks for this edge case and raises a ValueError or returns a specific value to handle this situation.