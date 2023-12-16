# DISCLAIMER:
# This code is insanely ugly and inefficient, I don't take any responsibilty for damage caused by reading it
# I'm gonna rewrite this some other day (part 1 as well)
# This puzzle made me lose my sanity


import re

def locateRange(value: int, propertyRanges: list[tuple[int]]) -> int | None:
    for index, propertyRange in enumerate(propertyRanges):
        if propertyRange[0] <= value <= propertyRange[1]:
            return index
    return None


def validLocation(location: int, propertiesRanges: dict) -> bool:
    seedProperties = {"location": location}
    for propertyIndex, property in enumerate(list(propertiesRanges.items())[:0:-1]):
        propertyName, rangesPair = property
        previousPropertyValue = list(seedProperties.values())[-1]
        index = locateRange(previousPropertyValue, rangesPair[1])

        if index is not None:
            offset = previousPropertyValue - rangesPair[1][index][0]
            next = rangesPair[0][index][0] + offset

        else:
            next = previousPropertyValue

        nextKey = list(propertiesRanges)[-2 - propertyIndex]
        seedProperties[nextKey] = next

    if (index:=locateRange(seedProperties["soil"], propertiesRanges["soil"][1])) is not None:
        offset = seedProperties["soil"] - propertiesRanges["soil"][1][index][0]
        seed = propertiesRanges["soil"][0][index][0] + offset
    else:
        seed = propertiesRanges["soil"]

    for seedRange in propertiesRanges["seed"]:
        if seedRange[0] <= seed <= seedRange[1]:
            return True

    return False


def main():
    regexMap = re.compile(r"(\w+)-to-(\w+)")
    regexMapProperties = re.compile(r"(\d+)\s+(\d+)\s+(\d+)")
    propertiesRanges = {"seed": []}

    with open("input.txt", "r") as file:
        seedsLine = file.readline()

        for regexOutput in re.finditer(r"(\d+) (\d+)", seedsLine):
            start, length = list(map(int, regexOutput.groups()))
            propertiesRanges["seed"].append((start, start + length))

        for line in file:
            if (regexMapOutput:=regexMap.search(line)) is not None:
                sourceName, destinationName = regexMapOutput.groups()
                sourceRanges = []
                destinationRanges = []
                
                for mappingLine in file:
                    if (regexPropertiesOutput:=regexMapProperties.search(mappingLine)) is not None:
                        destination, source, mapRange = list(map(int, regexPropertiesOutput.groups()))

                        # first element in sourceRanges corresponds to first element in destinationRanges
                        sourceRanges.append((source, source + mapRange))
                        destinationRanges.append((destination,  destination + mapRange))
                    else:
                        break

                propertiesRanges[destinationName] = [sourceRanges, destinationRanges]

    sortedLocations = sorted(propertiesRanges["location"][1], key=(lambda x: x[0]))
    for locationRange in sortedLocations:
        for location in range(*locationRange):
            if validLocation(location, propertiesRanges):
                print(f"The lowest location number that corresponds to any of the initial seed numbers: {location}")
                return 0


if __name__ == "__main__":
    main()

