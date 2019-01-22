def raindrops(number):
    sounds = {3: "Pling", 5: "Plang", 7: "Plong"}
    output = "".join((sounds[i] for i in sounds if number % i == 0))
    return output if output else str(number)
