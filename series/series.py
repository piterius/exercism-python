def slices(string, length):
    if length < 1 or len(string) < length:
        raise ValueError("You have entered invalid input")
    return [string[i:i + length] for i in range(len(string) - length + 1)]
