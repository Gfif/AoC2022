def main():
    with open("3/input.txt") as f:
        sum_priority = 0

        threesome = []
        for line in f.readlines():
            line = line.strip()

            threesome.append(set(c for c in line))

            if len(threesome) < 3:
                continue

            common = threesome[0] & threesome[1] & threesome[2]
            
            if len(common) > 1:
                raise Exception("more then one failures")

            c = common.pop()
            if c.isupper():
                priority = ord(c) - ord("A") + 27
            else:
                priority = ord(c) - ord("a") + 1

            sum_priority += priority
            threesome = []

        print(sum_priority)



if __name__ == "__main__":
    main()
