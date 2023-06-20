#Day 2; data types
#string are represented with a quotation mark
"hello" "world" "maryam" "abiola" "alliu"
#subscript is the method of pulling out a character in a string
print("hello"[0])
#integer; are whole numbers either positive or negative
print(123 + 34)
#large numbers are represented by underscore instead of a comma
123_456_789 
#float; are numbers with decimal points
print(123.5 + 5.7)
#boolean; they are either True or False
True
False
#How to know the datatype of a variable
name = "Maryam"
print(type(name))
age = 18
print(type(age))
#Type conversion

#hands on 4 two digits
number = input("Type a two digit number ")
first_number = number[0]
second_number = number[1]
print(int(first_number) + int(second_number))
#mathematical operation; BEDMAS
print(7 - 5)
print(7 + 5)
print(7 * 5)
print(7 / 5)
print(7 ** 5)
#hands on BMI 
height = input("enter your height in m ")
weight = input("enter your weight in kg")
bmi = int(weight) / float(height) ** 2
print(int(bmi))
#number manipulation and f string
#rounding of a number in float
print(round(5 / 3 , 2)) #the 2 represent the number of decimal places the output will be
# to get an whole number without changing the datatype while dividing is using //
print(7 // 2)
# when you want to divide twice
result = (4 / 2)
result /= 2
print(result)
# when you want to substract, add, multiply easily
score = 2
score =+ 1
print(score)
#f-string
score = 0
print(f"your score is {score}")
#hands on life in weeks
age = input("What is your current age? ")
days = (int(age) * int(365))
weeks = (int(age) * int(52))
months = (int(age) * int(12))
print(f"you have {days} days, {weeks} weeks and {months} months")