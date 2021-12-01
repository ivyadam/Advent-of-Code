def readFile():
    file = open('./Day1/test1.txt','r')
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
    currVal = input[0]

    for inputVal in input:
        if inputVal > currVal:
            counter += 1
        currVal = inputVal
    
    print(counter)

if __name__ == "__main__":
    fileVal = readFile()
    parseData(fileVal)