def safe_divide(numerator, denominator):
    """
    Safely divides two numbers and handles division by zero.

    Args:
        numerator (float): The number to be divided.
        denominator (float): The number to divide by.

    Returns:
        float: The result of the division if denominator is not zero.
        None: If denominator is zero.
    """
    try:
        result = numerator / denominator
        return result
    except ZeroDivisionError:
        print("Error: Cannot divide by zero.")
        return None

# Example usage
result = safe_divide(10, 0)
if result is not None:
    print("Result:", result)
    # Optimized: Move print outside the if-block to avoid code duplication and handle None gracefully
print("Result:", result if result is not None else "No result due to division by zero.")
