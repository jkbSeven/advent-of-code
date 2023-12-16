import re

def main():
    regexMap = re.compile(r"(\w+)-to-(\w+)")
    regexMapProperties = re.compile(r"(\d+)\s+(\d+)\s+(\d+)")
    with open("input.txt", "r") as file:
        seedsLine = file.readline()
        seeds = {int(regexOutput.group(0)): {"seed": int(regexOutput.group(0))} for regexOutput in re.finditer(r"(\d+)", seedsLine)}
        
        for line in file:
            if (regexMapOutput:=regexMap.search(line)) is not None:
                sourceName, destinationName = regexMapOutput.groups()
                sourceRanges = []
                destinationRanges = []
                
                for mappingLine in file:
                    if (regexPropertiesOutput:=regexMapProperties.search(mappingLine)) is not None:
                        destination, source, mapRange = list(map(int, regexPropertiesOutput.groups()))

                        # first element in sourceRanges corresponds to first element in destinationRanges
                        sourceRanges.append((source, source + mapRange - 1))
                        destinationRanges.append((destination,  destination + mapRange - 1))
                    else:
                        break

                for seed, properties in seeds.items():
                    previuosPropertyValue = list(seeds[seed].values())[-1]
                    for index, sourceRange in enumerate(sourceRanges):
                        if sourceRange[0] <= previuosPropertyValue <= sourceRange[1]:
                            offset = previuosPropertyValue - sourceRange[0]
                            properties[destinationName] = destinationRanges[index][0] + offset
                    properties[destinationName] = properties.get(destinationName, previuosPropertyValue)

    minLocation = seeds[list(seeds)[0]]["location"]
    for properties in seeds.values():
        if (newMinimum:=properties["location"]) < minLocation:
            minLocation = newMinimum

    print(f"The lowest location number that corresponds to any of the initial seed numbers: {minLocation}")
                

if __name__ == "__main__":
    main()
