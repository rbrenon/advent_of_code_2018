from collections import Counter


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
    print(f"doubles: {dubs} * triples: {trips} = {dubs * trips}")   # 6696


def part_two(data):
    pass


if __name__ == "__main__":
    main()