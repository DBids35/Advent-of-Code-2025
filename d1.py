from helper import filename_to_list_of_lines


def move(current_position: int, direction:str, steps:int) -> int:
    if direction == "L":
        return (current_position - steps) % 100
    elif direction == "R":
        return (current_position + steps) % 100
    else:
        raise ValueError(f"Invalid direction: {direction}")




def part1(lines: list[str]) -> int:
    current_position = 50
    zero_counter = 0
    for line in lines:
        direction = line[0]
        steps = int(line[1:])
        current_position = move(current_position, direction, steps)
        if current_position == 0:
            zero_counter += 1
    return zero_counter

def get_zero_crosses(start_position: int, direction: str, steps: int) -> int:
    crosses = steps//100
    if direction == "R" and (100 - start_position) <= (steps % 100) and start_position != 0:
        return crosses + 1
    elif direction == "L" and start_position <= (steps % 100) and start_position != 0:
        return crosses + 1
    return crosses

assert get_zero_crosses(50, "L", 68) == 1
assert get_zero_crosses(52, "R", 48) == 1
assert get_zero_crosses(95, "R", 60) == 1
assert get_zero_crosses(55, "L", 55) == 1
assert get_zero_crosses(99, "L", 99) == 1
assert get_zero_crosses(14, "L", 82) == 1

assert get_zero_crosses(82, "L", 30) == 0
assert get_zero_crosses(0, "L", 5) == 0
    
def part2(lines: list[str]) -> int:
    current_position = 50
    zero_counter = 0
    for line in lines:
        direction = line[0]
        steps = int(line[1:])
        zero_counter += get_zero_crosses(current_position, direction, steps)

        current_position = move(current_position, direction, steps)
    return zero_counter


if __name__ == "__main__":
    lines = filename_to_list_of_lines("d1.txt")
    print(part2(lines))