from collections import Counter
from jellyfish import damerau_levenshtein_distance as dld


def main():
    with open("input.txt") as file:
        raw_input = file.read().splitlines()

    part_one(raw_input)
    part_two(raw_input)


def part_one(data):
    dubs = 0
    trips = 0
    for line in data:
        string = dict(Counter(line))
        if 2 in string.values():
            dubs += 1
        if 3 in string.values():
            trips += 1
    print(f"Doubles: {dubs} * Triples: {trips} = {dubs * trips}")   # 6696


def part_two(data):
    diffs = []
    for index, line in enumerate(data):
        for comp_line in data[index+1:]:
            if dld(line, comp_line) < 2:
                diffs.append((line, comp_line))
    # print("\n", diffs[0][0], "\n", diffs[0][1])
    # matching_chars = [char for char in diffs[0][0] if char in diffs[0][1]]
    # bvnfawcnyoeyudzrpgsleimtkj

    matching_chars = str()
    for index, char in enumerate(diffs[0][0]):
        if char == diffs[0][1][index]:
            matching_chars += char
    print(f"Matching Chars: {matching_chars}")  # bvnfawcnyoeyudzrpgslimtkj


if __name__ == "__main__":
    main()