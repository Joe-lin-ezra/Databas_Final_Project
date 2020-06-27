import pandas as pd

def search(ID):
    counter = 0
    fileName = "STD.csv"
    file = open(fileName, encoding='cp950')

    line = file.readline()
    line = line.strip('\n').split(',')
    title = line
    title.pop()

    content = list()
    breakFlag = False
    while not breakFlag:
        for i in range(100):
            line = file.readline()
            line = line.strip('\n').split(',')

            if line[3] == 'NULL':
                breakFlag = True
                break

            if line[0] == ID:
                print(line[0], line[1], line[2])
                content.append([line[0], line[1], line[2]])

    file.close()
    return title, content

print(search('D099995294'))