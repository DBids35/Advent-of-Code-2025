from helper import filename_to_list_of_lines

def part1(clean_lines: list[list[str]]) -> int:
    total = 0
    # for all columns, iterate through the rows, and perform the operation on the two numbers
    for i in range(len(clean_lines[0])):
        multiply = False
        add = False
        nums = []
        # iterate through the rows, and perform the operation on the two numbers
        for j in range(len(clean_lines)):
            if clean_lines[j][i] == "*":
                multiply = True
            elif clean_lines[j][i] == "+":
                add = True
            else:
                nums.append(int(clean_lines[j][i]))
        temp_total = nums[0]
 
        for num in nums[1:]:
            if multiply:
                temp_total = temp_total * num
            elif add:
                temp_total += num
        print(temp_total)
        total += temp_total
    return total

def part2_parse(lines: list[str]) -> list[list[str]]:
    operators = lines[-1]
    lines = lines[:-1]
    clean_lines = []
    op_idxs = [i for i, x in enumerate(operators) if x != " "]
    # print(op_idxs)
    for line in lines:
        clean_line = []
        prev = 0
        for idx in op_idxs:
            if idx != 0:
                # print(idx)
                clean_line.append(line[prev:idx-1])
                #print(clean_line)
                prev = idx
        clean_line.append(line[prev:])
        #print(clean_line)
        clean_lines.append(clean_line)
    operators = [x for x in operators if x != " "]
    return clean_lines, operators

def part2(lines: list[list[str]], operators: list[str]) -> int:
    # print(lines)
    # translate lines of rows to columns
    rotated = list(zip(*lines[::-1]))
    double_rotated = []
    for col in rotated:
        double_rotated.append(list(zip(*col[::-1])))
    # print(double_rotated)
    total = 0
    for i, row in enumerate(double_rotated):
        row = [int("".join(val)) for val in row]
        print(row)
        temp_total = row[0]
        for num in row[1:]:
            if operators[i] == "*":
                temp_total = temp_total * num
            elif operators[i] == "+":
                temp_total += num
        total += temp_total
        print(temp_total)
    print(total)
        
    return 0

if __name__ == "__main__":
    with open(f"inputs/d6.txt", 'r') as file:
        lines = [line.rstrip("\n") for line in file.readlines()]
    lines, operators = part2_parse(lines)
    # print(lines)
    # print(part1(clean_lines))
    print(part2(lines, operators))