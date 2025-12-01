def filename_to_list_of_lines(filename: str) -> list[str]:
    with open(f"inputs/{filename}", 'r') as file:
        return [line.strip() for line in file.readlines()]

if __name__ == "__main__":
    print(filename_to_list_of_lines("d1.txt"))