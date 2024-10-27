# find the MAX element in a given list
# list =[3,5,7,9,2]


list =[3,5,7,9,2]

max=0

for i in list:
    if i>max:
        max=i
print("max element :",max)



'''  with explain '''

# Define the list of numbers
list = [3, 5, 7, 9, 2]

# Initialize the variable 'max' with 0
# This will be updated if any element in the list is greater than 0
max = 0

# Loop through each element in the list
for i in list:
    # If the current element is greater than 'max', update 'max'
    if i > max:
        max = i

# Print the maximum element found in the list
print("max element:", max)
