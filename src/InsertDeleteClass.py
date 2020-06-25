# Managed by Chin
import csv

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
        Num = 0
        with open('../data/Test.csv', newline='') as csvFile:
            Attribute = ['No.', 'StudentNo.', 'Class', 'CourseChineseName', 'Ptr']
            reader = csv.DictReader(csvFile,fieldnames=Attribute,delimiter=' ')
            for read in reader:
                Num+=1
        print('File exists')
        Num = Num-1
    except IOError:
        Num = 0
        with open('../data/Test.csv', 'w', newline='') as csvFile:
            Attribute = ['No.','StudentNo.','Class','CourseChineseName','Ptr']    # 設定csv 裡的欄位標題
            writer = csv.DictWriter(csvFile,fieldnames=Attribute,delimiter=' ')          # 寫入Dictionary 至 csv 檔裡 ; delimiter 是分隔號
            writer.writeheader()        #把標題 (Attribute) 寫入csv檔案裡
        csvFile.close()
        print("Error: File does not appear to exist.")

    Num = Num
    ptrNum = Num

    def __init__(self,Num=Num,StdID=None,CourseID=None,CourseName_C=None,ptrNum=ptrNum):
        self.Num = Num
        self.StdID = StdID
        self.CourseID = CourseID
        self.CourseName_C = CourseName_C # 中文科目的名稱
        self.Ptr = ptrNum


    def Insert(self):
        self.Num += 1
        self.Ptr = self.Num - 1
        with open('../data/Test.csv', 'a+', newline='') as csvFile:         # 覆寫檔案
            Attribute = ['No.','StudentNo.','CourseID','CourseChineseName','Ptr']    # 設定csv 裡的欄位標題
            writer = csv.DictWriter(csvFile,fieldnames=Attribute,delimiter=' ')          # 寫入Dictionary 至 csv 檔裡
            writer.writerow(
                {'No.': self.Num, 'StudentNo.': self.StdID, 'CourseID': self.CourseID, 'CourseChineseName': self.CourseName_C,
                 'Ptr': self.Ptr})

        csvFile.close()
        print('Insert Success!')
        pass

    def Delete(self):
        print('Delete!')
        with open('../data/Test.csv', newline='') as csvFile:
            Attribute = ['No.', 'StudentNo.', 'CourseID', 'CourseChineseName', 'Ptr']
            reader = csv.DictReader(csvFile,fieldnames=Attribute,delimiter=' ')
            writer = csv.DictWriter(csvFile,fieldnames=Attribute,delimiter = ' ')
            for read in reader:
                if read['StudentNo.'] == self.StdID and read['CourseID'] == self.CourseID:
                    writer.writerow(read)

Process = Procedure(StdID='D0213',CourseID='2314')
Process.Delete()