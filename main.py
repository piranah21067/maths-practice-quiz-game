import random
import time

print("---------- Maths Practice Quiz Game -----------")

totalQuestions=10
score=0

timeTakenForAdd=[]
timeTakenForSub=[]
timeTakenForMult=[]
timeTakenForDiv=[]
avgTime=[]  # Shows average time taken per question for all operators individually
selectedOperatorList=[]


print("Enter 1 for normal, enter 2 for customized")
option=int(input("Enter your option here:"))
operator=["+","-","*","/"]
if option==2:
    cust=input("Do you want to test with specific operator?: ")
    if cust=="yes":
        ops=input("Enter operator here ( +, -, *, /)")
        operator=[ops]

print("----- Test Started -----")

start=time.time()

for i in range(totalQuestions):
    startq=time.time()
    num=random.randint(1,10)
    num2=random.randint(1,100)
    selectedOperator= random.choice(operator)
    selectedOperatorList.append(selectedOperator)
    if selectedOperator=="*" or operator=="/":
        num2=random.randint(1,10)
    if selectedOperator=="/":
        num=random.randint(1,100)*num2
    question= str(num) + selectedOperator + str(num2)
    print("what is", question)
    
    userAns=int(input("Enter your answer here: "))
    correctAns= eval(question)
    
    if userAns==correctAns:
        print("Your answer is correct ")
        score+=5
    else:
        print("Your answer is not correct correct answer is,", correctAns)
        score-=1
    endq=time.time()
    timeTakenPerq=round(endq-startq)
    print(timeTakenPerq)
    
    if selectedOperator=="+":
        timeTakenForAdd.append(timeTakenPerq)
    elif selectedOperator=="-":
        timeTakenForSub.append(timeTakenPerq)
    elif selectedOperator=="/":
        timeTakenForDiv.append(timeTakenPerq)
    else:
        timeTakenForMult.append(timeTakenPerq)

print("Your score is", score,"/", totalQuestions*5 )
end=time.time()
time_taken=round(end-start)
print(time_taken, "Seconds taken to answer")

# Converting list to set to remove duplicate values
selectedOperatorList=list(set(selectedOperatorList))

print(" ")
print("------- Average Time Taken -------")
print(" ")
selectedOperatorList.sort()

for i in selectedOperatorList:
    if i=="+":
        avgAdd=sum(timeTakenForAdd)/(len(timeTakenForAdd))
        print("your average time for addition is" ,round(avgAdd,2))
        avgTime.append(avgAdd)
    if i=="-":
        avgSub=sum(timeTakenForSub)/(len(timeTakenForSub))
        print("your average time for subtraction is" ,round(avgSub,2))
        avgTime.append(avgSub)
    if i=="/":
        avgDiv=sum(timeTakenForDiv)/(len(timeTakenForDiv))
        print("Your average time for division is" ,round(avgDiv,2))
        avgTime.append(avgDiv)
    if i=="*":
        avgMult=sum(timeTakenForMult)/(len(timeTakenForMult))
        print("Your average time for multiplication is" ,round(avgMult,2))
        avgTime.append(avgMult)

print("\n  "*4)
print("------- Graph--------")
print(" ")

for i in range(len(selectedOperatorList)):
    print(selectedOperatorList[i]," |", end=" ")
    for j in range(round(avgTime[i])):
        print("#",end=" ")
    print(" ")

print("-------------------------------->")
print("             time taken-->")
