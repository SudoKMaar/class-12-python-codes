#To read text file and display the required
#--author Abhishek Kumar(14732821)
file = open ("sample.txt","r")
data = file.read()
print (data)
vowels = 0
consonants =0
upper =0
lower =0

for ch in data:
    if str. isupper(ch):
        upper += 1
    elif str.islower(ch):
        lower += 1

    ch = str.lower(ch)
    if ch in "aeiou":
        vowels += 1
    elif ch in "bcdfghjklmnpqrstvwxyz":
        consonants += 1

print("No. of Vowles are : ",vowels)
print("No. of Consonants are: ",consonants)
print("No. of Upper Case letters are : ",upper)
print("No. of Lower Case letters are : ",lower)
