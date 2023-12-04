from functools import reduce
from itertools import chain


def read_input(doc_path):
    with open(doc_path) as f:
        values = f.readlines()
    values = [value.strip('\n') for value in values]
    return values


def transform_set(s):
    """Multiply the values for each cube"""
    cube_limits = {
        "red": 0,
        "green": 0,
        "blue": 0,
    }
    for value in s:
        amount, color = value.split(' ')
        if int(amount) > cube_limits[color]:
            cube_limits[color] = int(amount)
    
    return reduce((lambda x, y: x * y), list(cube_limits.values()))


games = read_input("day_2/input.txt")

values = []
for game_id, g in enumerate(games):
    _, sets = g.split(': ')
    sets = sets.split('; ')
    sets = [s.split(', ') for s in sets]
    flattened = [s for s in chain(*sets)]
    values.append(transform_set(flattened))

print(sum(values))