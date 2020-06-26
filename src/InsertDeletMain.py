# Managed by Chin
#問題:中文輸入出現亂碼
import InsertDeleteClass

if __name__ == '__main__':

    while True:
        print('What do you want to do ?')
        print('1. Insert Data')
        print('2. Delete Data')
        Action = input("Enter your selection (number) : ")
        check = InsertDeleteClass.Analysis(Action)
        if (check.CheckSelection()):
            break

    if Action == str(1):
        while True:
            StdID = input('Please Enter Your Student ID : ')
            check = InsertDeleteClass.Analysis(StdID)           # 分析輸入的StdID 是否符合要求(D字開頭)
            if check.CheckStdID():
                break

        while True:
            CourseID = input('Please Enter Your Class : ')
            check = InsertDeleteClass.Analysis(CourseID)
            if check.CheckCourseID():
                break

        while True:
            CourseName = input('Please Enter Your Chinese Course Name : ')
            check = InsertDeleteClass.Analysis(CourseName)
            if check.CheckCourseName():
                break

        Process = InsertDeleteClass.Procedure(StdID=StdID,CourseID=CourseID,CourseName_C = CourseName)
        Process.Insert()
    else:

        while True:
            StdID = input('Please Enter Your Student ID : ')
            check = InsertDeleteClass.Analysis(StdID)           # 分析輸入的StdID 是否符合要求(D字開頭)
            if check.CheckStdID():
                break

        while True:
            CourseID = input('Please Enter Your Class : ')
            check = InsertDeleteClass.Analysis(CourseID)
            if check.CheckCourseID():
                break

        Process = InsertDeleteClass.Procedure(StdID=StdID,CourseID=CourseID)
        Process.Delete(StdID,CourseID)