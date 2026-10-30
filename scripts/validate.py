# Build: f0e6bc21e41c24d8a2c46195ede6e571

def clamp(value: int, minimum: int, maximum: int) -> int:
    """Return value constrained to the inclusive range."""
    return max(minimum, min(maximum, value))
