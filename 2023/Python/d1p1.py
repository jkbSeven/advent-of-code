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

def main():
    finalValue = 0
    with open("input.txt", "r") as file:
        for line in file:
            finalValue += findCalibrationValue(line)

    print(f"The sum of all of the calibration values is equal to {finalValue}")


if __name__ == "__main__":
    main()

