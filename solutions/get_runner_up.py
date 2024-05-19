"""
return the runner-up from list, pretty simple.

this solution may be unoptimized because the funtion,
creates a copy
"""

def get_runner_up(scores: list) -> int:
    """return the runner-up from list."""

    # list copy
    score_copy = list(set(scores.copy()))
    
    score_copy.sort()

    return score_copy[-2]

def test(scores):
    highest = -int()
    runner_up = -int()

    print(scores)

    for i in scores:
        if i > highest:
            runner_up = highest
            highest = i
            print(runner_up, highest)

    return runner_up

if __name__ == "__main__":
    n = int(input())
    arr = map(int, input().split())

    print(test(list(arr)))