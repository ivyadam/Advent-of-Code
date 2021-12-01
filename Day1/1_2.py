def readFile():
    file = open('./Day1/data1.txt','r')
    output = []
    while file:
        line = file.readline()
        if not line:
            break
        
        if line.endswith('\n'):
            line = line[:-1]
        output.append(line)

    file.close()
    return output

def parseData(input):
    counter = 0
    num1 = int(input[0])
    num2 = int(input[1])
    num3 = int(input[2])
    currVal = num1 + num2 + num3

    for inputVal in input[3:]:
        num1 = num2
        num2 = num3
        num3 = int(inputVal)
        sumVal = num1 + num2 + num3
        if sumVal > currVal:
            counter += 1
        currVal = sumVal
    
    print(counter)

if __name__ == "__main__":
    fileVal = readFile()
    parseData(fileVal)