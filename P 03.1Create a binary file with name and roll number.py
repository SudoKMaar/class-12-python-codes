#To create binary file and add name and roll number
                #--author Abhishek Kumar(14732821)
import pickle
stud_data = {}
list_of_students = []
no_of_students = int(input("Enter no of students : "))
for i in range(no_of_students):
    stud_data ["roll_no"] = int(input("Enter Roll NO:"))
    stud_data["name"] = input("Enter Name:")
    list_of_students.append(stud_data)
    stud_data={}
file=open("list.dat","wb")
pickle.dump(list_of_students, file)
file.close()
