from helper import filename_to_list_of_lines


def minimize_ranges(ranges: list[str]) -> list[str]:
    # sort the ranges by start
    ranges = sorted(ranges, key=lambda x: int(x.split("-")[0]))
    ranges = [[int(x.split("-")[0]), int(x.split("-")[1])] for x in ranges]

    final_ranges = []
    final_ranges.append(ranges[0])
    # iterate through the ranges
    # if the start of the current range is less than the end of the previous range, combine them
    # if the start of the current range is greater than the end of the previous range, add the current range to the final ranges
    for i in range(1, len(ranges)):
        if int(ranges[i][0]) <= final_ranges[-1][1]:
            if int(ranges[i][1]) > final_ranges[-1][1]:
                final_ranges[-1] = [final_ranges[-1][0], ranges[i][1]]
        else:
            final_ranges.append([ranges[i][0], ranges[i][1]])
    
    return final_ranges
  

def part1(ranges: list[str], ids: list[str]) -> int:
    ranges = minimize_ranges(ranges)
    # print(ranges)

    # sort ids
    ids = sorted(ids, key=lambda x: int(x))
    ids = [int(id) for id in ids]

    start_index = 0
    fresh_ingredients = set()

    for fresh_range in ranges:
        for i in range(start_index, len(ids)):
            # if the id is less than the start of the fresh range, continue
            if ids[i] < fresh_range[0]:
                continue
            # else if the idea is contained in the fresh range, add it to the fresh ingredients
            elif ids[i] <= fresh_range[1]:
                fresh_ingredients.add(ids[i])

            # else if the id is greater than the end of the fresh range, move to the next fresh range
            elif ids[i] > fresh_range[1]:
                start_index = i
                break
            
    return len(fresh_ingredients)

def part2(ranges: list[str]) -> int:
    ranges = minimize_ranges(ranges)
    total_possible_fresh_ingredients = 0
    for fresh_range in ranges:
        total_possible_fresh_ingredients += fresh_range[1] - fresh_range[0] + 1
    return total_possible_fresh_ingredients

if __name__ == "__main__":
    lines = filename_to_list_of_lines("d5.txt")
    # lines is a list of strings, I want to split it into two lists, separated by the blank line
    ranges = lines[:lines.index("")]
    ids = lines[lines.index("")+1:]
    # print(part1(ranges, ids))
    print(part2(ranges))