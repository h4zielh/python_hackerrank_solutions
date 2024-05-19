"""
return the runner-up from list, pretty simple.
"""

def get_runner_up(num: int, scores: list) -> int:
    """return the runner-up from list."""

    # list copy
    score_copy = set(scores.copy())
    
    score_list = list(score_copy)
    
    score_list.sort()

    return score_list[-2]

if __name__ == "__main__":
    n = int(input())
    arr = map(int, input().split())

    print(get_runner_up(n, list(arr)))