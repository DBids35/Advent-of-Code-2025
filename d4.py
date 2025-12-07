from helper import filename_to_list_of_lines, list_of_lines_to_list_of_lists


def grid_spot_checker(grid: list[list[str]], i: int, j: int) -> bool:
    
    if grid[i][j] == ".":
        return False
    # print(f"Checking spot {i}, {j}")
    # count rolls of paper adjacent to the spot
    # if the count is < 4 return True
    adjacent_rolls = 0
    for k in range(-1, 2):
        if 0 <= i + k  < len(grid):
            for l in range(-1,2):
                if 0 <= j + l  < len(grid[i + k ]):
                    if not (k == 0 and l == 0):
                        if grid[i + k ][j + l] == "@":
                            adjacent_rolls += 1
    if adjacent_rolls < 4:
        return True
        
    return False

def part1(grid: list[list[str]]) -> int:
    movable_rolls = []
    for i in range(len(grid)):
        for j in range(len(grid[i])):
            if grid_spot_checker(grid, i, j):
                movable_rolls.append((i, j))
    return movable_rolls

def part2(grid: list[list[str]]) -> int:
    
    previous_moved_rolls = -1
    moved_rolls = 0
    while moved_rolls > previous_moved_rolls:
        newly_moved_rolls = part1(grid)
        for roll in newly_moved_rolls:
            grid[roll[0]] = grid[roll[0]][:roll[1]] + "." + grid[roll[0]][roll[1]+1:]
        previous_moved_rolls = moved_rolls
        moved_rolls += len(newly_moved_rolls)
        
    return moved_rolls


if __name__ == "__main__":
    lines = filename_to_list_of_lines("d4.txt")
    grid = list_of_lines_to_list_of_lists(lines)
    # print(len(part1(grid)))
    print(part2(lines))