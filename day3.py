# find the unique element in the given list without using inbulit function 
# num=[1,8,1,2,3,2,4,5,4,5]

num=[1,8,1,2,3,2,4,5,4,5]
unique=[]
for i in num:
    if i not in unique:
        unique.append(i)
print(unique)