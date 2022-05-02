def is_invalid_(modifiers: set[str], s: str) -> bool:
    if (set(s) & modifiers):
        return True
    return False
