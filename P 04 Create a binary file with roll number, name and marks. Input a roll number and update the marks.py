import pickle 
       
def Readrecord():
    with open ('StudentRecord.dat','rb') as Myfile:
        print("\n-------DISPALY STUDENTS DETAILS--------")
        print("\nRoll No.",' ','Name','\t',end='')
        print('Marks',)
        while True:
           try:
               rec=pickle.load(Myfile)
               print(' ',rec['SROLL'],'\t  ' ,rec['SNAME'],'\t ',end='')
               print(rec['SMarks'] )
           except EOFError:
                break

def Input():
    n=int(input("How many records you want to create :"))
    for ctr in range(n):
        sroll=int(input("Enter Roll No: "))
        sname=input("Enter Name: ")
        smarks=float(input("Enter Marks: "))
        Writerecord(sroll,sname,smarks)
        

def Modify(roll):
    with open ('StudentRecord.dat','rb') as Myfile:
        newRecord=[]
        while True:
           try:
               rec=pickle.load(Myfile)
               newRecord.append(rec)
           except EOFError:
                break
    found=1       
    for i in range(len(newRecord)):
        if newRecord[i]['SROLL']==roll:
            name=input("Enter Name: ")
            marks=float(input("Enter Marks: "))

            newRecord[i]['SNAME']=name
            newRecord[i]['SMarks']=perc
            found =1
        else:
            found=0

    if found==0:

        print("Record not found")
    with open ('StudentRecord.dat','wb') as Myfile:
         for j in newRecord:
             pickle.dump(j,Myfile)


def main():
       while True:
        print('\nYour Choices are: ')
        print('1.Insert Records')
        print('2.Dispaly Records') 
        print('3.Update Records')
        print('0.Exit (Enter 0 to exit)')
        ch=int(input('Enter Your Choice: '))
        if ch==1:
            Input()
        elif ch==2:
            Readrecord()
        elif ch==3:
            r =int(input("Enter a Rollno to be update: "))
            Modify(r)
        else:
            break
main()
