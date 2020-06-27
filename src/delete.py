import DanDanMa
import os


def main():
    StdID = input('Please Enter Your Student ID : ')
    CourseID = input('Please Enter Your Class : ')
    confirm = int(input('Are you sure to delete the record? Y:100000, N:(other):'))

    # StdID = 'D0877706'
    # CourseID = '2142'
    # confirm = 100000

    if confirm != 100000:
        return 0

    fileName = "DanDanMa/DB_students_tc_big5.csv"
    inp = open(fileName, 'r+', encoding='cp950')
    out = open('DanDanMa/changed_File.csv', 'w', encoding='cp950')

    title = inp.readline()
    out.writelines(title)

    end = False

    while not end:

        for i in range(100):
            line = inp.readline()
            newLine = line.strip('\n').split(',')
            if newLine[0] == StdID and newLine[1] == CourseID:
                continue
            else:
                out.writelines(line)
            if newLine[0] == '':
                end = True
                break

    out.flush()
    inp.close()
    out.close()

    # for consistence the file
    # window cmd commands
    os.system('del DanDanMa\DB_students_tc_big5.csv')
    os.system('ren DanDanMa\changed_File.csv DB_students_tc_big5.csv')
    DanDanMa.Sort.sort()


if __name__ == '__main__':
    main()
