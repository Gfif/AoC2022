FILE = "10/input.txt"




def main():

    with open(FILE) as f:

        x = 1
        cycles = [x,]

        for line in f:
            line = line.strip()
            parts = line.split(" ")

            cmd = parts[0]
            value = None
            if len(parts) > 1:
                value = int(parts[1])

            if cmd == "noop":
                cycles.append(x)
            elif cmd == "addx":
                cycles.append(x)
                x += value
                cycles.append(x)

        for i in range(6):
            res = ""
            for i, c in enumerate(cycles[i * 40: (i + 1) * 40]):
                if i in range(c - 1, c + 2):
                    res += "#"
                else:
                    res += "."
            print(res)

        # return sum(i * cycles[i-1] for i in (20, 60, 100, 140, 180, 220))


if __name__ == "__main__":
    print(main())

