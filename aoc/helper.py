"""helper module to avoid code duplication"""

def read_input(doc_path):
    with open(doc_path) as f:
        values = f.readlines()
    values = [value.strip('\n') for value in values]
    return values