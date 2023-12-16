import re

def main():
    with open("input.txt", "r") as file:
        time = int("".join(re.findall(r"\d+", file.readline())))
        recordDistance = int("".join(re.findall(r"\d+", file.readline())))

    result = 0
    for holdingTime in range(1, time):
        if ((holdingTime * 1) * (time - holdingTime)) > recordDistance:
            result += 1

    print(f"Result: {result}")

if __name__ == "__main__":
    main()
        
