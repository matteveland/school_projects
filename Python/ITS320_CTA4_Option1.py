#Write a program that utilizes a loop to read a set of five floating-point values from user input.
#Ask the user to enter the values, then print the following data:

#Total
#Average
#Maximum
#Minimum
#Interest at 20% for each original value entered by the user.
#Use the formula: Interest_Value = Original_value + Original_value*0.2
#Assignment Submission Instructions

#Submit a text file containing your Python code. Name your file ITS320_CTA4_Option1.py.

print('Please enter 5 random numbers, whole or decimal, dealer\'s choice.')
input1 = float(input('1st Number: '))
input2 = float(input('2nd Number: '))
input3 = float(input('3rd Number: '))
input4 = float(input('4th Number: '))
input5 = float(input('5th Number: '))
#input1 = int(10)
#input2 = int(20)
#input3 = int(30)
#input4 = int(40)
#input5 = int(50)
user_inputs = [input1, input2, input3, input4, input5]

print('\nYou have entered the following set of numbers:', user_inputs, '\n')

sum_inputs = sum(user_inputs)
avg_inputs = sum(user_inputs)/len(user_inputs)

#Total
print('Sum of your inputs:', sum_inputs)
#Average
print('Average of your inputs:', avg_inputs)
#Maximum
print('Max number of your inputs:', max(user_inputs))
#Minimum
print('Minimum number of your inputs:', min(user_inputs), '\n')

print('For each value entered, a 20% interest would be:')
count = 1
for i in user_inputs:
    Interest_Value = i + (i * 0.2)
    print(f"Value {count}: {i} value at 20% interest is: ", Interest_Value)
    count += 1
