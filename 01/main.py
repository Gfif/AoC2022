
def first():
    with open("1/input.txt") as f:
        max_calroies = 0

        current_calories = 0
        for line in f.readlines():
            line = line.strip()

            if line:
                current_calories += int(line)
            else:
                max_calroies = max(current_calories, max_calroies)
                current_calories = 0


    print(max_calroies)

def second():
    with open("1/input.txt") as f:
        callories = []

        current_calories = 0
        for line in f.readlines():
            line = line.strip()

            if line:
                current_calories += int(line)
            else:
                callories.append(current_calories)
                current_calories = 0

    callories.sort(key=lambda x: -x)

    print(callories)
    print(sum(callories[:3]))


def main():
    second()


if __name__ == "__main__":
    main()
