import pandas as pd

def sort():
    fileName = "DB_students_tc_big5.csv"
    df = pd.read_csv(fileName,encoding='cp950')

    DataList=[]

    for i in range(len(df)):
        ID = filter(str.isdigit, df.iat[i, 0])
        ID = int(''.join(list(ID)))
        tmpList=[ID,df.iat[i, 0],df.iat[i, 1],df.iat[i, 2]]
        DataList.append(tmpList)

    pointer=list(range(1,len(df)))
    pointer.append("NULL")
    DataList.sort()
    stdID=[]
    classID=[]
    name=[]
    for i in range(len(df)):
        stdID.append(DataList[i][1])
        classID.append(DataList[i][2])
        name.append(DataList[i][3])
    df["student_id"] = stdID
    df["course_id"] = classID
    df["course_name"] = name
    df["std_next_pointer"] = pointer
    df.to_csv("STD.csv", index=False, encoding='cp950')

    DataList.clear()
    pointer.clear()
    stdID.clear()
    classID.clear()
    name.clear()
    for i in range(len(df)):
        tmpList=[df.iat[i, 1],df.iat[i, 0],df.iat[i, 2]]
        DataList.append(tmpList)

    pointer=list(range(1,len(df)))
    pointer.append("NULL")
    DataList.sort()
    for i in range(len(df)):
        stdID.append(DataList[i][1])
        classID.append(DataList[i][0])
        name.append(DataList[i][2])
    df["student_id"] = stdID
    df["course_id"] = classID
    df["course_name"] = name
    df["std_next_pointer"] = pointer
    df.to_csv("Class.csv", index=False, encoding='cp950')

