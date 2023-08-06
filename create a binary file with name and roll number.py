import pickle
student_data = {}
no_of_students = int(input("Enter no of students to insert in file:"))
file = open("student_data.dat","wb")
for i in range(no_of_students):
    student_data ["RollNo"]= int(input("Enter roll no:"))
    student_data ["Name"]= input("Enter Student Name:")
    student_data ["Marks"] = float(input ("Enter Student Marks:"))
    pickle.dump(student_data, file)
    student_data={}
file.close()
