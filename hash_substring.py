
def read_input():
    """
    This function acquires input both from keyboard and file.
    Use capital "I" (input from keyboard) and capital "F" (input from file) to choose the input type.

    After input type choice, read two lines: first line is pattern, and second line is text in which to look for pattern.
    """
    input_type = input().strip().upper()

    if input_type == 'F':
        try:
            with open("./tests/06") as file:
                pattern = file.readline().strip()
                text = file.readline().strip()
        except FileNotFoundError:
            print("File not found.")
            return None

    elif input_type == 'I':
        pattern = input().strip()
        text = input().strip()

    else:
        print("Invalid input type.")
        return None

    return pattern, text


def get_occurrences(pattern, text):
    """
    This function finds the occurrences of pattern in text using Rabin-Karp algorithm.

    Returns a list of indices where pattern is found.
    """
    occurrences = []
    pattern_length = len(pattern)
    text_length = len(text)
    pattern_hash = hash(pattern)

    for i in range(text_length - pattern_length + 1):
        if hash(text[i:i+pattern_length]) == pattern_hash:
            if text[i:i+pattern_length] == pattern:
                occurrences.append(i)

    return occurrences


def print_occurrences(output):
    """
    This function prints the output of the program.
    """
    print(' '.join(map(str, output)))


if __name__ == '__main__':
    input_data = read_input()
    if input_data:
        pattern, text = input_data
        pattern_occurrences = get_occurrences(pattern, text)
        print_occurrences(pattern_occurrences)
