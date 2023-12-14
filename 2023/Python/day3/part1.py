import string, re

def isSurrounded(lines: list[str], linesCount:int, rowIndex: int, numberStart: int, numberEnd: int, relativePositionsToCheck: tuple[tuple[int]]) -> bool:
    if rowIndex == 0:
        relativePositionsToCheck = relativePositionsToCheck[3:]
    elif rowIndex == linesCount - 1:
        relativePositionsToCheck = relativePositionsToCheck[:5]

    # re.Match.end() is not inclusive so there is no need to add 1 to numberEnd
    for digitIndex in range(numberStart, numberEnd):
        for relative_row, relative_column in relativePositionsToCheck:
            try:
                char = lines[rowIndex + relative_row][digitIndex + relative_column]
            except IndexError:
                continue
            else:
                if char != "." and char in string.punctuation:
                    return True

    return False

def main():
    regex = re.compile(r"(\d+)")
    relativePositionsToCheck =  ((-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)) # format: (relative_row, relative_column)

    with open("input.txt", "r") as file:
        lines = file.readlines()
        linesCount = len(lines)

    counter = 0
    for index, value in enumerate(lines):
        regexOutput = regex.search(value)
        while regexOutput is not None:
            if isSurrounded(lines, linesCount, index, *regexOutput.span(), relativePositionsToCheck):
                counter += int(regexOutput.group(0))
            regexOutput = regex.search(value, regexOutput.end())

    print(f"The sum of all of the part numbers in the engine schematic: {counter}")


if __name__ == "__main__":
    main()
