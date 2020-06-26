
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
    Data = sort(leftData)
    Data = sort(rightData)

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
    return Data
