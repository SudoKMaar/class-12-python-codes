import pickle
student_data = {}
file = open("student_data.dat","rb+")
try:
    while True:
        student_data = pickle.load(file)
        print(student_data)
except EOFError:
    file.close()
