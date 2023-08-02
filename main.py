def plus(compression: str) -> int:
    left, right = compression.split('+')
    left, right = int(left), int(right)
    result = left + right
    return result
