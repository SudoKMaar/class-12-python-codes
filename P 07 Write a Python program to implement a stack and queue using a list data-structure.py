#Program to implement a stack and queue using a list data-structure
#--author Abhishek Kumar(14732821)
STACK = []
MAX_CAPACITY=3
while(True):
    print('''1. Push value into Stack.
2. Pop value from STACK.
3. Print TOP value of STACK.
4. Print All value of Stack
Press any other number to exit.
    ''')
    choice = int(input("Enter your choice:"))
    if (choice ==1):
        if (len(STACK)==MAX_CAPACITY):
            print("STACK OVERFLOW..!!")
        else:
            val = int(input("Enter number to push into STACK"))
            STACK.append(val)
    elif (choice ==2):
        if (len(STACK)==0):
            print("STACK UNDERFLOW..!!")
        else:
            n = STACK.pop()
            print(n, "REMOVED FROM STACK")
    elif(choice ==3):
        top = STACK[-1]
        print("TOP VALUE OF STTACK IS", top)
    elif(choice ==4):
        print("ALL ELEMENTS OF STACK ARE:")
        print(STACK)
    else:
        break
