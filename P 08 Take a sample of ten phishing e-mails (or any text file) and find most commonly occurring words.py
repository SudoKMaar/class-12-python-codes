#Take a sample of ten phishing e-mails and find most commonly occurring words
#--author Abhishek Kumar(14732821)
file = open("Top_Pishing_Mails.txt","r")
content = file.read()
max=0
max_occuring_word = ""
occurance_dict = {}
words = content.split()
for word in words:
    count = content.count(word)
    occurance_dict.update({word: count})
    if (count>max):
        max=count
        max_occuring_word=word
print("Most occuring word is:", max_occuring_word)
print("No of times it occured is:", max)
print("Other words frequency is:")
print(occurance_dict)
