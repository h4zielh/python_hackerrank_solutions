"""
return the highest score from list, pretty simple
"""

def get_highest_score(num: int, scores: list) -> int:
    """return the highest score from list."""

    # the highest number in scores
    num = scores[0]

    for i in scores:
        if i > num:
            num = i

    return num


if __name__ == "__main__":
    n = int(input())
    arr = map(int, input().split())

    print(get_highest_score(n, list(arr)))