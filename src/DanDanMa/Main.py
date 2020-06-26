import pandas as pd
import sys
sys.setrecursionlimit(100000000)


def sort(Data):
    if len(Data) > 1:
        mid = len(Data) // 2
    leftData = {"id": Data["id"][:mid],
                "student_id": Data["student_id"][:mid],
                "course_id": Data["course_id"][:mid],
                "course_name": Data["course_name"][:mid],
                }
    rightData = {"id": Data["id"][mid:],
                 "student_id": Data["student_id"][mid:],
                 "course_id": Data["course_id"][mid:],
                 "course_name": Data["course_name"][mid:],
                 }
    sort(leftData)
    sort(rightData)

    leftIndex = 0
    rightIndex = 0
    mergedIndex = 0
    while rightIndex < len(rightData) and leftIndex < len(leftData):
        if rightData["id"][rightIndex] < leftData["id"][leftIndex]:
            Data["student_id"][mergedIndex] = rightData["student_id"][rightIndex]
            Data["course_id"][mergedIndex] = rightData["course_id"][rightIndex]
            Data["course_name"][mergedIndex] = rightData["course_name"][rightIndex]
            rightIndex = rightIndex + 1
        else:
            Data["student_id"][mergedIndex] = leftData["student_id"][leftIndex]
            Data["course_id"][mergedIndex] = leftData["course_id"][leftIndex]
            Data["course_name"][mergedIndex] = leftData["course_name"][leftIndex]
            leftIndex = leftIndex + 1
        mergedIndex = mergedIndex + 1
    while rightIndex < len(rightData):
        Data["student_id"][mergedIndex] = rightData["student_id"][rightIndex]
        Data["course_id"][mergedIndex] = rightData["course_id"][rightIndex]
        Data["course_name"][mergedIndex] = rightData["course_name"][rightIndex]
        rightIndex = rightIndex + 1
        mergedIndex = mergedIndex + 1
    while leftIndex < len(leftData):
        Data["student_id"][mergedIndex] = leftData["student_id"][leftIndex]
        Data["course_id"][mergedIndex] = leftData["course_id"][leftIndex]
        Data["course_name"][mergedIndex] = leftData["course_name"][leftIndex]
        leftIndex = leftIndex + 1
        mergedIndex = mergedIndex + 1

fileName = "DB_students_tc_big5.csv"
df = pd.read_csv(fileName,encoding='cp950')

choose=int(input("0.sort 1.use stdID search 2. use classID serach"))
if(choose==0):
    ##use stdID sort
    Data = {"id":[],
            "student_id":[],
            "course_id":[],
            "course_name":[],
            }
    for i in range(len(df)):
        ID = filter(str.isdigit, df.iat[i, 0])
        ID = int(''.join(list(ID)))
        Data["id"].append(ID)
        Data["student_id"].append(df.iat[i,0])
        Data["course_id"].append(df.iat[i,1])
        Data["course_name"].append(df.iat[i,2])
    Data = sort(Data)

    df["student_id"] = Data["student_id"]
    df["course_id"] = Data["course_id"]
    df["course_name"] = Data["course_name"]
    df.to_csv(fileName, index=False, encoding='cp950')

elif choose==1:
    print("2")
elif choose==2:
    print("2")