import re
from aoc.helper import read_input


examples = [
    "1abc2",        # 12
    "pqr3stu8vwx",  # 38
    "a1b2c3d4e5f",  # 15
    "treb7uchet",   # 77
]
# sum = 142


def number_in_string(value: str):
    numbers = re.findall("[0-9]", value)
    number = f"{numbers[0]}{numbers[-1]}"
    return int(number)

examples = read_input("day_1/calibration_document.txt")
numbers = [number_in_string(example) for example in examples]

print(f"Part 1: {sum(numbers)}")
