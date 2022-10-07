import random
import time
print("---------- maths practice quiz game -----------")
totalQuestions=10
timeTakenForAdd=[]
timeTakenForSub=[]
timeTakenForMult=[]
timeTakenForDiv=[]
selectedOperatorList=[]
print("enter 1 for normal, enter 2 for customized")
option=int(input("enter your option here:"))
operator=["+","-","*","/"]
if option==2:
    cust=input("do you want to test with specific operator?: ")
    if cust=="yes":
        ops=input("enter operator here ( +, -, *, /)")
        operator=[ops]
score=0
print("----- test started -----")
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
    
    userAns=int(input("enter your answer here: "))
    correctAns= eval(question)
    if userAns==correctAns:
        print("your answer is correct ")
        score+=5
    else:
        print("your answer is not correct correct answer is,", correctAns)
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
    elif selectedOperator=="*":
        timeTakenForMult.append(timeTakenPerq)
print("your score is", score,"/", totalQuestions*5 )
end=time.time()
time_taken=round(end-start)
print(time_taken, "seconds taken to answer")

selectedOperatorList=set(selectedOperatorList)
selectedOperatorList=list(selectedOperatorList)
print(" ")
print("------- average time taken -------")
print(" ")
avgTime=[]
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
        print("your average time for division is" ,round(avgDiv,2))
        avgTime.append(avgDiv)
    if i=="*":
        avgMult=sum(timeTakenForMult)/(len(timeTakenForMult))
        print("your average time for multiplication is" ,round(avgMult,2))
        avgTime.append(avgMult)
print(" ")
print(" ")
print(" ")
print(" ")
print(" ")

for i in range(4):
    print(selectedOperatorList[i]," |", end=" ")
    for j in range(round(avgTime[i])):
        print("#",end=" ")
    print(" ")
print("-------------------------------->")
print("             time taken-->")
