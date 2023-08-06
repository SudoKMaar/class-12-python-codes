import pickle
student_data = {}
found = False 
roll_no = int(input("Enter the roll no to search:"))
file = open("student_data.dat","wb+")
try:
    while True:
        pos = file.tell()
        student_data= pickle.load(file)
        if (student_data['RollNo']==roll_no):
            student_data['Marks']= float(input("Enter marks to update:"))
            file.seek(pos)
            pickle.dump(student_data)
            found=True
except EOFError:
    if (found == False):
        print ("Roll No not found. Please try again")
    else:
        print("Student marks updated successfuly")
    file.close()
