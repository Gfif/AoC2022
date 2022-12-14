def range_len(_range):
    return _range[1] - _range[0] + 1


def main():
    with open("4/input.txt") as f:
        count = 0
        for line in f.readlines():
            range1, range2 = tuple(
                x.split("-") for x in line.strip().split(",")
            )
            range1 = tuple(map(int, range1))
            range2 = tuple(map(int, range2))

            intersection = (max(range1[0], range2[0]), min(range1[1], range2[1]))

            if intersection == range1 or intersection == range2:
                count += 1

    return count
        


if __name__ == "__main__":
    print(main())
