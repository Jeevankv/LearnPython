#Heath Management System
import sys
def getDate():
    import datetime
    return datetime.datetime.now()

def AddFood():

    print("Whose Data Do you Want to ADD")
    print("press 1:Jeevan 2:Manoj 3:Abhay")
    choiceFood = int(input())
    print("Enter the Food Taken")
    if choiceFood== 1:
        food = input()
        Date = str(getDate())
        JD = open("health management system/JeevanDiet.txt", "a")
        JD.write("\n["+Date+"] : "+food+"\n")
        JD.close()
        print("Data written successfully\n")
    elif choiceFood == 2:
        Date = str(getDate())
        food = input()
        MD = open("health management system/ManojDiet.txt", "a")
        MD.write("\n["+Date+"] : "+food+"\n")
        MD.close()
        print("Data written successfully\n")
    elif choiceFood == 3:
        Date = str(getDate())
        food = input()
        AD = open("health management system/AbhayDiet.txt", "a")
        AD.write("\n["+Date+"] : "+food+"\n")
        AD.close()
        print("Data written successfully\n")

def AddExercise():
    print("Whose Data Do you Want to ADD")
    print("press 1:Jeevan 2:Manoj 3:Abhay")
    choiceExercise = int(input())
    print("Enter Exercise Done")
    if choiceExercise == 1:
        Date = str(getDate())
        Exercise = input()
        JE = open("health management system/JeevanExercise.txt", "a")
        JE.write("\n["+Date+"] : "+Exercise+"\n")
        JE.close()
        print("Data written successfully\n")
    elif choiceExercise==2:
        Date = str(getDate())
        Exercise = input()
        ME = open("health management system/ManojExercise.txt", "a")
        ME.write("\n[" + Date + "] : " + Exercise + "\n")
        ME.close()
        print("Data written successfully\n")
    elif choiceExercise==3:
        Date = str(getDate())
        Exercise = input()
        AE = open("health management system/AbhayExercise.txt", "a")
        AE.write("\n[" + Date + "] : " + Exercise + "\n")
        AE.close()
        print("Data written successfully\n")

def RetrieveFood():
    print("Whose Data Do you Want to Retrieve")
    print("press 1:Jeevan 2:Manoj 3:Abhay")
    choiceFood=int(input())
    if choiceFood==1:
        JD=open("health management system/JeevanDiet.txt")
        print(JD.read())
        JD.close()
    elif choiceFood==2:
        MD=open("health management system/ManojDiet.txt")
        print(MD.read())
        MD.close()
    elif choiceFood==3:
        AD=open("health management system/AbhayDiet.txt")
        print(AD.read())
        AD.close()

def RetrieveExercise():
    print("Whose Data Do you Want to Retrieve")
    print("press 1:Jeevan 2:Manoj 3:Abhay")
    choiceExercise=int(input())
    if choiceExercise==1:
        JE=open("health management system/JeevanExercise.txt")
        print(JE.read())
        JE.close()
    elif choiceExercise==2:
        ME=open("health management system/ManojExercise.txt")
        print(ME.read())
        ME.close()
    elif choiceExercise==3:
        AE=open("health management system/AbhayExercise.txt")
        print(AE.read())
        AE.close()

while(True):
    print("DO you want to Add Data or Retrieve Data?")
    print("press 1 to Add Data\npress 2 to Retrieve Data")
    inp=int(input())
    if inp == 1:
        print("Which Data do you want Add ?(Diet or Exercise)")
        print("press 1:Diet 2:Exercise")
        choiceAdd = int(input())
        if choiceAdd==1:
            AddFood()
        else:
            AddExercise()
    elif inp==2:
        print("Which Data do you want Retrieve ?(Diet or Exercise)")
        print("press 1:Diet 2:Exercise")
        choiceRetrieve = int(input())
        if choiceRetrieve==1:
            RetrieveFood()
        else:
            RetrieveExercise()

    print("Do You want to continue ?(y / n)")
    loop =input()
    if loop == 'y':
        continue
    else:
        sys.exit()



