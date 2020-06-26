import csv

def readcsv():
    keys = []
    count = 0
    with open('../data/DB_students_tc_big5.csv', 'r') as fp:
        reader = csv.DictReader(fp)
        for rec in reader:
            if count == 100:
                break
            if rec['student_id'][2:6] in keys:
                continue
            keys.append(rec['student_id'][2:6])
            count+=1
    return keys