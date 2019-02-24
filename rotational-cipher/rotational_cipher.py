from string import ascii_lowercase as lower, ascii_uppercase as upper


def rotate(text, count):
    output = []
    for symbol in text:
        if symbol in lower:
            output.append(lower[(lower.index(symbol) + count) % 26])
        elif symbol in upper:
            output.append(upper[(upper.index(symbol) + count) % 26])
        else:
            output.append(symbol)
    return "".join(output)
