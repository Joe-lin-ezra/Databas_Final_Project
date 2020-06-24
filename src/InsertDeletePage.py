# Managed by Chin
#問題:中文輸入出現亂碼
import csv

#寫檔部分
with open('../data/Test.csv','w',newline='') as csvFile:
    Attribute = ['No.','StudentNo.','Class','CourseChineseName','Ptr']    # 設定csv 裡的欄位標題

    writer = csv.DictWriter(csvFile,fieldnames=Attribute,delimiter=' ')          # 寫入Dictionary 至 csv 檔裡

    writer.writeheader()        #把標題 (Attribute) 寫入csv檔案裡

    writer.writerow({'No.': '1', 'StudentNo.': 'D0001', 'Class': '1A','CourseChineseName':'中文科','Ptr':0})           #寫入測試資訊

#讀檔部分
with open('../data/Test.csv', newline='') as csvFile:
    reader = csv.DictReader(csvFile,fieldnames=Attribute,delimiter=' ')

    for read in reader:
        print(read)

    # 需要使用者輸入的資訊
    # print("學生編號輸入格式 : Dxxxx")
    # StdID = input("請輸入學生編號 : ")