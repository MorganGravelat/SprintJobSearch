#Try CTRL+F to see the keywords I scattered around. Search imports for examples of good import statements




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


##Additional from reeborg
    else:
        if wall_on_right() and wall_in_front():
            turn_left()
        else:
            turn_right()



###DAY 7 Hangman
#Process
#START -> GENERATE A WORD RANDOMLY -> Generate as many blanks as letters in word -> Ask for letter guess from user --
# --> Is the letter correct? -> NO? Lose a life -> Have they run out of lives? -> YES? You Lose
#                                                                                  NO? Go BACK to ask for letter guess from user
#                             -> YES? Replace blanks with letter -> Are blanks all filled? -> NO? GO BACK TO Ask for letter guess from user
#                                                                                             YES? You Win

''' Hangman prototype
while score > 0:
      guess = input("Pick a letter: ").lower()
  if len(guess) == 1:
    if guess in word:
      print("This letter is in")
    else:
      score -= 1
      if score != 0:
        print(f"This letter is not in, you new score is {score}")
      else:
        print(f"Your score is {score} SO YOU LOSE!")
  else:
    print('You input an invalid guess, please provide just one letter!')
'''

#My Code so far!
#Step 1

word_list = ["aardvark", "baboon", "camel"]

#TODO-1 - Randomly choose a word from the word_list and assign it to a variable called chosen_word.

#TODO-2 - Ask the user to guess a letter and assign their answer to a variable called guess. Make guess lowercase.

#TODO-3 - Check if the letter the user guessed (guess) is one of the letters in the chosen_word.
import random
word = word_list[random.randint(0, len(word_list) - 1)]
print(word)
score = 6
display = []
guesses = ''

while len(word) > len(display):
  display.append('_')
print(f"{display}\n{stages[score]}")


while score > 0:
  guess = input("Pick a letter: ").lower()
  if guess in guesses and len(guess) == 1:
    print("You already made that guess?!")
  elif len(guess) == 1:
    guesses+=guess
    if guess in word:
      for x in range(len(word)):
        if guess == word[x]:
          display[x] = guess
      print(f"You got it right! {guess} is in there! \n{display}\n{stages[score]}")
      if '_' not in display:
        print('You WIN!')
        break
    else:
      score -= 1
      print(f"There are no {guess}'s, your new score is {score}")
      print(f"{display}\n{stages[score]}")
  else:
    print('You input an invalid guess, please provide just one letter!')

if score == 0:
  print(f"Your score is {score} SO YOU LOSE!\n {stages[score]}", display)

############################################################################

stages = ['''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========
''', '''
  +---+
  |   |
      |
      |
      |
      |
=========
''']

logo = '''
 _
| |
| |__   __ _ _ __   __ _ _ __ ___   __ _ _ __
| '_ \ / _` | '_ \ / _` | '_ ` _ \ / _` | '_ \
| | | | (_| | | | | (_| | | | | | | (_| | | | |
|_| |_|\__,_|_| |_|\__, |_| |_| |_|\__,_|_| |_|
                    __/ |
                   |___/    '''

word_list = [
'abruptly',
'absurd',
'abyss',
]


'''
Using the files above in another Python file structure.
Completed next step of hangman for user experience
#Step 5

import random
from hangman_words import word_list
from hangman_art import stages, logo

#TODO-1: - Update the word list to use the 'word_list' from hangman_words.py
#Delete this line: word_list = ["ardvark", "baboon", "camel"]
chosen_word = random.choice(word_list)
word_length = len(chosen_word)
guesses = ''

end_of_game = False
lives = 6

#TODO-3: - Import the logo from hangman_art.py and print it at the start of the game.
print(logo)
#Testing code
print(f'Pssst, the solution is {chosen_word}.')

#Create blanks
display = []
for _ in range(word_length):
    display += "_"

while not end_of_game:
    guess = input("Guess a letter: ").lower()

    #TODO-4: - If the user has entered a letter they've already guessed, print the letter and let them know.
    if len(guess) == 1 and guess in guesses:
      print(f'You already guessed {guess.upper()}')
      continue
    else:
      guesses += guess
    #Check guessed letter
    for position in range(word_length):
        letter = chosen_word[position]
        #print(f"Current position: {position}\n Current letter: {letter}\n Guessed letter: {guess}")
        if letter == guess:
            display[position] = letter

    #Check if user is wrong.
    if guess not in chosen_word:
        #TODO-5: - If the letter is not in the chosen_word, print out the letter and let them know it's not in the word.
        lives -= 1
        print(f"{guess.upper()} is a bad guess! You have {lives} lives left!")
        if lives == 0:
            end_of_game = True
            print("You lose.")

    #Join all the elements in the list and turn it into a String.
    print(f"{' '.join(display)}")

    #Check if user has got all letters.
    if "_" not in display:
        end_of_game = True
        print("You win.")

    #TODO-2: - Import the stages from hangman_art.py and make this error go away.
    print(stages[lives])
'''

#Simple variables inside function def block
##Input print functions
def greet():
    name = input("What is your name? ")
    print(f"Hello {name}!")
    print(f"How do you do {name}?")
    print(f"Well see yuh later {name}!")

greet()

## Function that allows for input
name = input("What is your name? ")
def greet_with_name(name):
    print(f"Hello {name}!")
    print(f"How do you do {name}?")
    print(f"Well see yuh later {name}!")

greet_with_name(name)

name = input("What is your name? ")
location = input("Where do you live? ")
def greet_with(name, location):
    print(f"Hello {name}!")
    print(f"How is {location}?")
    print(f"Well see yuh later {name}!")

greet_with(name, location) #position matters here name must be in name location and location in its proper spot

#You can use Keyword Arguments
# DEFINING ARGUMENTS SPECIFICALLY
greet_with(location = location, name = name)

#Using Keyword Arguments
#Testing how much paint you need for a job
test_h = int(input("Height of wall: "))
test_w = int(input("Width of wall: "))
coverage = 5
def paint_calc(height, width, cover):
  cans_needed = (height * width) / cover
  print(f"You'll need {int(cans_needed)} cans of paint.")

paint_calc(height=test_h, width=test_w, cover=coverage)
##Prime number identification
import math #Math import

def prime_checker(number):
  if number == 2:
    return "It's a prime number"
  elif number % 2 == 0 or number < 2:
    return "It's not a prime number"

  for i in range(3, math.floor(math.sqrt(number)) + 1, 2): #floor sqrt square root math operators
    if number % i == 0:
      return "It's not a prime number"
  return "It's a prime number"


n = int(input("Check this number: "))
print(prime_checker(number=n))

####Basic use of input and array positioning for encyrption
direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))
def encrypt(text, shift):
  alphabet = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
  newWord = ''
  for ltr in text:
    ind = alphabet.index(ltr.lower()) + shift
    if ind >= len(alphabet):
      ind -= 26
    newWord += alphabet[ind]

  return newWord

print(encrypt(text, shift))


##Belowis their version of basic cipher##
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))

#Don't change the code above 👆

#TODO-1: Create a function called 'encrypt' that takes the 'text' and 'shift' as inputs.
def encrypt(plain_text, shift_amount):
  #TODO-2: Inside the encrypt function, shift each letter of the text forwards in the alphabet by the shift amount and print the encrypted text.
  #e.g.
  #plain_text = "hello"
  #shift = 5
  #cipher_text = "mjqqt"
  #print output: "The encoded text is mjqqt"
  cipher_text = ""
  for letter in plain_text:
    position = alphabet.index(letter)
    new_position = position + shift_amount
    new_letter = alphabet[new_position]
    cipher_text += new_letter
  print(f"The encoded text is {cipher_text}")

#TODO-3: Call the encrypt function and pass in the user inputs. You should be able to test the code and encrypt a message.
encrypt(plain_text=text, shift_amount=shift)

################# part 2 Cipher
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))

def encrypt(plain_text, shift_amount):
  cipher_text = ""
  for letter in plain_text:
    position = alphabet.index(letter)
    new_position = position + shift_amount
    cipher_text += alphabet[new_position]
  print(f"The encoded text is {cipher_text}")


def decrypt(text, shift):
  decrypted_text=""
  for letter in text:
    position = alphabet.index(letter)
    new_position = position - shift
    decrypted_text += alphabet[new_position]
  print(f'Decrypted text is: "{decrypted_text}"')
#TODO-1: Create a different function called 'decrypt' that takes the 'text' and 'shift' as inputs.

  #TODO-2: Inside the 'decrypt' function, shift each letter of the 'text' *backwards* in the alphabet by the shift amount and print the decrypted text.
  #e.g.
  #cipher_text = "mjqqt"
  #shift = 5
  #plain_text = "hello"
  #print output: "The decoded text is hello"


#TODO-3: Check if the user wanted to encrypt or decrypt the message by checking the 'direction' variable. Then call the correct function based on that 'drection' variable. You should be able to test the code to encrypt *AND* decrypt a message.
if direction == 'encode':
  encrypt(plain_text=text, shift_amount=shift)
elif direction == 'decode':
  decrypt(text=text, shift=shift)

#######THEIRS
def decrypt(cipher_text, shift_amount):
  plain_text = ""
  for letter in cipher_text:
    position = alphabet.index(letter)
    new_position = position - shift_amount
    plain_text += alphabet[new_position]
  print(f"The decoded text is {plain_text}")



###Part 2 End


###Part 3 Start COMBINED function called casear()
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))

#TODO-1: Combine the encrypt() and decrypt() functions into a single function called caesar().
def caesar(text, shift, direction):
  if direction != 'decode' and direction != 'encode':
    print('Please fill the direction with encode or decode.')
    return
  if shift > 26:
    print('Shift can not be greater than 26')
    return
  cipher_text = ""
  if direction == 'decode':
    shift = -shift
  for letter in text:
    position = alphabet.index(letter)
    new_position = position + shift
    cipher_text += alphabet[new_position]
  print(f"The {direction}d text is {cipher_text}")

#TODO-2: Call the caesar() function, passing over the 'text', 'shift' and 'direction' values.

caesar(text, shift, direction)
###COURSES WORK
def caesar(start_text, shift_amount, cipher_direction):
      end_text = ""
  if cipher_direction == "decode":
      shift_amount *= -1
  for letter in start_text:
    position = alphabet.index(letter)
    new_position = position + shift_amount
    end_text += alphabet[new_position]
  print(f"Here's the {direction}d result: {end_text}")

###Part 3 End

###Part 4 QOL IF FUNCTIONS WHILE LOOP INPUT MODULO
from art import logo

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

game_going = True

def caesar(start_text, shift_amount, cipher_direction):
  end_text = ""
  if cipher_direction != 'decode' and cipher_direction != 'encode':
    print('Please fill the direction with encode or decode.')
    return
  if shift_amount > 26:
    shift_amount %= 26
  if cipher_direction == "decode":
    shift_amount *= -1
  for char in start_text:

    if char in alphabet:
      position = alphabet.index(char)
      new_position = position + shift_amount
      end_text += alphabet[new_position]
    else:
      end_text += char

  print(f"Here's the {cipher_direction}d result: {end_text}")

while game_going == True:
  print(logo)
  direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
  text = input("Type your message:\n").lower()
  shift = int(input("Type the shift number:\n"))

  caesar(start_text=text, shift_amount=shift, cipher_direction=direction)

  go_again = input("Do you want to go again? Type Y if you wish to go again and anything else at all if not").lower()
  if (go_again != 'y'):
    print("Thanks for playing!")
    game_going = False


### Dictionary in python DICT

'''
{Key: Value} Pairs / The key is what you lookup and the value is what it stores.
{Bug: An error in a program that prevents the program from running as expected}
For multiple items in dict always cap off the items with a comma ,
{'A': 'HEY THERE', 'B': 'Oh well!',}
'''
##You can run simple loops on dicts like this
student_scores = {
  "Harry": 81,
  "Ron": 78,
  "Hermione": 99,
  "Draco": 74,
  "Neville": 62,
}

student_grades = {}

for key in student_scores:
  if student_scores[key] <= 70:
    student_grades[key] = 'Fail'
  elif student_scores[key] <= 80:
    student_grades[key] = 'Acceptable'
  elif student_scores[key] <= 90:
    student_grades[key] = 'Exceeds Expectations'
  else:
    student_grades[key] = 'Outstanding'

print(student_grades)


##You can nest lists in dictionarys and vice versa

hello = [{1:2, 3:4, 5:6,},{7:8, 9:10, 11:12,}]

travel_log = [
{
  "country": "France",
  "visits": 12,
  "cities": ["Paris", "Lille", "Dijon"]
},
{
  "country": "Germany",
  "visits": 5,
  "cities": ["Berlin", "Hamburg", "Stuttgart"]
},
]


def add_new_country(country, visits, cities): #Adds a new country to the list of dicts
  new_country = {}
  new_country["country"] = country
  new_country["visits"] = visits
  new_country["cities"] = cities
  travel_log.append(new_country)


add_new_country("Russia", 2, ["Moscow", "Saint Petersburg"])
print(travel_log)

#If you try
#With this nested Dict
order = {
    "starter": {1: "Salad", 2: "Soup"},
    "main": {1: ["Burger", "Fries"], 2: ["Steak"]},
    "dessert": {1: ["Ice Cream"], 2: []},
}
# To access steak you would have to print(order["main"][2][0]) the "main" key is first
# followed by the 2 key and then the 0 index of the array
##Bidding with a dictionary
from replit import clear
#HINT: You can call clear() to clear the output in the console.

def highest(dict):
  highest_bid = 0
  highest_bidder = ''
  for key in dict:
    if dict[key] > highest_bid:
      highest_bid = dict[key]
      highest_bidder = key
  print(f"The item goes to {highest_bidder} with a bid of {highest_bid}!")
bidding = True
bids = {}

while bidding == True: #While loop to keep the bids going as long as there are people to bid.
  name = input("What is your name? ")
  bid = int(input("How much are you bidding? "))

  bids[name] = bid

  more = input("Are there any more bids? Type Y for yes and N for no: ").lower()
  if more != "y":
    highest(bids)
    bidding = False
  else:
      clear() #Clear clears the console
##Below is testing and multiple return statements
def is_leap(year):
      if year % 4 == 0:
    if year % 100 == 0:
      if year % 400 == 0:
        return True
      else:
        return False
    else:
        return True
  else:
    return False
##DOCS STRING
def days_in_month(year, month):
  '''This function takes the year and month you input and checks to see #This is a doc string and will pop up when hovering over your function!
  if it is a leap year and then returns the number of days in that month.'''
  month_days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
  if month > 12 or month < 1:
    return "Invalid month entered."
  if month == 2 and is_leap(year):
    return 29
  return month_days[month - 1]

# IEH
# DIOAJOJa
# AOIFJ Ctrl+/ Will comment out lines of code that are selected

#Do NOT change any of the code below 👇
year = int(input("Enter a year: "))
month = int(input("Enter a month: "))
days = days_in_month(year, month)
print(days)

# Tests
import unittest

class MyTest(unittest.TestCase):

    def test_1(self):
        self.assertEqual(days_in_month(2018, 2), 28)

    def test_2(self):
        self.assertEqual(days_in_month(2020, 2), 29)

    def test_3(self):
        self.assertEqual(days_in_month(2019, 4), 30)

    def test_4(self):
        self.assertEqual(days_in_month(1045, 5), 31)

print("\n")
print('Running some tests on your code:')
print(".\n.\n.\n.")
unittest.main(verbosity=1, exit=False)

def add(n1, n2):
      return n1 + n2

def subtract(n1, n2):
  return n1 - n2

def multiply(n1, n2):
  return n1 * n2

def divide(n1, n2):
  return n1 / n2

print(add(2, multiply(5, divide(8, 4)))) #Returns 12.0 FLOAT because it is a math equation

##You can return a function call from within your function
def outer_function(a, b):
    def inner_function(c, d):
        return c + d
    return inner_function(a, b)

result = outer_function(5, 10)
print(result)

##CALCULATOR
from replit import clear

def adder(num1,num2):
  return num1 + num2
def subtracter(num1,num2):
  return num1 - num2
def multiplier(num1,num2):
  return num1 * num2
def divider(num1,num2):
  return num1 / num2
operations = {'/': divider,'*': multiplier, '+': adder, '-': subtracter}

calculating = True


while calculating == True:

  num1 = int(input("What is the first number? "))
  operation = input("What operation will you use? * / + - : ")
  num2 = int(input("What is the second number? "))

  print(f"{num1} {operation} {num2} = {operations[operation](num1,num2)}")

  again = input("Would you like to keep calculating? Type Y for yes and N for no: ").lower()
  if again != 'y':
    print("Thanks for using the calculator stupid fucking piece of shit!")
    calculating = False
  else:
    clear()
###Final calculator below

from replit import clear
from art import logo

def add(n1, n2):
  return n1 + n2

def subtract(n1, n2):
  return n1 - n2

def multiply(n1, n2):
  return n1 * n2

def divide(n1, n2):
  return n1 / n2

operations = {
  "+": add,
  "-": subtract,
  "*": multiply,
  "/": divide
}

def calculator():
  print(logo)

  num1 = float(input("What's the first number?: "))
  for symbol in operations:
    print(symbol)
  should_continue = True

  while should_continue:
    operation_symbol = input("Pick an operation: ")
    num2 = float(input("What's the next number?: "))
    calculation_function = operations[operation_symbol]
    answer = calculation_function(num1, num2)
    print(f"{num1} {operation_symbol} {num2} = {answer}")

    if input(f"Type 'y' to continue calculating with {answer}, or type 'n' to start a new calculation: ") == 'y':
      num1 = answer
    else:
      should_continue = False
      clear()
      calculator()

calculator()
####Next module
#Blackjack rules
#Ace is 1 or 11
#Tie score = draw
# Over 21 means you lose
#
#ExperimentalBlackjack
game_going = True
card_suits = ['of Diamonds','of Clubs','of Hearts','of Spades']
cards = [[2,'Two',3],[3,'Three',3],[4,'Four',3],
         [5,'Five',3],[6,'Six',3],[7,'Seven',3],
         [8,'Eight',3],[9, 'Nine',3],[10, 'Ten',3],
         [10, 'Jack',3],[10, 'Queen',3],[10, 'King',3],
         [11, 'Ace',3]]

while game_going == True:
  deck = cards.shuffle()
  i = 0
  user_hand = [deck[i],deck[i+1]]
  dealer_hand = [deck[i+2],deck]
  for card in cards:


#Blackjack

##Completed Project

############### Our Blackjack House Rules #####################

## The deck is unlimited in size.
## There are no jokers.
## The Jack/Queen/King all count as 10.
## The the Ace can count as 11 or 1.
## Use the following list as the deck of cards:
## cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
## The cards in the list have equal probability of being drawn.
## Cards are not removed from the deck as they are drawn.


import random
from replit import clear
logo = """
.------.            _     _            _    _            _
|A_  _ |.          | |   | |          | |  (_)          | |
|( \/ ).-----.     | |__ | | __ _  ___| | ___  __ _  ___| | __
| \  /|K /\  |     | '_ \| |/ _` |/ __| |/ / |/ _` |/ __| |/ /
|  \/ | /  \ |     | |_) | | (_| | (__|   <| | (_| | (__|   <
`-----| \  / |     |_.__/|_|\__,_|\___|_|\_\ |\__,_|\___|_|\_\\
      |  \/ K|                            _/ |
      `------'                           |__/
"""

def deal_card():
  """Returns a random card from the deck."""
  cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
  card = random.choice(cards)
  return card


def calculate_score(cards):
  """Take a list of cards and return the score calculated from the cards"""

  if sum(cards) == 21 and len(cards) == 2:
    return 0

  if 11 in cards and sum(cards) > 21:
    cards.remove(11) ##REMOVE can remove specific thing from list
    cards.append(1)
  return sum(cards)

def compare(user_score, computer_score):
  #Bug fix. If you and the computer are both over, you lose.
  if user_score > 21 and computer_score > 21:
    return "You went over. You lose 😤"


  if user_score == computer_score:
    return "Draw 🙃"
  elif computer_score == 0:
    return "Lose, opponent has Blackjack 😱"
  elif user_score == 0:
    return "Win with a Blackjack 😎"
  elif user_score > 21:
    return "You went over. You lose 😭"
  elif computer_score > 21:
    return "Opponent went over. You win 😁"
  elif user_score > computer_score:
    return "You win 😃"
  else:
    return "You lose 😤"

def play_game():

  print(logo)

  user_cards = []
  computer_cards = []
  is_game_over = False

  for _ in range(2):
    user_cards.append(deal_card())
    computer_cards.append(deal_card())


  while not is_game_over:

    user_score = calculate_score(user_cards)
    computer_score = calculate_score(computer_cards)
    print(f"   Your cards: {user_cards}, current score: {user_score}")
    print(f"   Computer's first card: {computer_cards[0]}")

    if user_score == 0 or computer_score == 0 or user_score > 21:
      is_game_over = True
    else:
      user_should_deal = input("Type 'y' to get another card, type 'n' to pass: ")
      if user_should_deal == "y":
        user_cards.append(deal_card())
      else:
        is_game_over = True


  while computer_score != 0 and computer_score < 17:
    computer_cards.append(deal_card())
    computer_score = calculate_score(computer_cards)

  print(f"   Your final hand: {user_cards}, final score: {user_score}")
  print(f"   Computer's final hand: {computer_cards}, final score: {computer_score}")
  print(compare(user_score, computer_score))


while input("Do you want to play a game of Blackjack? Type 'y' or 'n': ") == "y":
  clear()
  play_game()


##SCOPE local scope global scope globalscope localscope

enemies = 1 # Global scope

def increase_enemies():
    enemies = 2 # Local Scope
    print(f"enemies inside function: {enemies}") #Local scope exists within functions, this assignment of enemies is only in here

increase_enemies()
print(f"enemies outisde function: {enemies}")

def drink_potion():
    potion_strength = 2
    print(potion_strength)

drink_potion()
print(potion_strength)

#####################################################

game_level = 3
def create_enemy():
    enemies = ["Skeleton", "Zombie", "Alien"]
    if game_level < 5:
       new_enemy = enemies[0]

print(enemies) #This is a name error

enemies = "Skeleton"



enemies = 1 #Creating a varialbe called enemies and setting it equal to 1


def increase_enemies():
    global enemies #You can set a global variable inside a function like this. Cannot modify without this
    #This also allows you to set the global variable within the function like so
    enemies += 2
    #It checks for enemies here then outside if there is none in here
    print(f"enemies inside function: {enemies}") #enemies = 3

increase_enemies()
print(f"enemies outside function: {enemies}") # enemies = 3

##### Return statements
enemies = 1

def increase_enemies():
    return enemies + 2 #Takes globally scoped enemies and modifies the value with a return statement in the code
    #It checks for enemies here then outside if there is none in here
    print(f"enemies inside function: {enemies}") #enemies = 3

enemies = increase_enemies() #Assign the variable
print(f"enemies outside function: {enemies}") # enemies = 3

########################
game_level = 3
enemies = ["Skeleton", "Zombie", "Alien"]

def create_enemy():
    enemies = ["Skeleton", "Zombie", "Alien"]
    if game_level < 5:
        new_enemy = enemies[0]

if game_level < 5: #This will show up but the function won't
        new_enemy = enemies[0]

print(new_enemy)


####
enemies = 1

def create_enemy():
    enemies += 1
    if game_level < 5:
        new_enemy = enemies[0]

if game_level < 5: #This will show up but the function won't
        new_enemy = enemies[0]

print(new_enemy)

#####
#Global Constants
#Var define that you will never change
PI = 3.14159 #the naming convention is all caps
URL = 'https://www.google.com'
TWITTER_HANDLE = "@morgan_g"

def calc():
    print(pi * 2)

calc()


def bar():
    my_variable = 9

    if 16 > 9:
      my_variable = 16 #This alters the variable because in python there is no block scope,
      #inside the if is the same as outside as far as scope is concerned

    print(my_variable)

bar()

########################################################Guess the number game
from random import randint
from art import logo

EASY_LEVEL_TURNS = 10
HARD_LEVEL_TURNS = 5

#Function to check user's guess against actual answer.
def check_answer(guess, answer, turns):
  """checks answer against guess. Returns the number of turns remaining."""
  if guess > answer:
    print("Too high.")
    return turns - 1
  elif guess < answer:
    print("Too low.")
    return turns - 1
  else:
    print(f"You got it! The answer was {answer}.")

#Make function to set difficulty.
def set_difficulty():
  level = input("Choose a difficulty. Type 'easy' or 'hard': ")
  if level == "easy":
    return EASY_LEVEL_TURNS
  else:
    return HARD_LEVEL_TURNS

def game():
  print(logo)
  #Choosing a random number between 1 and 100.
  print("Welcome to the Number Guessing Game!")
  print("I'm thinking of a number between 1 and 100.")
  answer = randint(1, 100)
  print(f"Pssst, the correct answer is {answer}")

  turns = set_difficulty()
  #Repeat the guessing functionality if they get it wrong.
  guess = 0
  while guess != answer:
    print(f"You have {turns} attempts remaining to guess the number.")

    #Let the user guess a number.
    guess = int(input("Make a guess: "))

    #Track the number of turns and reduce by 1 if they get it wrong.
    turns = check_answer(guess, answer, turns)
    if turns == 0:
      print("You've run out of guesses, you lose.")
      return
    elif guess != answer:
      print("Guess again.")


game()

#Use a Debugger
def mutate(a_list):
  b_list = []
  for item in a_list:
    new_item = item * 2
  b_list.append(new_item)
  print(b_list)

mutate([1,2,3,5,8,13])
#Use a Debugger
def mutate(a_list):
  b_list = []
  for item in a_list:
    new_item = item * 2
    b_list.append(new_item)
  print(b_list)

mutate([1,2,3,5,8,13])


####Instagram higher and lower game // This is all your code
from game_data import data
from art import logo,vs
import random
from replit import clear

def makeGuess(answer, A,B):
  guess = input("Who has more followers? Type 'A' or 'B': ").lower()
  while guess != 'a' and guess != 'b':
    guess = input("Please Type 'A' or 'B': ").lower()
  letter = 'a' if answer == A else 'b'
  if guess != letter:
    clear()
    print(logo)
    print(f"Sorry, that's wrong. Final score: {game.score}")
    again = input("\nWould you like to play again? Type Y or N: ").lower()
    if again != 'y':
      game.game_going = False
    else:
      clear()
      game.score = 0
      game.winner = ''
  else:
    clear()
    game.winner = answer
    game.score += 1

def moreFollowers(A,B):
  if A['follower_count'] > B['follower_count']:
    return A
  else:
    return B

def game():
  game.game_going = True
  game.score = 0
  answer = ''
  game.winner = ''
  while game.game_going == True:

    print(logo)


    ind_one = random.randint(0, len(data)-1)
    ind_two = random.randint(0, len(data)-1)
    A = data[ind_one] if game.winner == '' else game.winner
    B = data[ind_two]

    answer = moreFollowers(A,B)

    if game.score > 0: print(f"You're right! Current score: {game.score}.")

    print(f"Compare A: {A['name']}, a {A['description']}, from {A['country']}.")
    print(vs)
    print(f"Against B: {B['name']}, a {B['description']}, from {B['country']}.")

    makeGuess(answer, A,B)

game()

'''
    {
        'name': 'Cristiano Ronaldo',
        'follower_count': 215,
        'description': 'Footballer',
        'country': 'Portugal'
    },
'''
## Their guessing game for comparison

from game_data import data
import random
from art import logo, vs
from replit import clear

def get_random_account():
  """Get data from random account"""
  return random.choice(data)

def format_data(account):
  """Format account into printable format: name, description and country"""
  name = account["name"]
  description = account["description"]
  country = account["country"]
  # print(f'{name}: {account["follower_count"]}')
  return f"{name}, a {description}, from {country}"

def check_answer(guess, a_followers, b_followers):
  """Checks followers against user's guess
  and returns True if they got it right.
  Or False if they got it wrong."""
  if a_followers > b_followers:
    return guess == "a"
  else:
    return guess == "b"


def game():
  print(logo)
  score = 0
  game_should_continue = True
  account_a = get_random_account()
  account_b = get_random_account()

  while game_should_continue:
    account_a = account_b
    account_b = get_random_account()

    while account_a == account_b:
      account_b = get_random_account()

    print(f"Compare A: {format_data(account_a)}.")
    print(vs)
    print(f"Against B: {format_data(account_b)}.")

    guess = input("Who has more followers? Type 'A' or 'B': ").lower()
    a_follower_count = account_a["follower_count"]
    b_follower_count = account_b["follower_count"]
    is_correct = check_answer(guess, a_follower_count, b_follower_count)

    clear()
    print(logo)
    if is_correct:
      score += 1
      print(f"You're right! Current score: {score}.")
    else:
      game_should_continue = False
      print(f"Sorry, that's wrong. Final score: {score}")

game()



########################################################Coffee machine#############################################################
MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}

profit = 0
resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}


def is_resource_sufficient(order_ingredients):
    """Returns True when order can be made, False if ingredients are insufficient."""
    for item in order_ingredients:
        if order_ingredients[item] > resources[item]:
            print(f"​Sorry there is not enough {item}.")
            return False
    return True


def process_coins():
    """Returns the total calculated from coins inserted."""
    print("Please insert coins.")
    total = int(input("how many quarters?: ")) * 0.25
    total += int(input("how many dimes?: ")) * 0.1
    total += int(input("how many nickles?: ")) * 0.05
    total += int(input("how many pennies?: ")) * 0.01
    return total


def is_transaction_successful(money_received, drink_cost):
    """Return True when the payment is accepted, or False if money is insufficient."""
    if money_received >= drink_cost:
        change = round(money_received - drink_cost, 2)
        print(f"Here is ${change} in change.")
        global profit
        profit += drink_cost
        return True
    else:
        print("Sorry that's not enough money. Money refunded.")
        return False


def make_coffee(drink_name, order_ingredients):
    """Deduct the required ingredients from the resources."""
    for item in order_ingredients:
        resources[item] -= order_ingredients[item]
    print(f"Here is your {drink_name} ☕️. Enjoy!")


is_on = True

while is_on:
    choice = input("​What would you like? (espresso/latte/cappuccino): ")
    if choice == "off":
        is_on = False
    elif choice == "report":
        print(f"Water: {resources['water']}ml")
        print(f"Milk: {resources['milk']}ml")
        print(f"Coffee: {resources['coffee']}g")
        print(f"Money: ${profit}")
    else:
        drink = MENU[choice]
        if is_resource_sufficient(drink["ingredients"]):
            payment = process_coins()
            if is_transaction_successful(payment, drink["cost"]):
                make_coffee(choice, drink["ingredients"])


#############################################################Object Oriented Programming#############################################################

#car = CarBlueprint() assigning a new instance of a car class if that exists
from another_module import another_variable
print(another_variable)

import random

from turtle import Turtle, Screen #Example of turtle module that is not in the standard library


Jake = Turtle() #Creating a new instance of a turtle class
Jake.shape("turtle") #Changes the shape of the turtle
Jake.color('black', 'red') #Changes the color of the turtle
Jake.begin_fill() #Begins the fill of the turtle
i = 0 #Initializing a variable
yes = True #Initializing a variable
while yes: #While the variable is true
    Jake.forward(10 + i) #
    Jake.left(90)
    Jake.forward(10 + i)
    Jake.left(90)
    Jake.forward(10 + i)
    Jake.left(90)
    i = random.randint(1, 100)
    if i > 90:
        yes = False
Jake.end_fill() #Ends the fill of the turtle
my_screen = Screen()
print(my_screen.canvheight) #Screen will show up and then tell you the height
my_screen.exitonclick() #Screen now shows up and leaves only when clicked

##Turtle is loaded with python always

#Packages have to be installed
#If you want pretty table
#Pycharm settings -> Project Interpreter -> +Python Interpreter -> +Packages -> +pip -> +pip install prettytable

#OOP
numbers = [7,4,1,8,6,8,5,4,0,5,5,9,0,2,4,
 3,8,10,2,4,9,5,10,3,5,10,8,0,2,3,0,3,4,10]
def average(numbers):
    return sum(numbers) / len(numbers)

print(average(numbers))
#############################################################TURTLE WORK OOP#############################################################
from turtle import Turtle as T, Screen as S  # Example of turtle module that is not in the standard library
import heroes
import random

my_tuple = (1, 3, 8) #tuples are

my_screen = S()
my_screen.bgcolor("black")
Jake = T()  # Creating a new instance of a turtle class
# Jack = Turtle()
# Jank = Turtle()
Jake.shape("turtle")
# Jack.shape("turtle")
# Jank.shape("turtle")
Jake.shapesize(1, 1, 3)
# Jake.begin_fill()
Pen = False
colors = ["red", "green", "blue", "yellow",
          "grey", "purple", "CornflowerBlue",
          "DarkOrchid", "IndianRed", "DeepSkyBlue",
          "LightSeaGreen", "wheat", "SlateGray", "SeaGreen"]
Jake.pensize(15)
Jake.speed("fastest")
Jake.hideturtle()
def draw_shape(num_sides):
    angle = 360 / num_sides
    for _ in range(num_sides):
        Jake.forward(100)
        Jake.right(angle)

def random_walk(num_moves):
    angles = [0, 90, 180, 270]
    for _ in range(num_moves):
        Jake.color(random.choice(colors))
        Jake.forward(30)
        Jake.right(random.choice(angles))


# for i in range(3,10):
#     Jake.color(random.choice(colors))
#     draw_shape(i)

# Jake.end_fill()
random_walk(1000)
my_screen.exitonclick()

# Jake.shape("turtle") #Changes the shape of the turtle
# Jake.color('black', 'red') #Changes the color of the turtle
# Jake.begin_fill() #Begins the fill of the turtle
# i = 0 #Initializing a variable
# yes = True #Initializing a variable
# while yes: #While the variable is true
#     Jake.forward(10 + i) #
#     Jake.left(90)
#     Jake.forward(10 + i)
#     Jake.left(90)
#     Jake.forward(10 + i)
#     Jake.left(90)
#     i = random.randint(1, 100)
#     if i > 90:
#         yes = False
# Jake.end_fill() #Ends the fill of the turtle
# my_screen = Screen()
# print(my_screen.canvheight) #Screen will show up and then tell you the height
# my_screen.exitonclick()

# You can use from 'turtle import *' To eimport everything
#############################################################TURTLE WORK OOP END SECTION#############################################################
#############################################################TUPLE EXAMPLE############################################################################# #
#Tuple is a collection of items that cannot be changed
#Tuples are immutable
#Tuples are faster than lists
import turtle as t
import random

tim = t.Turtle()
t.colormode(255)

def random_color():
    r = random.randint(0, 255)  # Random red value
    g = random.randint(0, 255) # Random green value
    b = random.randint(0, 255) # Random blue value
    random_color = (r, g, b)
    return random_color


directions = [0, 90, 180, 270]
tim.pensize(15)
tim.speed("fastest")

for _ in range(200):
    tim.color(y)
    tim.forward(30)
    tim.setheading(random.choice(directions))

#############################################################TURTLE CIRCLE GRAPH######################################
import turtle as t

import random

tim = t.Turtle()
t.colormode(255)
screen = t.Screen()

def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    random_color = (r, g, b)
    return random_color


directions = [0, 90, 180, 270]
tim.pensize(1)
tim.speed("fastest")

# for _ in range(200):
#     tim.color(random_color())
#     tim.forward(30)
#     tim.setheading(random.choice(directions))
def draw_graph(gap_size):
    for _ in range(int(360 / gap_size)):
        tim.color(random_color())
        tim.circle(100)
        tim.setheading(tim.heading() + gap_size)
draw_graph(1)
# for _ in range(72):
#     tim.color(random_color())
#     tim.circle(100)
#     print(current_heading)
#     # tim.right(2)
#     tim.setheading(current_heading + 5)
#     current_heading = tim.heading()

# while current_heading <= 350:
#     tim.color(random_color())
#     tim.circle(200)
#     print(current_heading)
#     # tim.right(2)
#     tim.setheading(current_heading + 5)
#     current_heading = tim.heading()

screen.exitonclick()
#############################################################TURTLE CIRCLE GRAPH END SECTION######################################
###HIRST
import colorgram
from turtle import Turtle as T, Screen as S
import turtle as TT
import random

extracted = colorgram.extract('DOTSJUSTDOTS.jpg', 30)

color_list = [
 (246, 239, 239), (2, 9, 9), (122, 95, 95),
 (74, 33, 33), (237, 211, 211), (220, 81, 81),
 (223, 118, 118), (92, 1, 1), (178, 140, 140),
 (33, 90, 90), (150, 91, 91), (9, 153, 153),
 (204, 64, 64), (167, 129, 129), (2, 64, 64),
 (6, 219, 219), (220, 179, 179), (4, 80, 80),
 (80, 135, 135), (116, 151, 151), (78, 111, 111),
 (117, 187, 187), (7, 219, 219), (122, 12, 12),
 (243, 205, 205), (135, 221, 221), (229, 173, 173)
 ]
tim = T()
TT.colormode(255)
screen = S()
left_right = True
#tim.speed("slowest")
tim.speed("fastest")
tim.pensize(1)
tim.up()
tim.setheading(0)
dots = 100
#tim.hideturtle()
screen.bgcolor("black")
# def draw_line_of_dots():
#     for _ in range(10):
#         tim.color(random.choice(color_list))
#         tim.down()
#         tim.begin_fill()
#         tim.circle(10)
#         tim.end_fill()
#         tim.up()
#         tim.forward(45)
# def left_or_right():
#     global left_right
#     if left_right:
#         tim.setheading(tim.heading() + 90)
#         tim.forward(40)
#         tim.setheading(tim.heading() + 90)
#         left_right = not left_right
#     else:
#         tim.right(90)
#         tim.forward(40)
#         tim.right(90)
#         left_right = not left_right


for dot_count in range(1, dots + 1):
    tim.dot(20, random.choice(color_list))
    tim.forward(50)

    if dot_count % 10 == 0:
        tim.setheading(90)
        tim.forward(50)
        tim.setheading(180)
        tim.forward(500)
        tim.setheading(0)
    # draw_line_of_dots()
    # left_or_right()





screen.exitonclick()


# rgb_colors = []
#
# for color in extracted:
#     r = color.rgb.r
#     g = color.rgb.g
#     b = color.rgb.g
#     rgb_colors.append((r, g, b))

# print(rgb_colors)
#############################################################HIRST END######################################

#############################################################Listeners (Higher Order Functions)######################################
import turtle as T

class Etch_A_Sketch():

    def __init__(self):
        self.lawson = T.Turtle()
        self.screen = T.Screen()
        self.lawson.shape("arrow")
        self.lawson.turtlesize(.7, .7, .7)
        self.lawson.speed("fastest")


    def move_up(self):
        self.lawson.forward(10)

    def move_right(self):
        self.lawson.setheading(self.lawson.heading() - 10)

    def move_left(self):
        self.lawson.setheading(self.lawson.heading() + 10)

    def move_down(self):
        self.lawson.forward(10)

    def stop_start(self):
        pen_status = self.lawson.isdown()
        if pen_status:
            self.lawson.up()
        else:
            self.lawson.down()
    def erase_drawing(self):
        self.lawson.up()
        self.lawson.setheading(0)
        self.lawson.setposition(0, 0)
        self.lawson.clear()
        self.lawson.down()

    def start_drawing(self):
        self.screen.listen()
        self.screen.onkey(key="w", fun=self.move_up)
        self.screen.onkey(key="s", fun=self.move_down)
        self.screen.onkey(key="a", fun=self.move_left)
        self.screen.onkey(key="d", fun=self.move_right)
        self.screen.onkey(key="space", fun=self.stop_start)
        self.screen.onkey(key="c", fun=self.erase_drawing)

        self.screen.exitonclick()




#############################################################Listeners (Higher Order Functions) End######################################
#############################################################TurtleRaces######################################
import turtle as T
from random import randint
T.hideturtle()

is_race_on = False
screen = T.Screen()
screen.bgcolor("black")
screen.setup(600, 400)
user_bet = screen.textinput(
        title="Make your bet!",
        prompt="Which turtle do you think will win? Enter a color(Red,Green,Blue,Orange,Yellow,Pink): "
    ).lower()
colors = ["pink", "green", "blue", "orange", "yellow", "red"]
y_positions = [-70, -40, -10, 20, 50, 80]
all_turtles = []
finish_liner = T.Turtle(shape="arrow")
finish_liner.up()
finish_liner.color("white")
finish_liner.hideturtle()
finish_liner.setposition(230, -200)
finish_liner.down()
finish_liner.setheading(90)
finish_liner.forward(400)


for i in range(0, 6):
    new_turtle = T.Turtle(shape="turtle") #CLASS OOP USING A LOOP TO ADD MULTIPLE INSTANCES OF TURTLE
    new_turtle.up() #HIDES THE TURTLE DRAWING ON THE SCREEN FOR EACH INSTANCE OF TURTLE
    new_turtle.color(colors[i]) #SETS THE COLOR OF EACH TURTLE
    new_turtle.setposition(-230, y_positions[i]) #SETS THE POSITION OF EACH TURTLE
    all_turtles.append(new_turtle) #ADDING THE TURTLE TO THE LIST OF TURTLES TO BE USED

if user_bet:
    is_race_on = True


while is_race_on == True:
    for turtle in all_turtles:
        random_dist = randint(0, 5)
        turtle.forward(random_dist)
        if turtle.pencolor() == "red":
            turtle.forward(4)
        if turtle.xcor() > 230:
            is_race_on = False
            winning_color = turtle.pencolor()
            if winning_color == user_bet:
                print(f"YOU GOT IT RIGHT! {winning_color} Takes the race!")
            else:
                print(f"You were wrong ): {winning_color} took the race!")


print(user_bet)

screen.exitonclick()

#############################################################TurtleRaces END######################################
#############################################################SNAKE START UDEMY######################################

from turtle import Screen, Turtle

screen = Screen()
screen.setup(width=600,height=600)
screen.bgcolor("black")
screen.title("My Snake Game")
screen.tracer(0)
starting_positions = [(0, 0), (-20, 0), (-40, 0)]

segments = []

for position in starting_positions:
    new_segment = Turtle("square")
    new_segment.color("white")
    new_segment.up()
    new_segment.goto(position)
    segments.append(new_segment)

screen.update()
game_is_on = True
while game_is_on:
    for seg in segments:
        seg.forward(20)
screen.exitonclick()

#############################################################SNAKE END UDEMY######################################
#############################################################CLASS INHERITANCE START######################################
class Animal:
    def __init__(self):
        self.num_eyes = 2
    def breathe(self):
        print("Inhale, exhale")

class Fish(Animal): # Inherits from Animal
    def __init__(self):
        super().__init__() #The constructor is the same as the animal constructor, the class also inherits methods

    def breathe(self):
        super().breathe() #The breathe method is the same as the animal breathe method
        print("Blub, blub") #Unique twist on the animal class method breathe

    def swim(self):
        print("I'm swimming")

nemo = Fish()
nemo.swim()
nemo.breathe()
print(nemo.num_eyes)
#############################################################CLASS INHERITANCE END######################################
# paddle
# ball
#enempy paddle which inherits from paddle
#Create the screen
#Create and move a paddle
#Create another paddle
#create the ball and make it move
#detect collision with wall and bounce
# Detect collision with paddle
#Detect when paddle misses
#Keep score
from turtle import Screen, Turtle
from paddly import Paddle
screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("Pong")
screen.tracer(0)

r_paddle = Paddle(350, 0)
l_paddle = Paddle(-350, 0)


screen.listen()
screen.onkeypress(r_paddle.up, "Up")
screen.onkeypress(r_paddle.down, "Down")

game_on = True

while game_on:
    screen.update()

screen.exitonclick()

#Inheriting a class like the paddle
#Paddle.py
from turtle import Turtle


class Paddle:
    def __init__(self,posX, posY):
        self.paddle = Turtle()
        self.paddle.up()
        self.paddle.goto(posX, posY)
        self.paddle.shape("square")
        self.paddle.color("white")
        self.paddle.shapesize(stretch_wid=5, stretch_len=1)

    def up(self):
        (posX, posY) = self.paddle.pos()
        if (posY >= 220):
            return
        else:
            print(posX, posY)
            self.paddle.setpos(posX, (posY+20))

    def down(self):
        (posX, posY) = self.paddle.pos()
        if (posY <= -220):
            return
        else:
            print(posX, posY)
            self.paddle.setpos(posX, (posY - 20))
##Ball.py
from turtle import Turtle


class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.color("white")
        self.shape("circle")
        self.penup()

    def move(self):
        new_x = self.xcor() + 8
        new_y = self.ycor() + 8
        self.goto(new_x, new_y)
