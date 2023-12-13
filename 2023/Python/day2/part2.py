import re

def regexParse(line: str, regex: re.Pattern) -> int:
    gameIndex = re.match(r"Game (\d+):", line).group(1)
    regexOutput = regex.findall(line)

    required = {
        "red": 0,
        "green": 0,
        "blue": 0
    }

    for entry in regexOutput:
        count, color = entry.split()
        count = int(count)
        if count > required[color]:
            required[color] = count

    return required["red"] * required["green"] * required["blue"]

def main():
    counter = 0
    regex = re.compile(r"\d+ \w+")

    with open("input.txt", "r") as file:
        for line in file:
            counter += regexParse(line, regex)

    print(f"Total: {counter}")


if __name__ == "__main__":
    main()
