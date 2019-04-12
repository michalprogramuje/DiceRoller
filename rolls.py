import random
def roll(dices, result):
    for x in range(dices):
        result.append(random.randint(1, 6))
def analyze_result(result, count1=0, count2=0, count3=0, count4=0, count5=0, count6=0):
    for i in result:
        if i==1:
            count1=count1+1
        elif i==2:
            count2=count2+1
        elif i==3:
            count3=count3+1
        elif i==4:
            count4=count4+1
        elif i==5:
            count5=count5+1
        elif i==6:
            count6=count6+1
    print("Liczba 1: ", count1, "\nLiczba 2: ", count2, "\nLiczba 3: ", count3, "\nLiczba 4: ", count4, "\nLiczba 5: ",
          count5, "\nLiczba 6: ", count6)
def reroll(whatreroll, result):
    howmany=0
    for i in result:
        if i in whatreroll:
            howmany=howmany+1
result=[]
roll(20,result)
print(result)
analyze_result(result)