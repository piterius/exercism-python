def to_rna(input_str):
    if any((a for a in input_str if a not in 'GCTA')):
        raise ValueError("Invalid input.")
    trans_table = str.maketrans("GTCA", "CAGU")
    return input_str.translate(trans_table)
