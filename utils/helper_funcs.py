from math import sqrt

def deep_compare_lists(a: list, b: list) -> bool:
    """
    Use sparingly. We're n^2 for this one.
    """
    for a_item in a:
        if not a_item in b:
            return False
    return True

def euc_dis(a: tuple, b: tuple) -> float:
    return sqrt((a[0] - b[0])**2 + (a[1] - b[1])**2)

def tup_add(a:tuple, b: tuple) -> tuple:
    return (a[0] + b[0], a[1] + b[1])


if __name__ == '__main__':
    print(euc_dis((0,0), (3,4)))