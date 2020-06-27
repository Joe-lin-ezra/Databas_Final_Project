import DanDanMa
import os


def main():
    StdID = input('Please Enter Your Student ID : ')
    CourseID = input('Please Enter Your Class : ')
    CourseName = input('Please Enter Class Name: ')
    confirm = int(input('Are you sure to insert the record? Y:100000, N:(other):'))

    # StdID = 'D047765252'
    # CourseID = '2142'
    # CourseName = 'aka476'
    # confirm = 100000

    if confirm != 100000:
        return 0

    fileName = "DanDanMa/DB_students_tc_big5.csv"
    file = open(fileName, 'a', encoding='cp950')

    file.writelines([StdID, ',', CourseID, ',', CourseName, ',', '\n'])
    DanDanMa.Sort.sort()


if __name__ == '__main__':
    main()
