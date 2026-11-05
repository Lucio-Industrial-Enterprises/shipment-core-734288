"""Parse pick-list quantities."""


def parse_quantity(value: str) -> int:
    result = int(value.strip())
    if result < 0:
        raise ValueError(f"quantity must be non-negative, got {result}")
    return result
