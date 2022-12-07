def open_file(file_name):
    """Open a file and return it's contents."""
    with open(file_name, "r") as file:
        return file.read()


def get_lines(file_contents):
    """Return a list of lines from a file."""
    return file_contents.splitlines()


def check_contents(lines):
    """Check the contents of a file."""
    elf_food = {}  # dictionary to store the food of each elf
    elf = 0  # elf is the current elf
    calories = 0  # total food of each elf

    for line in lines:
        try:
            # convert str to int
            line = int(line)
            calories += line
        # check if line is blank
        except ValueError:
            if line == "":
                elf_food[elf] = calories
                calories = 0  # reset total
                elf += 1  # move to next elf
    return elf_food


def find_largest(elf_food, num=1):
    """Print the key of the largest value in a dictionary."""
    top = {}
    for _ in range(num):
        largest_value = 0
        largest_key = 0
        for key in elf_food:
            if elf_food[key] > largest_value:
                largest_value = elf_food[key]
                largest_key = key
        top[largest_key] = largest_value
        del elf_food[largest_key]
    return top


def total_calories(top):
    """Return the total calories of the top n elves."""
    total = 0
    for key in top:
        total += top[key]
    return total


if __name__ == "__main__":
    file_contents = open_file("input.txt")
    lines = get_lines(file_contents)
    elf_food = check_contents(lines)
    top_three = find_largest(elf_food, 3)
    print(top_three)
    print(total_calories(top_three))
