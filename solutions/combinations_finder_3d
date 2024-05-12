# i was gave a challenge to calculate every combination between x, y and z,
# beeing the sum of them different from n, i didn't want to use nested loops
# but i got bored to do the combination analisys. I'm not proud of this.

def find_valid_combinations(x: int, y: int, z: int, n: int) -> list:
    """Returns every non-repeating combination between x, y and z, being the sum of the three different from n."""

    combinations = []
    
    for a in range(x+1):
        for b in range(y+1):
            for c in range(z+1):
                if (a + b + c) != n and [a, b, c] not in combinations:
                    combinations += [[a, b, c]]
    
    return combinations
