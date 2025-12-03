from operator import indexOf
from helper import filename_to_list_of_lines

def batery_bank_to_next_num(battery_bank: list[int], remaining_digits: int) -> int:
    if remaining_digits == 1:
        return max(battery_bank)
    else:
        return max(battery_bank[:-(remaining_digits-1)])

def battery_bank_to_joltage(battery_bank: list[int]) -> int:
    battery_joltage = 0
    for i in range(12, 0, -1):
        next_num = batery_bank_to_next_num(battery_bank, i)
        battery_bank = battery_bank[indexOf(battery_bank, next_num) + 1:]
        battery_joltage += next_num * 10 ** (i-1)
    return battery_joltage

def part1(input: list[str]) -> int:
    # convert list of strings to list of lists of integers
    input = [list(map(int, list(line))) for line in input]
    total = 0
    for battery_bank in input:
        battery_joltage = battery_bank_to_joltage(battery_bank)
        total += battery_joltage
    return total

def part2(input: list[str]) -> int:
    return 0

if __name__ == "__main__":
    lines = filename_to_list_of_lines("d3.txt")
    print(part1(lines))
    # print(part2(lines))
