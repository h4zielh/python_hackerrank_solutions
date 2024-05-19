"""
return the runner-up from list, pretty simple.

i had to use the math library because if i declared both highest and runner_up
as int() it would not work if the list contained a negative number, the function
goes through each element of the list, if the element is not the highest, compare if
its not equal to the current highest and if it's higher then the current runner-up,
if true just add the number as the new runner-up
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