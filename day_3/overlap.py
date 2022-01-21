

def main():
    with open("input.txt") as file:
        raw_input = file.read().splitlines()

    part_one(raw_input, 1000)
    part_two(raw_input, 1000)


def part_one(data: list, dims: int = 10) -> None:
    fabric = [[0 for _ in range(dims)] for _ in range(dims)]
    for line in data:
        line = line.split()

        # claim_id = row_data[0].split('#')[1]
        col, row = int(line[2].split(",")[0]), int(line[2].split(",")[1][:-1])
        width, height = int(line[3].split("x")[0]), int(line[3].split("x")[1])

        for col_index in range(col, col+width):
            for row_index in range(row, row+height):
                fabric[row_index][col_index] += 1

    gt_1 = 0

    for row in fabric:
        for col in row:
            if col > 1:
                gt_1 += 1

    print(gt_1)     # 104126


def part_two(data: list, dims: int = 10) -> None:
    fabric = [[0 for _ in range(dims)] for _ in range(dims)]
    claims = {}
    for line in data:
        line = line.split()

        claim_id = int(line[0].split('#')[1])
        col, row = int(line[2].split(",")[0]), int(line[2].split(",")[1][:-1])
        width, height = int(line[3].split("x")[0]), int(line[3].split("x")[1])
        claims[claim_id] = [(col, col+width), (row, row + height), width * height]

    full_claim = []
    for claim in claims.keys():
        full_claim.append(claim)
        for col_index in range(claims[claim][0][0], claims[claim][0][1]):
            for row_index in range(claims[claim][1][0], claims[claim][1][1]):
                if fabric[row_index][col_index] > 0:
                    try:
                        full_claim.pop(full_claim.index(claim))
                        full_claim.pop(full_claim.index(fabric[row_index][col_index]))
                    except:
                        pass
                fabric[row_index][col_index] = claim

    print(full_claim)
    for claim in full_claim:
        no_claims = 0
        for row in fabric:
            for col in row:
                if col == claim:
                    no_claims += 1
        if no_claims == claims[claim][2]:
            print(f"matching claim count: {claim}")     # 695


if __name__ == "__main__":
    main()
