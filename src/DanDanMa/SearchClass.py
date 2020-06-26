import pandas as pd

def search(ID):
    counter=0
    breaknum=0
    fileName = "Class.csv"
    df = pd.read_csv(fileName, encoding='cp950')
    ID=int(ID)
    for i in range(len(df)):
        # print(int(df.iat[counter, 1]))
        if ID == int(df.iat[counter, 1]):
            print(df.iat[counter, 0])
            while True:
                counter = df.iat[counter, 3]
                try:
                    counter = int(counter)
                except:
                    print(counter)
                    breaknum=1
                    break
                if (ID != df.iat[counter, 1]):
                    breaknum=1
                    break
                print(df.iat[counter, 0])
        if breaknum==1:
            break
        counter = df.iat[counter, 3]
        try:
            counter = int(counter)
        except:
            break
