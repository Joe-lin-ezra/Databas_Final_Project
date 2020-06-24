import csv
class DBMS(object):

    def __init__(self):
        self.hash_table = dict()
        with open('DB_students.csv',newline='') as csvfile:
            rows = csv.DictReader(csvfile)
            for row in rows:
                # print(row['student_id'])
                course_hash = hash(row['course_id'])
                # student_hash = hash(row['student_id'])
                if(course_hash in self.hash_table):
                    self.hash_table[course_hash].add(row['student_id'])
                else:
                    self.hash_table[course_hash] = set([row['student_id']])

    def print_table(self):
        return self.hash_table

    def add(self, course_id, student_id):
        course_hash = hash(course_id)
        if(course_hash in self.hash_table):
            self.hash_table[course_hash].add(student_id)
        else:
            self.hash_table[course_hash] = set([student_id])

    def remove(self, course_id, student_id):
        course_hash = hash(course_id)
        if(course_hash in self.hash_table):
            self.hash_table[course_hash].remove(student_id)
            if not self.hash_table[course_hash]:
                del self.hash_table[course_hash]
        else:
            print("NOT FOUND COURSE")

    def search(self, course_id):
        course_hash = hash(course_id)
        if not course_hash in self.hash_table:
            print("NOT FOUND COURSE")
        else :
           print(self.hash_table[course_hash])
           print(course_id + " total quantity：" + str(len(self.hash_table[course_hash])))
    
    def input_CID(self):
        CID = str(input("Input Course_ID："))
        return CID

    def input_SID(self):
        SID = str(input("Input Student_ID："))
        return SID

if __name__ == "__main__":
    dbms = DBMS()
    # print(dbms.print_table())
    # dbms.add("2142","D00000000")
    # print(dbms.print_table())
    # dbms.remove("2142","D00000000")
    # print(dbms.print_table())
    # dbms.remove("2142","D0877706")
    # print(dbms.print_table())
    # dbms.search("1297")
    
    while(True):
        opcode = input(">> ")
        if opcode == "add":
            dbms.add(dbms.input_CID(),dbms.input_SID())
        elif opcode == "del":
            dbms.remove(dbms.input_CID(),dbms.input_SID())
        elif opcode == "search":
            dbms.search(dbms.input_CID())
        elif opcode == "show":
            print(dbms.print_table())
        else:
            print("Undefine Code.")