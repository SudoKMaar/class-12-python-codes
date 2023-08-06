#To read a text file and seprate each word by #
#--author Abhishek Kumar(14732821)
file = open("sample.txt","r")
content = file.readlines()
for line in content:
    words = line.split()
    for word in words:
        print (word+"#", end='')
    print ("")
