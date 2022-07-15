from secrets import randbelow
import this
from tkinter import N


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

##Multi conditional statments

a = 12
# is a > 15 ? False
# is a > 10 and a < 13 the and operator is javascript &&
a > 10 and a < 13
a > 10 or a < 13 # or is javascripts || operator

## New conditionals for mid life crisis men
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
  elif age >= 45 and age <= 55: ##Using and we are checking to see if they are in the age bracket for a mid life crisis
    print("Everything is going to be ok. Have a free ride on us!")
  else:
    bill = 12
    print("Adult tickets are $12.")

  wants_photo = input("Do you want a photo taken? Y or N. ")
  if wants_photo == "Y":
    bill += 3

  print(f"Your final bill is ${bill}")

else:
  print("Sorry, you have to grow taller before you can ride.")

### Next is conditionals with for loop through string |  lowercase a string | Count a letter in a string


#Love Calculator

print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")
score1 = 0
score2 = 0

for ltr in 'true':
  score1 += name1.lower().count(ltr)
  score1 += name2.lower().count(ltr)
for ltr in 'love':
  score2 += name1.lower().count(ltr)
  score2 += name2.lower().count(ltr)

score = int(f"{score1}{score2}")

if score > 90 or score < 10:
  print(f"Your score is {score}, you go together like coke and mentos.")
elif score > 40 and score < 50:
  print(f"Your score is {score}, you are alright together.")
else:
  print(f"Your score is {score}")

### Choose  your own adventure
print('''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')
print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.")

#Write your code below this line 👇

choice1 = input('You\'re at a cross road. Where do you want to go? Type "left" or "right" \n').lower()
if choice1 == "left":
  choice2 = input('You\'ve come to a lake. There is an island in the middle of the lake. Type "wait" to wait for a boat. Type "swim" to swim across. \n').lower()
  if choice2 == "wait":
    choice3 = input("You arrive at the island unharmed. There is a house with 3 doors. One red, one yellow and one blue. Which colour do you choose? \n").lower()
    if choice3 == "red":
      print("It's a room full of fire. Game Over.")
    elif choice3 == "yellow":
      print("You found the treasure! You Win!")
    elif choice3 == "blue":
      print("You enter a room of beasts. Game Over.")
    else:
      print("You chose a door that doesn't exist. Game Over.")
  else:
    print("You get attacked by an angry trout. Game Over.")
else:
  print("You fell into a hole. Game Over.")


### Random
import random #You imust import random

random_integer = random.randint(1, 10) #Random int betwee nthese numbers
random_float = random.random()*5 # random.random gives float between 0 and 1 * 5 is now 0 and 5
print(random_integer)

love_score = random.randint(1, 100)
print(f"Your love score is {love_score}")

random_side = random.randint(0, 1) ##Coin flip random integer
if random_side == 1:
    print("Heads")
else:
    print("Tails")
####################################################################

# Data types
## lists
fruits = ["apple", "orange","pear"] #List data structure

## List of states
states_of_america = ["Delaware", "Pennsylvania", "New Jersey",
                     "Georgia", "Connecticut", "Massachusetts",
                     "Maryland", "South Carolina", "New Hampshire",
                     "Virginia", "New York", "North Carolina",
                     "Rhode Island", "Vermont", "Kentucky", "Tennessee",
                     "Ohio", "Louisiana", "Indiana", "Mississippi",
                     "Illinois", "Alabama", "Maine", "Missouri", "Arkansas",
                     "Michigan", "Florida", "Texas", "Iowa", "Wisconsin",
                     "California", "Minnesota", "Oregon", "Kansas",
                     "West Virginia", "Nevada", "Nebraska", "Colorado",
                     "North Dakota", "South Dakota", "Montana", "Washington",
                     "Idaho", "Wyoming", "Utah", "Oklahoma", "New Mexico",
                     "Arizona", "Alaska", "Hawaii"]

#Change a variable in the list
states_of_america[1] = "Pencilvania"
#You can append items to the list in python
states_of_america.append("Morganland") # Append Method add to a list
states_of_america.extend(["Tonyland", "Troyland"]) #Add a list to a list Extend method
print(states_of_america) #You will notice the list as changed
## List of fruits
dirty_dozen = ["Strawberries", "Spinach", "Kale",
               "Nectarines", "Apples", "Grapes",
               "Peaches", "Cherries", "Pears",
               "Tomatoes", "Celery", "Potatoes"]

#You can seperate and add to lists in any way you want
fruits = ["Strawberries","Nectarines","Apples",
          "Grapes", "Peaches", "Cherries", "Pears",]
vegetables = ["Spinach", "Kale","Tomatoes", "Celery", "Potatoes"]
#You can add them back together like this
dirty_dozens = [fruits, vegetables]
print(dirty_dozens)
## INDEX INFORMATION
# the 0 is the count of the offset of the item, the Strawberries item is offset by 0 because it begins the list.add()

#Application of Random method , len() function, and string formatting
##Decide whos going to pay the meal randomly

names_string = input("Give me everybody's names, separated by a comma. ")
names = names_string.split(", ")

import random

print(f"{names[random.randint(0, (len(names)-1))]} is going to buy the meal today!")


#Below is their version of above
import random

# Split string method
names_string = input("Give me everybody's names, seperated by a comma. ")
names = names_string.split(", ")

#Write your code below this line 👇

#Get the total number of items in list.
num_items = len(names)
#Generate random numbers between 0 and the last index.
random_choice = random.randint(0, num_items - 1)
#Pick out random person from list of names using the random number.
person_who_will_pay = names[random_choice]

print(person_who_will_pay + " is going to buy the meal today!")

#person_who_will_pay = random.choice(names) #This does the same thing as above but doesn't show you understand it.

####### Next Coding Section

#Given the following list:

fruits = ["Strawberries", "Nectarines", "Apples", "Grapes", "Peaches", "Cherries", "Pears"]
#Which line of code will give you "Apples"?
print(fruits[-5]) #This can give you apples just like fruits[2]

##Given the code below:

fruits = ["Strawberries", "Nectarines", "Apples", "Grapes", "Peaches", "Cherries", "Pears"]
fruits[-1] = "Melons" #Grabs the last element of the list
fruits.append("Lemons") #Adds Lemons to the back of the list
print(fruits)
##What do you think will be printed?
["Strawberries", "Nectarines", "Apples", "Grapes", "Peaches", "Cherries", "Melons", "Lemons"]

### Q3
fruits = ["Strawberries", "Nectarines", "Apples", "Grapes", "Peaches", "Cherries", "Pears"]
vegetables = ["Spinach", "Kale", "Tomatoes", "Celery", "Potatoes"]

dirty_dozen = [fruits, vegetables]

print(dirty_dozen[1][1]) #[['Strawberries', 'Nectarines', 'Apples', 'Grapes', 'Peaches', 'Cherries', 'Pears'],
                         #['Spinach', 'Kale', 'Tomatoes', 'Celery', 'Potatoes']]
#Prints Kale since there is two lists within that list

#Lists treasure map exercise

row1 = ["⬜️","⬜️","⬜️"]
row2 = ["⬜️","⬜️","⬜️"]
row3 = ["⬜️","⬜️","⬜️"]
map = [row1, row2, row3]
print(f"{row1}\n{row2}\n{row3}")
position = input("Where do you want to put the treasure? ")

row = position[1]
column = int(position[0]) - 1
if row == '1':
  row1[column] = "X"
elif row == '2':
  row2[column] = "X"
else:
  row3[column] = "X"


print(f"{row1}\n{row2}\n{row3}")

##Their version below GREAT VERSION
# Lists List Copy Affecting data from multiple list in a nested list.
row1 = ["⬜️","️⬜️","️⬜️"]
row2 = ["⬜️","⬜️","️⬜️"]
row3 = ["⬜️️","⬜️️","⬜️️"]
map = [row1, row2, row3]
#print(f"{row1}\n{row2}\n{row3}") ADD NEW LINE TO TEXT

#position = input("Where do you want to put the treasure? ")
position = '23'
horizontal = int(position[0])
vertical = int(position[1])

map[vertical - 1][horizontal - 1] = "X" #The map contains direct copies of the rows and thus can be edited

print(f"{row1}\n{row2}\n{row3}") #new line example


## Rock Paper Scissors PYTHON

rock = '''
Rock!
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
Paper!
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
Scissors!
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

#Write your code below this line 👇
import random
choices = [rock, paper, scissors]

def rockPaperScissors():
  Choice = int(input("What do you choose?\nType 0 for Rock, 1 for Paper or 2 for Scissors: "))

  aiChoice = random.randint(0, 2)
  #print(f"You chose {choices[Choice]}")
  #print(f"AI chose {choices[aiChoice]}")
  if Choice == aiChoice:
    print(f"You chose {choices[Choice]}\nAI chose {choices[aiChoice]}\n IT IS A TIE. Next Round!\n")
    rockPaperScissors()
  elif Choice > 2 or Choice < 0:
    print("You must choose \n0 for Rock, \n1 for Paper, \nand 2 for Scissors.")
    rockPaperScissors()
  elif (Choice == 0 and aiChoice == 2) or (Choice == 1 and aiChoice == 0) or (Choice == 2 and aiChoice == 1):
    print(f"You chose {choices[Choice]}\nAI chose                {choices[aiChoice]}\n Next round!\n")
    print("You win!")
  else:
    print(f"You chose {choices[Choice]}\nAI chose                {choices[aiChoice]}\n Next round!\n")
    print("You lose!")

  playAgain = input("Would you like to play again?\nType Y or N to answer: ").lower()

  if playAgain == 'y':
    rockPaperScissors()
  elif playAgain == 'n':
    print("Thanks for playing!")
    return
  else:
    print("You didn't answer a valid response! Thanks for playing")




rockPaperScissors()

## Their RPS code
import random

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

game_images = [rock, paper, scissors]

user_choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n"))
print(game_images[user_choice])

computer_choice = random.randint(0, 2)
print("Computer chose:")
print(game_images[computer_choice])

if user_choice >= 3 or user_choice < 0:
  print("You typed an invalid number, you lose!")
elif user_choice == 0 and computer_choice == 2:
  print("You win!")
elif computer_choice == 0 and user_choice == 2:
  print("You lose")
elif computer_choice > user_choice:
  print("You lose")
elif user_choice > computer_choice:
  print("You win!")
elif computer_choice == user_choice:
  print("It's a draw")

## Day 4 end

#Loops for loop
fruits = ["Apple", "Peach", "Pear"]
for fruit in fruits:
  print(fruit) #This is a simple python for loop
  print(fruit + " Pie") # You Can append all elements
  print(fruits) #This prints the whole list
#Loops exercise 1 below

student_heights = input("Input a list of student heights ").split()
for n in range(0, len(student_heights)):
  student_heights[n] = int(student_heights[n])

total = 0

for x in student_heights:
  total += x

print(int(total / len(student_heights)))



student_heights = input("Input a list of student heights ").split() #Split takes away spaces by default to create a list of each number
for n in range(0, len(student_heights)):
  student_heights[n] = int(student_heights[n])
# print(student_heights)


total_height = 0
for height in student_heights:
  total_height += height
print(f"total height = {total_height}")

number_of_students = 0
for student in student_heights:
  number_of_students += 1
print(f"number of students = {number_of_students}")

average_height = round(total_height / number_of_students)
print(average_height)



#### Finding the highest score
### Using loop if formatted string f-string

student_scores = input("Input a list of student scores ").split()
for n in range(0, len(student_scores)):
  student_scores[n] = int(student_scores[n])
print(student_scores)

highest = 0

for n in student_scores:
    if highest < n:
        highest = n


print(f"The highest score in the class is: {highest}")

## for loops range function HOW TO USE RANGE
# A for loop using range
for number in range(1, 13, 3): #Prints all the numbers starting at 1 and ending once the number hits >=13 The extra number determines the step to be 3 I.E. 1 4 7 10
    print(number)

total = 0
for number in range(1, 101): #You can count to 100 and add each number together by flipping the two 50 in half. 100 + 1 is 101, 99 + 2 is 101 and so on. 50 pairs of 101 OR 50 X 101? 10 X 101 = 1010 X 5 = 5050
    total += number

#print(total)


for number in range(1, 101): #You can count to 100 and add each number together by flipping the two 50 in half. 100 + 1 is 101, 99 + 2 is 101 and so on. 50 pairs of 101 OR 50 X 101? 10 X 101 = 1010 X 5 = 5050
    total += number

#print(total)

##Even numbers only using steps

total = 0
for number in range(2, 101, 2): #Two ways to count in even numbers, this is the best one since it skips unwanted numbers
    total += number

total2 = 0
for number in range(1, 101):
    if number % 2 == 0:
        total2+=number

print(total2)


for n in range(1, 100): #Simple fizz buzz for loop
    if n % 5 == 0 and n % 3 == 0:
        print("FizzBuzz")
    elif n % 3 == 0:
        print("Fizz")
    elif n % 5 == 0:
        print("Buzz")
    else:
        print(n)
##Password generator applying the things I have learned

###My version
#Password Generator Project
import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm',
           'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z',
           'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M',
           'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']

numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']

symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters= int(input("How many letters would you like in your password?\n"))
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

#Eazy Level - Order not randomised:
#e.g. 4 letter, 2 symbol, 2 number = JduE&!91


#Hard Level - Order of characters randomised:
#e.g. 4 letter, 2 symbol, 2 number = g^2jk8&P
import random

password = ""

while nr_letters > 0 or nr_symbols > 0 or nr_numbers > 0:
  if nr_letters > 0:
    nr_letters -= 1
    password += letters[random.randint(0, len(letters)-1)]
  elif nr_symbols > 0:
    nr_symbols -= 1
    password += symbols[random.randint(0, len(symbols)-1)]
  elif nr_numbers > 0:
    nr_numbers -= 1
    password += numbers[random.randint(0, len(numbers)-1)]

print(password, type(password))
password = list(password)
print(password, type(password))
for x in range(0, len(password)): #There is a shuffle function
  letr1 = password[x]
  randomNum = random.randint(0, len(password)-(x+1))
  letr2 = password[randomNum]
  password[x] = letr2
  password[randomNum] = letr1

password = ''.join(password)
print(password, type(password))


## Their version Random List Loop For Loop While Loop Password Range Join Method Shuffle Function

#Password Generator Project
import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters = int(input("How many letters would you like in your password?\n"))
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

password_list = []

for char in range(1, nr_letters + 1):
  password_list.append(random.choice(letters)) # Random . Choice Chooses randomly from the lists above REALLY USEFUL

for char in range(1, nr_symbols + 1):
  password_list += random.choice(symbols)

for char in range(1, nr_numbers + 1):
  password_list += random.choice(numbers)

print(password_list)
random.shuffle(password_list) # Shuffles a list for me instead of having to use the function I wrote above.
print(password_list)

password = ""
for char in password_list:
  password += char

print(f"Your password is: {password}")


## Python Functions

def mingin(): # The colon says new line.
    print('hey')
    print('bye')

mingin()


### While loops LOOPS
# While something=true
number = 6 #While loop python
while number > 0:
    print('hey')
    number -= 1

# You can use while loops to run until something happens while not at_goal(): #This one only stops once the goal is reached, while 5>3orTrue: #This will never stop
#Reeborg Jump Hurdles Function
def turn_right():
    turn_left()
    turn_left()
    turn_left()
def jump():
    turn_left()
    while not right_is_clear():
        move()
    turn_right()
    move()
    turn_right()
    while front_is_clear():
        move()
    turn_left()


while not at_goal():
    if front_is_clear():
        move()
    else:
        jump()
