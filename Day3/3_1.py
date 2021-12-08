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
    gammaRate = []
    epsilonRate = []
    maxIndex = len(input[0])

    while index < maxIndex:
        onesCount = zeroesCount = 0
        for row in input:
            if row[index] == 0:
                zeroesCount += 1
            else:
                onesCount += 1

        if onesCount > zeroesCount:
            gammaRate.append(1)
            epsilonRate.append(0)
        else:
            gammaRate.append(0)
            epsilonRate.append(1)

        index += 1
    
    return [gammaRate, epsilonRate]
    
def convertBinary(binaryRates):
    gammaBin = binaryRates[0]
    epsilonBin = binaryRates[1]
    arrayLen = len(gammaBin)
    gammaDec = epsilonDec = 0
    binaryCounter = 1

    while arrayLen > 0:
        gammaDec += (gammaBin.pop(-1) * binaryCounter)
        epsilonDec += (epsilonBin.pop(-1) * binaryCounter)
        binaryCounter *= 2
        arrayLen -= 1

    print(gammaDec * epsilonDec)

if __name__ == "__main__":
    fileVal = readFile()
    binaryRates = parseData(fileVal)
    convertBinary(binaryRates)