"""
return the runner-up fromlist pretty simple.
"""

def get_runner_up(num: int, scores: list) -> int:
    """return the highest score from list."""

    

    # the highest number in scores
    num = scores[0]

    # the runner-up, second highest number in scores
    runner_up = scores[0]

    for i in scores:
        if i > num:
            num = i

        elif i > runner_up:
            runner_up = i

    return runner_up


if __name__ == "__main__":
    n = int(input())
    arr = map(int, input().split())

    print(get_highest_score(n, list(arr)))