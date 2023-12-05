from aoc.helper import read_input


SPELLED_NUMS = {
    "one": "1",
    "two": "2",
    "three": "3",
    "four": "4",
    "five": "5",
    "six": "6",
    "seven": "7",
    "eight": "8",
    "nine": "9"
}

DIGITS = [ 
    "one", "two", "three", "four", "five", "six", "seven", "eight", "nine",
    "1", "2", "3", "4", "5", "6", "7", "8", "9"
    ]

def read_calibration_doc(doc_path:str):
    with open(doc_path) as f:
        values = f.readlines()
    values = [value.strip('\n') for value in values]
    return values


examples = [
    "two1nine",                                # 29
    "eightwothree",                            # 83
    "abcone2threexyz",                         # 13
    "xtwone3four",                             # 24
    "4nineeightseven2",                        # 42
    "zoneight234",                             # 14
    "7pqrstsixteen",                           # 76  -> sum = 281
    "nineight",                                # 98  -> someone told me this tip let's see
]

def find_digit(value: str, operation):
    for d in DIGITS:
        if operation(value, d):
            if len(d) > 2:
                return SPELLED_NUMS[d]
            return d

    for r in range(1, len(value)):
        for d in DIGITS:
            if operation(value[r:], d) or operation(value[:-r], d):
                if len(d) > 2:
                    return SPELLED_NUMS[d]
                return d


first_num = last_num = ""

examples = read_input("day_1/calibration_document.txt")
numbers = list()
for example in examples:
    first_num = find_digit(example, str.startswith)
    last_num = find_digit(example, str.endswith)

    numbers.append(int(f"{first_num}{last_num}"))

print(numbers)
print(f"Part 2: {sum(numbers)}")