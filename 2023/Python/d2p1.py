import re

def regexParse(line: str, restrictions: dict, regex: re.Pattern) -> int:
    gameIndex = re.match(r"Game (\d+):", line).group(1)
    regexOutput = regex.findall(line)

    for entry in regexOutput:
        count, color = entry.split()
        if int(count) > restrictions[color]:
            return 0

    return int(gameIndex)

def main():
    restrictions = {
        "red": 12,
        "green": 13,
        "blue": 14
    }

    counter = 0
    regex = re.compile(r"\d+ \w+")
    with open("input.txt", "r") as file:
        for line in file:
            counter += regexParse(line, restrictions, regex)

    print(f"Total sum: {counter}")


if __name__ == "__main__":
    main()
