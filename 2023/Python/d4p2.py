def parseLine(line: str, rounds: dict) -> int:
    dividedLine = line.split(" | ")
    gameNumberString, winningNumbersString = dividedLine[0].split(": ")
    gameNumber = int(gameNumberString.split()[1])
    winningNumbers = [int(number) for number in winningNumbersString.split()]
    elfNumbers = [int(number) for number in dividedLine[1].split()]

    counter = 0
    for number in elfNumbers:
        if number in winningNumbers:
            counter += 1
    
    for next in range(1, counter + 1):
        nextCardIndex = gameNumber + next
        if nextCardIndex <= 186:
            rounds[nextCardIndex] += rounds[gameNumber]


def main():
    rounds = {x: 1 for x in range(1, 187)}

    with open("input.txt", "r") as file:
        for line in file:
            parseLine(line, rounds)

    print(f"Total worth: {sum(rounds.values())}")


if __name__ == "__main__":
    main()

