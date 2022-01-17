

def main():
    with open('input.txt') as file:
        raw_input = file.read().splitlines()
    part_one(raw_input)
    part_two(raw_input)


def part_one(input: list) -> None:
    freq = 0
    for line in input:
        freq += int(line)

    print(f"Part one: {freq}")  # 497


def part_two(input: list) -> None:
    freq = {}
    frequency = 0
    repeat = True
    while repeat:
        for line in input:
            frequency += int(line)
            # print(frequency)
            if frequency in freq.keys():
                print(f"Part two: {frequency}")     # 558
                repeat = False
                break
            else:
                freq[frequency] = 1
                # -10
        # print(len(freq))


if __name__ == "__main__":
    main()