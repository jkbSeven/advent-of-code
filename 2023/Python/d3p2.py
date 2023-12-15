import string, re

def analyzeSurroundings(lines: list[str], linesCount:int, rowIndex: int, gearPosition: int, relativePositionsToCheck: tuple[tuple[int]], regexNumber: re.Pattern) -> int:
    if rowIndex == 0:
        relativePositionsToCheck = relativePositionsToCheck[3:]
        linesOfInterest = lines[:(rowIndex + 1) + 1]

    elif rowIndex == linesCount - 1:
        relativePositionsToCheck = relativePositionsToCheck[:5]
        linesOfInterest = lines[rowIndex - 1:]

    else:
        linesOfInterest = lines[rowIndex - 1:(rowIndex + 1) + 1]

    numbers = []
    for line in linesOfInterest:
        for regexOutput in regexNumber.finditer(line):
            for relativePosition in relativePositionsToCheck:
                # re.Match.end() is not inclusive, that's where the "-1" comes from
                if regexOutput.start() <= (gearPosition + relativePosition[1]) <= (regexOutput.end() - 1):
                    numbers.append(int(regexOutput.group(0)))
                    break

    if len(numbers) == 2:
        return numbers[0] * numbers[1]

    return 0

def main():
    regex = re.compile(r"\*")
    regexNumber = re.compile(r"(\d+)")
    relativePositionsToCheck =  ((-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)) # format: (relative_row, relative_column)

    with open("input.txt", "r") as file:
        lines = file.readlines()
        linesCount = len(lines)

    counter = 0
    for index, value in enumerate(lines):
        for regexOutput in regex.finditer(value):
            counter += analyzeSurroundings(lines, linesCount, index, regexOutput.start(), relativePositionsToCheck, regexNumber)

    print(f"The sum of all of the part numbers in the engine schematic: {counter}")


if __name__ == "__main__":
    main()
