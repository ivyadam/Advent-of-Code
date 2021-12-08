def readFile():
    file = open('./Day3/data3.txt','r')
    output = []
    while file:
        tempList = []
        line = file.readline()
        if not line:
            break
        
        if line.endswith('\n'):
            line = line[:-1]

        for num in line:
            tempList.append(int(num))
        
        output.append(tempList)

    file.close()
    return output

def parseData(input):
    index = 0
    oxygenRating = findRating(input, index, "oxygen")
    co2Rating = findRating(input, index, "co2")
    return [oxygenRating[0], co2Rating[0]]
    
def findRating(input, currIndex, ratingType):
    onesCount = zeroesCount = 0
    onesArray = []
    zeroesArray = []
    for row in input:
        if row[currIndex] == 0:
            zeroesCount += 1
            zeroesArray.append(row)
        else:
            onesCount += 1
            onesArray.append(row)

    if ratingType == "oxygen":
        if onesCount >= zeroesCount:
            if len(onesArray) == 1:
                return onesArray
            else:
                return findRating(onesArray, currIndex + 1, ratingType)
        else:
            if len(zeroesArray) == 1:
                return zeroesArray
            else:
                return findRating(zeroesArray, currIndex + 1, ratingType)
    else:
        if zeroesCount <= onesCount:
            if len(zeroesArray) == 1:
                return zeroesArray
            else:
                return findRating(zeroesArray, currIndex + 1, ratingType)
        else:
            if len(onesArray) == 1:
                return onesArray
            else:
                return findRating(onesArray, currIndex + 1, ratingType)
    
def convertBinary(binaryRates):
    oxygenRate = binaryRates[0]
    co2Rate = binaryRates[1]
    arrayLen = len(oxygenRate)
    oxygenDec = co2Dec = 0
    binaryCounter = 1

    while arrayLen > 0:
        oxygenDec += (oxygenRate.pop(-1) * binaryCounter)
        co2Dec += (co2Rate.pop(-1) * binaryCounter)
        binaryCounter *= 2
        arrayLen -= 1

    print(oxygenDec * co2Dec)

if __name__ == "__main__":
    fileVal = readFile()
    binaryRates = parseData(fileVal)
    convertBinary(binaryRates)