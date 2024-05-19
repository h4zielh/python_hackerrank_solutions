"""
return the runner-up from list, pretty simple.

this solution may be unoptimized because the funtion,
creates a copy
"""

import math

def get_runner_up(scores):
    highest = -math.inf
    runner_up = -math.inf

    for i in scores:
        if i > highest:
            if highest > runner_up:
                runner_up = highest
                
            highest = i

        elif i > runner_up and i != highest:
            runner_up = i

    return runner_up

if __name__ == "__main__":
    n = int(input())
    arr = map(int, input().split())

    print(get_runner_up(list(arr)))