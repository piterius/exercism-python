def transform(input_dict):
    return {letter.lower(): points for points, letters in input_dict.items() for letter in letters}