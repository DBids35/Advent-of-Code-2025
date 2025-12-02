from helper import filename_to_list_of_lines

def part1(input: list[str]) -> int:
    invalid_sum = 0
    for string_range in input:
        for num in range(int(string_range.split("-")[0]), int(string_range.split("-")[1]) + 1):
            digits = len(str(num))
            if digits % 2 == 0:
                if int(str(num)[:digits//2]) == int(str(num)[digits//2:]):
                    invalid_sum += num
    return invalid_sum

def check_if_first_n_characters_repeat(num: int, n: int) -> bool:
    # check if the first n digits repeat any number of times
    # for example, num is 131313, n is 3
    # digits is 6
    digits = len(str(num))
    # if digits is less than n, return False
    if digits <= n:
        return False
    # if n isn't a factor of digits, return False
    if digits % n != 0:
        return False
    # digits // n (6//3 = 2) 
    # [0, 1]
    for i in range(digits // n):
        if str(num)[i*n:(i+1)*n] != str(num)[:n]:
            return False
    return True

assert check_if_first_n_characters_repeat(131313, 3) == False
assert check_if_first_n_characters_repeat(131313, 2) == True
assert check_if_first_n_characters_repeat(131313, 1) == False
assert check_if_first_n_characters_repeat(565656, 2) == True

def part2(input: list[str]) -> int:
    invalid_sum = 0
    for string_range in input:
        for num in range(int(string_range.split("-")[0]), int(string_range.split("-")[1]) + 1):
            # check if the first n charaters repeat
            # ns to check are the factors of the number of digits
            # ex: 1 for 2 digits, 1 for 3 digits, 2 for 4 digits, 1 for 5 digits, 2 and 3 for 6 digits, etc.
            digits = len(str(num))
            # check all the digits from 1 to the number of digits
            invalid = False
            for i in range(digits):
                if check_if_first_n_characters_repeat(num, i+1):
                    invalid = True
                    break
            if invalid:
                invalid_sum += num
    return invalid_sum

if __name__ == "__main__":
    lines = filename_to_list_of_lines("d2.txt")
    input = lines[0].split(",")
    # print(part1(input))
    print(part2(input))