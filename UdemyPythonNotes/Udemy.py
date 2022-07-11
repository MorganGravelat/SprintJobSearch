import this


print( len( input("What is your name? ") ) ) #This is a way you can prompt What is your name? Morgan and when I answer my name it spits out 6

def name_length():
    print('What is your name?')
    name = input()
    print(len(name))
    return len(name)
#Above is the worse version I made

## Primitive Data Types

#Print a string and index that string
print ("Hello"[0])
print("123" + "345")

#Type of data in python # this means it prints out to be this
num_char = 1
print(type(num_char)) # <class 'int'>


#Convert num_char to string
new_num_char = str(num_char) #Conver to string

#Can be used now in a concat print statement
print('HEY FOOL' + new_num_char) #type(new_num_char) <class 'str'>

# Add two numbers from a two digit input number
def twoNumbers(num):
    new_num = int(num[0]) + int(num[1]) # Converting the indexed str to int
    return new_num
print(twoNumbers(two_digit_number))


##Mathematical Operators

#Addition
num1 = 3 + 5 #8

#Subtraction
num2 = 5 - 3 #2

#Multiplication
num3 = 5 * 2 #10

#Divison
num4 = 6 / 3 #2.0
# Division always prints out float even with no remainder

#Exponent
2 ** 2 # 4
#This is 2 to the power of 2

# Please Excuse My Dear Aunt Sally PEMDAS
# ()
# **
# * /    #With these two the most left will be selected first
# + -


## Body Mass Index BMI Code

height = input("enter your height in m: ")
weight = input("enter your weight in kg: ")

def bodyindex(h, w):
    bmi = float(w) / (float(h)**2) #Input becomes a string, use float() to convert
    print(f"{w} ÷ ({h} x {h}) = {bmi}") #String formatting
    return bmi

print(bodyindex(height, weight))


##Number Manipulation
print (8/3) # 2.66666666
print (int(8/3)) # 2 #Convert into Integer int integer
print (round(8/3)) # 3 #2.6666666 UP Round number
print (round(8/3, 4)) # the 4 chooses the amount of decimal places you get NONE is 0

# You can take
result = 4 / 2 # 2
result /= 2 # this divides the result by 2 and makes it equal to the answer

# You can set a score
score = 0

score += 1 # 1 These can all manipulate the number.
score -= 1 # 0
score *= 1 # 0

## String Formatting
score = 0
height = 1.8
isWinning = True
# f-String
print(f"{score} that is score, then here is height {height} and here goes isWinning {isWinning}")
# Simple use of the f-String to calculate your days months and weeks until 90 years old
def weeksUntilNinety(age):
      years = 90 - int(age)
  months = round(years * 12)
  weeks = round(years * 52)
  days = round(years * 365)

  print(f"You have {days} days, {weeks} weeks, and {months} months left.")
  return f"You have {days} days, {weeks} weeks, and {months} months left."

###QUESTION TIME
a = int("5") / int(2.7)
#What data type will this become
#ANSWER: FLOAT

age = 12
print("You are " + age + " years old")
# This will give you a Type Error. Age is an integer. You are trying to concatenate a String to an Integer.


# f-string use, Decimal Formatting

## Calculating the per person price with tip included when splitting a meal or alone.add()
def tipCalculator():
      print("Welcome to the tip calculator!")
  bill = input("What was the total bill? $")
  tipPercent = input("How much tip would you like to give? ")
  people = input("How many people to split the bill? ")

  perPerson = (float(bill) / int(people)) * (1 + (.01 * float(tipPercent)))
  perPerson = "{:.2f}".format(perPerson) #Format the number of decimal places in the float
  print (f"Each person should pay: ${perPerson}")
  return f"Each person should pay: ${perPerson}"

tipCalculator()
## Below is Udemy SOlution with neat trick for affecting input right away.add()
# INPUT TRICKS
#If the bill was $150.00, split between 5 people, with 12% tip.
#Each person should pay (150.00 / 5) * 1.12 = 33.6
#Round the result to 2 decimal places.
print("Welcome to the tip calculator!")
bill = float(input("What was the total bill? $")) #Didn't know before to use these affectors on the input itself VERY USEFUL
tip = int(input("How much tip would you like to give? 10, 12, or 15? "))
people = int(input("How many people to split the bill?"))

tip_as_percent = tip / 100
total_tip_amount = bill * tip_as_percent
total_bill = bill + total_tip_amount
bill_per_person = total_bill / people
final_amount = round(bill_per_person, 2)


# FAQ: How to round to 2 decimal places?

# Find the answer in the Q&A here: https://www.udemy.com/course/100-days-of-code/learn/lecture/17965132#questions/13315048


print(f"Each person should pay: ${final_amount}")
## End tip calculator Below is other formatter codes
'''
Number	Format	Output	Description
3.1415926	{:.2f}	3.14	Format float 2 decimal places
3.1415926	{:+.2f}	+3.14	Format float 2 decimal places with sign
-1	{:+.2f}	-1.00	Format float 2 decimal places with sign
2.71828	{:.0f}	3	Format float with no decimal places
5	{:0>2d}	05	Pad number with zeros (left padding, width 2)
5	{:x<4d}	5xxx	Pad number with x’s (right padding, width 4)
10	{:x<4d}	10xx	Pad number with x’s (right padding, width 4)
1000000	{:,}	1,000,000	Number format with comma separator
0.25	{:.2%}	25.00%	Format percentage
1000000000	{:.2e}	1.00e+09	Exponent notation
13	{:10d}	        13	Right aligned (default, width 10)
13	{:<10d}	13	Left aligned (width 10)
13	{:^10d}	    13	Center aligned (width 10)
'''


### Control Flow and Logical Operators

#if else python code
'''
if condition:
    do this
else:
    do this
'''

#Example if statement
print ("Welcome to the rollercoaster")
height = int(input("What is your height in cm? "))
if height > 120: # You can also use >= / <= / < / == / != # All simple comparison operators
    print("You can ride the rollercoaster")
else:
    print("sorry go away")


### Mathematical Operators
## Modulo
# Modulo operator can be used to detect odds and evens
number = int(input("Which number do you want to check? "))

def OddorEven(num):
      if num % 2 != 0:
    print("This is an odd number")
    return "This is an odd number"
  else:
    print("This is an even number")

OddorEven(number)

##Updated rollercoaster height checker
print ("Welcome to the rollercoaster")
height = int(input("What is your height in cm? "))
if height > 120: # You can also use >= / <= / < / == / != # All simple comparison operators Conditional Operators Conditions
    print("You can ride the rollercoaster")
    age = int(input("What is your age? "))
    if age < 12:
        print("Please pay $5.")
    elif age <= 18:
        print("Please pay $7.")
    else:
        print("Please pay $12.")
else:
    print("sorry go away")
######## BREAK


### Upgraded BMI Calculator
height = float(input("enter your height in m: "))
weight = float(input("enter your weight in kg: "))

def bmiCalculator(height, weight):
  bmi = round(weight / (height ** 2))

  if bmi < 18.5:
    print(f"Your BMI is {bmi}, you are underweight.")
  elif bmi <= 25:
    print(f"Your BMI is {bmi}, you have a normal weight.")
  elif bmi <= 30:
    print(f"Your BMI is {bmi}, you are slightly overweight.")
  elif bmi <= 35:
    print(f"Your BMI is {bmi}, you are obese.")
  else:
    print(f"Your BMI is {bmi}, you are clinically obese.")
  return


bmiCalculator(height, weight)

### End of BMI Calculator

##Found out if something is a leap year modulo if else statements
year = int(input("Which year do you want to check? "))

if year % 100 == 0:
  if year % 400 == 0:
    print("Leap Year")
  else:
    print("Not Leap Year")
elif year % 4 == 0:
  print("Leap Year")
else:
  print("Not Leap Year")

##Their version below
if year % 4 == 0:
    if year % 100 == 0:
        if year % 400 == 0:
            print("Leap Year")
        else:
            print("Not leap year.")
    else:
        print("Leap Year.")
else:
    print("Not Leap Year.")

### END OF Leap Year Finder
##If elif else practice
print("Welcome to the rollercoaster!")
height = int(input("What is your height in cm? "))
bill = 0

if height >= 120:
  print("You can ride the rollercoaster!")
  age = int(input("What is your age? "))
  if age < 12:
    bill = 5
    print("Child tickets are $5.")
  elif age <= 18:
    bill = 7
    print("Youth tickets are $7.")
  else:
    bill = 12
    print("Adult tickets are $12.")

  wants_photo = input("Do you want a photo taken? Y or N. ")
  if wants_photo == "Y":
    bill += 3

  print(f"Your final bill is ${bill}")

else:
  print("Sorry, you have to grow taller before you can ride.")


##Else if practice // PIZZA ORDER Input if else elif mathematical operator
print("Welcome to Python Pizza Deliveries!")
size = input("What size pizza do you want? S, M, or L ")
add_pepperoni = input("Do you want pepperoni? Y or N ")
extra_cheese = input("Do you want extra cheese? Y or N ")

bill = 0

if size == 'L':
  bill += 25
elif size == 'M':
  bill += 20
elif size == 'S':
  bill += 15

if add_pepperoni == "Y":
  if size == 'S':
    bill += 2
  else:
    bill += 3

if extra_cheese == "Y":
  bill += 1

print(f"Your final bill is: {bill}")
