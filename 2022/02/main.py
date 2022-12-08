lookup_opp = {
    "A": "Rock",
    "B": "Paper",
    "C": "Scissors",
}

lookup_self = {
    "X": "Rock",
    "Y": "Paper",
    "Z": "Scissors",
}

point_shape = {
    "Rock": "1",
    "Paper": "2",
    "Scissors": "3",
}

point_outcome = {
    "lose": "0",
    "win": "6",
    "draw": "3",
}


def total_score(shape, outcome) -> int:
    """Return the total score of a shape and outcome."""
    shape = lookup_shape(shape, shape)[1]  # get the shape of self
    return int(point_shape[shape]) + int(point_outcome[outcome])


def is_win(opp, self) -> bool:
    """Return True if self wins against opp."""
    if lookup_self[self] == "Rock" and lookup_opp[opp] == "Scissors":
        return True
    elif lookup_self[self] == "Paper" and lookup_opp[opp] == "Rock":
        return True
    elif lookup_self[self] == "Scissors" and lookup_opp[opp] == "Paper":
        return True
    else:
        return False


def is_draw(opp, self) -> bool:
    """Return True if self and opp are the same shape."""
    if lookup_self[self] == lookup_opp[opp]:
        return True
    else:
        return False


def get_outcome(opp, self) -> str:
    """Return the outcome of a game."""
    if is_win(opp, self):
        return "win"
    elif is_draw(opp, self):
        return "draw"
    else:
        return "lose"


def get_score(opp, self) -> int:
    """Return the score of a game."""
    outcome = get_outcome(opp, self)
    return total_score(self, outcome)


def lookup_shape(opp, self) -> tuple:
    """Return the shape of self and opp."""
    opp = lookup_opp.get(opp, None)
    self = lookup_self.get(self, None)
    return (opp, self)


with open("input.txt", "r") as file:
    data = file.read()
    lines = data.splitlines()

    total = 0
    for line in lines:
        opp = line[0]
        self = line[2]
        outcome = get_outcome(opp, self)
        score = get_score(opp, self)
        total += score
        print(f"{opp} vs {self} = {outcome} :: {score}")
    print(f"total score: {total}")

