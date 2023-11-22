def deep_compare_lists(a: list, b: list) -> bool:
    """
    Use sparingly. We're n^2 for this one.
    """
    for a_item in a:
        if not a_item in b:
            return False
    return True