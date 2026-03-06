def mean(values: list[float]) -> float:
    if len(values) == 0:
        raise ValueError("values must not empty")
    return sum(values) / len(values)