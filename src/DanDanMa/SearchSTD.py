import pandas as pd

def search(ID):
    counter=0
    breaknum=0
    fileName = "STD.csv"
    df = pd.read_csv(fileName, encoding='cp950')
    for i in range(len(df)):
        if ID == df.iat[counter, 0]:
            print(df.iat[counter, 1],df.iat[counter, 2])
            while True:
                counter = df.iat[counter, 3]
                counter = int(counter)
                if (ID != df.iat[counter, 0]):
                    breaknum=1
                    break
                print(df.iat[counter, 1], df.iat[counter, 2])
        if breaknum==1:
            break
        counter = df.iat[counter, 3]
        try:
            counter = int(counter)
        except:
            break
