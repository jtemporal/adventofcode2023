import re


examples = [
    "1abc2",        # 12
    "pqr3stu8vwx",  # 38
    "a1b2c3d4e5f",  # 15
    "treb7uchet",   # 77
]
# sum = 142

def read_calibration_doc(doc_path:str):
    with open(doc_path) as f:
        values = f.readlines()
    values = [value.strip('\n') for value in values]
    return values


def number_in_string(value: str):
    numbers = re.findall("[0-9]", value)
    number = f"{numbers[0]}{numbers[-1]}"
    return int(number)

examples = read_calibration_doc("day_1/calibration_document.txt")
numbers = [number_in_string(example) for example in examples]

print(f"Part 1: {sum(numbers)}")
