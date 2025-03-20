def generate_pattern():
    pattern = [
        [" " * 12 + "1   2   3   4"],
        [" " * 8 + "8   7   6   5"],
        [" " * 4 + "9  10  11  12"],
        ["16  15  14  13"]
    ]
    for row in pattern:
        print(row[0])
generate_pattern()


