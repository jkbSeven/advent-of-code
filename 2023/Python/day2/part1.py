import re

def regexParse(line: str, restrictions: dict) -> int:
    gameIndex = re.match(r"Game (\d+):", line).group(1)
    regex = re.compile(r"\d+ \w+")
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
    with open("input.txt", "r") as file:
        for line in file:
            counter += regexParse(line, restrictions)

    print(f"Total sum: {counter}")


if __name__ == "__main__":
    main()
