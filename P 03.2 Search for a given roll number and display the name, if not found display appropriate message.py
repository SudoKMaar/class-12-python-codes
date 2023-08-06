#To search for roll number and display the name
                #--author Abhishek Kumar(14732821)
import pickle
file = open ("list.dat","rb")
list_of_students = pickle.load(file)
roll_no = int(input("Enter roll no. of the student"))
found = False
for stud_data in list_of_students:
    if(stud_data['roll_no']==roll_no):
        found=True
        print (stud_data['name'], "found in file.")
if (found == False):
    print ("No student data found. Please try again.")
