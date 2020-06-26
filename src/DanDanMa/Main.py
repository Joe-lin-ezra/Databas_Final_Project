import Sort
import SearchSTD
import SearchClass
import sys
sys.setrecursionlimit(100000000)

choose=int(input("0.sort 1.use stdID search 2. use classID serach"))
if(choose==0):
    Sort.sort()
elif choose==1:
    ID=input("plz enter std ID")
    SearchSTD.search(ID)
elif choose==2:
    ID = input("plz enter class ID")
    SearchClass.search(ID)