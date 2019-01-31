def hey(sentence):
    sentence = sentence.strip()
    if len(sentence) == 0:
        return "Fine. Be that way!"
    elif sentence[-1] == '?' and sentence.isupper():
        return "Calm down, I know what I'm doing!"
    elif sentence[-1] == '?':
        return "Sure."
    elif sentence.isupper():
        return "Whoa, chill out!"
    else:
        return "Whatever."
