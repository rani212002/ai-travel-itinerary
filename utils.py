def validate_inputs(destination, days):
    if not destination:
        return False, "Destination cannot be empty"
    if days <= 0:
        return False, "Number of days must be greater than 0"
    return True, ""
