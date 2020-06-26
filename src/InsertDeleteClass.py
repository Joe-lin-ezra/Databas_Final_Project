# Managed by Chin
import csv
from operator import itemgetter, attrgetter
class Analysis():
    def __init__(self,input):
        self.Input = input

    def CheckSelection(self):
        if self.Input == str(1):
            # print('Insert Data')
            return 1
        elif self.Input == str(2):
            # print('Delete Data')
            return 1
        else:
            print("---Invaild Selection Please Input Again---")
            return 0

    def CheckStdID(self):
        if self.Input[0] == 'D' :
            return 1
        else:
            print("---Invaild StudentID Please Input Again---")
            return 0

    def CheckCourseID(self):
        if len(self.Input) > 4 or len(self.Input) < 4:
            print("---Invaild CourseID Please Input Again---")
            return 0
        elif self.Input[0] == '0' :
            print("---Invaild CourseID Please Input Again---")
            return 0
        else:
            return 1

    def CheckCourseName(self):
        if self.Input.islower() or self.Input.isupper():
            print("---Invaild CourseName Please Input Again---")
            return 0
        else:
            return 1


class Procedure ():
    try:
        open('../data/DB_students_tc_big5.csv', newline='',encoding="utf-8")
        def Copy(self):
            File = csv.reader(open('../data/DB_students_tc_big5.csv', encoding="utf-8"))
            writer = csv.writer(open('../data/copy.csv', 'w+', newline='', encoding="utf-8"))
            writer.writerow(['No.', "student_id", 'course_id', 'course_name', 'ptr'])
            Line = [i for i in File]
            # print(Line[index][0,1,2]) 0 : stdid 1: courseID 2 : courseName
            for i in range(0, 100):
                if Line[i][1].isnumeric():
                    writer.writerow([i, Line[i][0], Line[i][1], Line[i][2],None])
            pass
        print('File exists')
    except IOError:
        Num = 0
        print("Error: File does not appear to exist.")


    def __init__(self,StdID=None,CourseID=None,CourseName_C=None):
        self.StdID = StdID
        self.CourseID = CourseID
        self.CourseName_C = CourseName_C # 中文科目的名稱


    def Insert(self):
        # 從未排序的File中取得最後的號碼(LastDataNumber)
        UnSortingFile = csv.reader(open('../data/copy.csv', newline='', encoding='utf-8'))
        LastDataNumber = 0
        for i in UnSortingFile:
            LastDataNumber = i[0]
        open('../data/copy.csv').close()

        # 透過已知最後的號碼來加插新的資料於下一行
        with open('../data/copy.csv', 'a', newline='', encoding='utf-8') as File:
            OverWrite = csv.writer(File)
            InsertToNumber = int(LastDataNumber) + 1
            data = [InsertToNumber, self.StdID, self.CourseID, self.CourseName_C,0]
            OverWrite.writerow(data)
        open('../data/copy.csv').close()

        # Pointer Distribution
        self.PtrRelocation()

        # Sortting
        self.SortingByStudentID()

        print("Insert Done!")
        pass

    def SortingByStudentID(self):
        File = csv.reader(open('../data/copy.csv',encoding="utf-8"))
        writer = csv.writer(open('../data/OutputTest.csv','w',newline='',encoding="utf-8"))
        OutputFile = sorted(File,key=itemgetter(1))
        for i in OutputFile:
            if i[0].isnumeric():
                writer.writerow(i)

        pass

    def GetTotalLine(self):
        Count = 0
        File = csv.reader(open('../data/copy.csv', newline='', encoding='utf-8'))
        for i in File:
            Count+=1
        return Count

    def PtrRelocation(self):
        # 取得TotalLine(總行數)
        TotalLine = self.GetTotalLine()
        File = csv.reader(open('../data/copy.csv',encoding="utf-8"))
        Line = [line for line in File]
        # Modify Part
        for i in range(0,TotalLine):
            if Line[i][4].isnumeric():
                if i+2 <= TotalLine:
                    Line[i][4] = i+2
        with open('../data/copy.csv', 'w', newline='',encoding="utf-8") as csvFile:
            writer = csv.writer(csvFile)
            for line in Line:
                if line[0].isnumeric():
                    writer.writerow(line)
        pass


    def Delete(self,StdID,CourseID):
        # 讀取未排序的資料
        File = csv.reader(open('../data/copy.csv', encoding="utf-8"))
        Line = [line for line in File]
        Found = 0
        count = 0
        PointingToTarget = 0            # 繼承del 位置的資料所指向的位置
        for i in Line:
            if i[1] == StdID and i[2] == CourseID:
                PointingToTarget = i[0]
                break

        # 重新載入資料(清除的不會被載入)
        with open('../data/copy.csv','w',newline='',encoding='utf-8') as csvFile:
            Writer = csv.writer(csvFile)
            for i in Line:
                if i[1] != StdID and i[2] != CourseID:
                    if i[4] != PointingToTarget:
                        Writer.writerow(i)
                else:
                    Line[count-1][4] = Line[count][4]
                    Writer.writerow(Line[count-1])
                count += 1

        #輸出到OutputTest 的介面中
        self.SortingByStudentID()

        print("Deletion Complete!")
