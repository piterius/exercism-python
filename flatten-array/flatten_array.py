def flatten(nested):
    output = []
    for element in nested:
        if isinstance(element, (list, tuple)):
            output.extend(flatten(element))
        elif element is not None:
            output.append(element)
    return output
