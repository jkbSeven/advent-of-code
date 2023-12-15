def parseLine(line: str) -> int:
    dividedLine = line.split(" | ")
    winningNumbersString = dividedLine[0].split(": ")[1]
    winningNumbers = [int(number) for number in winningNumbersString.split()]
    elfNumbers = [int(number) for number in dividedLine[1].split()]
    
    counter = 0
    for number in elfNumbers:
        if number in winningNumbers:
            if not counter:
                counter += 1
            else:
                counter *= 2

    return counter

def main():
    counter = 0
    with open("input.txt", "r") as file:
        for line in file:
            counter += parseLine(line)

    print(f"Total worth: {counter}")


if __name__ == "__main__":
    main()
