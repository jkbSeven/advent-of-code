import re

def findCalibrationValue(line: str) -> int:
    first = None
    last = None

    for char in line:
        if first is None and char.isdigit():
            first = int(char)
        elif char.isdigit():
            last = int(char)

    if last is None:
        last = first

    return (10 * first) + last

def parseLine(line: str, regex: re.Pattern, substitutions: dict) -> str:
    original = line
    regexOutput = regex.search(line)
    while regexOutput is not None:
        value = regexOutput.group(0)
        line = line.replace(value, substitutions[value], 1)
        regexOutput = regex.search(line)

    return line

def main():
    regex = re.compile(r"(one|two|three|four|five|six|seven|eight|nine)")
    substitutions = {
        "one": "o1e",
        "two": "t2o",
        "three": "th3ee",
        "four": "fo4r",
        "five": "fi5e",
        "six": "s6x",
        "seven": "se7en",
        "eight": "ei8ht",
        "nine": "ni9e"
    }
    with open("input.txt", "r") as file:
        finalValue = 0
        for line in file:
            line = parseLine(line, regex, substitutions)
            finalValue += findCalibrationValue(line)

    print(f"The sum of all of the calibration values is equal to {finalValue}")


if __name__ == "__main__":
    main()
