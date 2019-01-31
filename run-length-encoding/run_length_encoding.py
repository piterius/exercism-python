def encode3(data):
    output, prev, count = '', '', 0
    for char in data:
        if char != prev:
            output += str(count) + prev if count > 1 else prev
            prev, count = char, 1
        else:
            count += 1
    else:
        output += str(count) + prev if count > 1 else prev
    return output


def decode(data):
    output, count = '', []
    for char in data:
        if char.isdigit():
            count.append(char)
        else:
            output += int("".join(count)) * char if count else char
            count = []
    return output
