import csv

def readcsv():
    keys = []
    count = 0
    with open('DB_students_tc_big5.csv', 'r') as fp:
        reader = csv.DictReader(fp)
        for rec in reader:
            if count == 10:
                break
            if rec['student_id'] in keys:
                continue
            keys.append(rec['student_id'])
            count+=1
    return keys