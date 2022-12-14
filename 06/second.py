def add_char(d, key):
    if key in d:
        d[key] += 1
    else:
        d[key] = 1


def rm_char(d, key):
    if key not in d:
        raise Exception("Some Error!")
    
    d[key] -= 1
    if d[key] == 0:
        del d[key]


def main():
    l = 14
    with open("6/input.txt") as f:
        line = f.readline()

        d = {}
        for i in range(l):
            add_char(d, line[i])

        for i in range(len(line) - l):
            if len(d) == l:
                return i + l
            
            rm_char(d, line[i])
            add_char(d, line[i + l])
            
        raise Exception("Some Error!")

if __name__ == "__main__":
    print(main())
