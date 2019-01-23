codons = {"AUG": "Methionine", "UUU": "Phenylalanine", "UUC": "Phenylalanine", "UUA": "Leucine", "UUG": "Leucine",
          "UCU": "Serine", "UCC": "Serine", "UCA": "Serine", "UCG": "Serine", "UAU": "Tyrosine", "UAC": "Tyrosine",
          "UGU": "Cysteine", "UGC": "Cysteine", "UGG": "Tryptophan", "UAA": "STOP", "UAG": "STOP", "UGA": "STOP"}


def proteins(strand):
    result = []
    for i in range(0, len(strand), 3):
        if strand[i:i + 3] not in codons:
            raise ValueError("Incorrect strand")
        if codons[strand[i:i + 3]] == "STOP":
            return result
        else:
            result.append(codons[strand[i:i + 3]])
    return result

