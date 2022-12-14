def main():
    with open("3/input.txt") as f:
        sum_priority = 0

        for line in f.readlines():
            line = line.strip()
            middle = len(line) // 2

            first, second = line[:middle], line[middle:]
            if len(first) != len(second):
                raise Exception("parts has different sizes")
            first = set(c for c in first)
            second = set(c for c in second)

            common = first & second
            if len(common) > 1:
                raise Exception("more then one failures")

            c = common.pop()
            if c.isupper():
                priority = ord(c) - ord("A") + 27
            else:
                priority = ord(c) - ord("a") + 1

            sum_priority += priority

        print(sum_priority)



if __name__ == "__main__":
    main()
