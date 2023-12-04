
def read_input(doc_path):
    with open(doc_path) as f:
        values = f.readlines()
    values = [value.strip('\n') for value in values]
    return values

games = read_input("day_2/input.txt")

cube_limits = {
    "red": "12",
    "green": "13",
    "blue": "14",
}

def transform_set(s):
    """given a set return true if possible, false otherwise"""
    cube_limits = {
        "red": 12,
        "green": 13,
        "blue": 14,
    }

    for value in s:
        amount, color = value.split(' ')
        if int(amount) > cube_limits[color]:
            return False
    return True


possible_ids = []
for game_id, g in enumerate(games):
    _, sets = g.split(': ')
    sets = sets.split('; ')
    sets = [s.split(', ') for s in sets]
    transformed = []
    for s in sets:
        transformed.append(transform_set(s))
    
    if all(transformed):
        print(f"Game ID: {game_id+1}, Possible")
        possible_ids.append(game_id+1)

print(sum(possible_ids))
