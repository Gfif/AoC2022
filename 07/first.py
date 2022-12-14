from collections import defaultdict


def main():
    with open("7/input.txt") as f:
        current_path = []
        sizes = defaultdict(lambda: 0)

        for line in f:
            line = line.strip()
            parts = line.split()

            if parts[1] == "cd":
                if parts[2] == "/":
                    current_path = []
                elif parts[2] == "..":
                    current_path.pop()
                else:
                    current_path.append(parts[2])
            elif parts[1] == "ls":
                print(f"LIST {current_path}")
                # TODO: read all input here
            else:
                parts = line.split()
                if parts[0] == "dir":
                    pass
                else:
                    size = int(parts[0])
                    sizes["/".join(current_path)] += size             
                    for i in range(len(current_path)):
                        path = "/".join(current_path[:i])
                        sizes[path] += size
        
        print(dict(sizes))

        unused_space = 70000000 - sizes[""]
        need_space = 30000000 - unused_space

        print(sizes[""])
        print(unused_space)
        print(need_space)

        fit_sizes = [v for v in sizes.values() if v > 30000000 - unused_space]
        print(fit_sizes)

        return min(fit_sizes)


if __name__ == "__main__":
    print(main())
