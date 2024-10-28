# find Intersection Between Two lists. 
# num1=[1,2,2,5]
# num2=[2,2]


num1=[1,2,2,5]
num2=[2,2]
intersection=[]
for i in num1:
    if i in num2:
        intersection.append(i)
print(intersection)
