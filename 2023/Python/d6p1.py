import re

def main():
    with open("input.txt", "r") as file:
        times = list(map(int, re.findall(r"\d+", file.readline())))
        distances = list(map(int, re.findall(r"\d+", file.readline())))

    result = 1
    races = zip(times, distances)
    for time, recordDistance in races:
        winCases = 0
        for holdingTime in range(1, time):
            if ((holdingTime * 1) * (time - holdingTime)) > recordDistance:
                winCases += 1
        if winCases:
            result *= winCases

    print(f"Result: {result}")

if __name__ == "__main__":
    main()
        
