#Day 1 I learnt about how to print, strings
print("Hello world!")
# creating new lines on a single line of code using \n 
print("Hello world\nHello world")
# combination of strings into one strings
print("Hello" + "Angela")
print("Alliu" + "Maryam" + "Abiola")
# spacing in combined string
print("Alliu " + " Maryam" + " Abiola")
print("Alliu" + " " + "Maryam" + " " + "Abiola")
# indentation error: is the error when there are spaces at the beginning of a line;in python codes are started at the beginning of the line
# input function
input("What is your name?")
#difference between input and print: input contains the prompt and print contains the output
print("Hello " + input("What is your name?"))
#Hands on 1
name = input("what is your name?")
length = len(name)
print(length)
print( len ( input("what is your name?")))
#Python variable
name = "Abiola"
print(name)
#hands on 2
a = input("a: ")
b = input("b: ")
a = b
c = a
print(b)
print(c)
#variable naming; you can't have a space btw a variable, use an underscore,
user_name = input("what is your last name?")
age1 = "70years"
# Band name hands on 3
print("Welcome to the Band Name Generator")
city = input("What is the name of the city you grew up in?")
pet = input("What's the name of your pet?")
print("Your band name could be" + " " + city + " " + pet)
