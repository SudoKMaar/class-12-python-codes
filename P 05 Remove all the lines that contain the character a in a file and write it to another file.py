#Remove all the lines that contain the character 'a' in a file and write it to another 
        #--author Abhishek Kumar(14732821)
file = open("first.txt","r")
lines = file.readlines() 
file.close()

file= open ("first.txt","w")
file1= open ("second.txt","w")
for line in lines:
    if 'a' in line:
        file1.write(line)
    else :
        file.write(line)
#For better user experience
print("All the lines that contains the keyword has been removed from First.txt")
print("All the lines that contains the keyword has been saved in Second.txt file")
file.close()
file1.close()
