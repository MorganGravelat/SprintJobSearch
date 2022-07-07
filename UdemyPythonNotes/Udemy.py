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
new_num_char = str(num_char)

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
print (int(8/3)) # 2
print (round(8/3)) # 3 #2.6666666 UP
print (round(8/3, 4)) # the 4 chooses the amount of decimal places you get NONE is 0
