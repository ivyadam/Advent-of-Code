def readFile():
    file = open('./Day2/data2.txt','r')
    output = []
    while file:
        line = file.readline()
        if not line:
            break
        
        if line.endswith('\n'):
            line = line[:-1]
        splitLine = line.split(' ')
        output.append(splitLine)

    file.close()
    return output

def parseData(input):
    horizontal = vertical = aim = 0

    for inputVal in input:
        if inputVal[0] == 'forward':
            horizontal += int(inputVal[1])
            vertical += (aim * int(inputVal[1]))
        elif inputVal[0] == 'up':
            aim -= int(inputVal[1])
        else:
            aim += int(inputVal[1])
    
    print(horizontal * vertical)

if __name__ == "__main__":
    fileVal = readFile()
    parseData(fileVal)