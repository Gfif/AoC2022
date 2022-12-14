def first():

    shape_points = {
        "Rock": 1,
        "Paper": 2,
        "Scissors": 3,
    }

    outcome_points = {
        "win": 6,
        "draw": 3,
        "lose": 0,
    }

    shape_mapping = {
        "A": "Rock",
        "B": "Paper",
        "C": "Scissors",
        "X": "Rock",
        "Y": "Paper",
        "Z": "Scissors",
    }

    win_results = (
        ("Rock", "Paper"), ("Paper", "Scissors"), ("Scissors", "Rock"),
    )

    with open("2/input.txt") as f:
        score = 0

        for line in f.readlines():
            line = line.strip()
            shapes = tuple(shape_mapping[x] for x in line.split())

            if len(shapes) != 2:
                raise Exception("No!")

            if shapes[0] == shapes[1]:
                result = "draw"
            elif shapes in win_results:
                result = "win"
            else:
                result = "lose"

            score += outcome_points[result]
            score += shape_points[shapes[1]]

        print(score)


def last():
    shape_points = {
        "Rock": 1,
        "Paper": 2,
        "Scissors": 3,
    }

    outcome_points = {
        "win": 6,
        "draw": 3,
        "lose": 0,
    }

    shape_mapping = {
        "A": "Rock",
        "B": "Paper",
        "C": "Scissors",
    }

    result_mapping = {
        "X": "lose",
        "Y": "draw",
        "Z": "win",
    }

    win_results = dict((
        ("Rock", "Paper"), ("Paper", "Scissors"), ("Scissors", "Rock"),
    ))

    lose_results = dict((v, k) for k, v in win_results.items())

    with open("2/input.txt") as f:
        score = 0

        for line in f.readlines():
            line = line.strip()
            parts = line.split()
            if len(parts) != 2:
                raise Exception("No!")

            opponent_shape = shape_mapping[parts[0]]
            result = result_mapping[parts[1]]

            if result == "draw":
                my_shape = opponent_shape
            elif result == "win":
                my_shape = win_results[opponent_shape]
            else:
                my_shape = lose_results[opponent_shape]
            score += outcome_points[result]
            score += shape_points[my_shape]

        print(score)

def main():
    last()


if __name__ == "__main__":
    main()
