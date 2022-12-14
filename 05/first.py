def main():
    with open("5/input.txt") as f:

        stacks = []
        for line in f:
            if line.startswith(" 1"):
                break

            for i in range(len(line) // 4):
                crate = line[i * 4 + 1]
                if len(stacks) < i + 1:
                    stacks.append([])
                if crate != " ":
                    stacks[i].append(crate)

        for i, stack in enumerate(stacks):
            stack.reverse()

        f.readline()

        for line in f:
            line = line.strip()
            parts = line.split(" ")

            cnt = int(parts[1])
            src = int(parts[3])
            dst = int(parts[5])

            crates = stacks[src - 1][-cnt:]
            stacks[src - 1] = stacks[src - 1][:-cnt]
            stacks[dst - 1] += crates

        result = "".join(stack.pop() for stack in stacks)

        return result


if __name__ == "__main__":
    print(main())
