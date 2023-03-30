/*
1. Basic Syntax
2. Comments
3. Preprocessor Directives
4. Header File
5. #include
6. printf
7. user input
8. variables
9. data types
10. enums and chars
11. format specifiers
12. command line arguments
13. operators
*/
//1. Basic Syntax
int main() // main is a function int is the common return type
{
    printf("Hi, my name is Morgan Gravelat");
    return 0;
}
void main() // void is a function that does not return anything
{
    printf("Hi, my name is Morgan Gravelat");
    return 0; // this is not needed and will give you a build warning
}
//2. Comments
// Comments can look like this
/*
    or like this
*/
/* You can put this above your code to help explain what it does
Author: Morgan Gravelat
Purpose: An example snippet of code that displays my name to the console
Date: March 21 2023
*/

3. Preprocessor Directives
// These are usually at the top of the file but can be anywhere
// Preprocessor directives are used to include libraries
// Preprocessor directives are not compiled
// #ifdef, #ifndef, #endif, #define, #undef, #include, #line, #error, #pragma
// #include is used to include libraries
// #ifndef is used to check if a library has already been included
// #define is used to define a constant
// #undef is used to undefine a constant
// #pragma is used to include a library
// #error is used to display an error message
// #line is used to change the line number
// #ifdef is used to check if a constant has been defined
// #endif is used to end an #ifdef or #ifndef block
#include <stdio.h> // this is a preprocessor directive
#include <stdlib.h> // this is a preprocessor directive
#include <string.h> // this is a preprocessor directive
#include <math.h> // this is a preprocessor directive
#include <ctype.h> // this is a preprocessor directive
#include <conio.h> // this is a preprocessor directive
#include <time.h> // this is a preprocessor directive
#include <windows.h> // this is a preprocessor directive

4. Header File

// A header file is a file that contains function prototypes
// Header files define the functions that are available to the user
// stdio.h is a standard header file it contains function prototypes for input and output
// to use printf you must include stdio.h it contains the function prototype for printf
// stdio is short for standard input output
// header files are case sensitive so always use lowercase letters
// you can use angle brackets or double quotes to include a header file
// #include <stdio.h> is the same as #include "stdio.h"
// use #ifndef and #define to check if a header file has already been included

5. #include
// As stated above #include is used to include libraries
// There are 2 types of libraries
// 1. Standard Libraries
// 2. User Defined Libraries
// Standard Libraries are included with the compiler
// User Defined Libraries are created by the user
// Standard Libraries
#include <stdio.h> // this is a preprocessor directive
// This library is used for input and output
// It contains functions such as printf, scanf, etc.
// User Defined Libraries
#include "myLibrary.h" // this is a preprocessor directive
// This library is created by the user
// It contains functions that the user has created
// It is included in the same directory as the source code

5. Header File

// A header file is a file that contains function prototypes
// Header files define the functions that are available to the user
// stdio.h is a standard header file it contains function prototypes for input and output
// to use printf you must include stdio.h it contains the function prototype for printf
// stdio is short for standard input output
// header files are case sensitive so always use lowercase letters
// you can use angle brackets or double quotes to include a header file
// #include <stdio.h> is the same as #include "stdio.h"
// use #ifndef and #define to check if a header file has already been included
// Header files don't contain any code they only contain function prototypes
// Header files are used to prevent duplicate function prototypes

6. printf
// printf is used to display output to the console
// printf is a function that is defined in stdio.h
// printf is short for print formatted
// printf is a standard library function
// it outputs a formatted string to the console
// printf is a function that takes 2 parameters
// 1. A string
// 2. A list of variables

7. user input
// scanf is used to get input from the user
// scanf is a function that is defined in stdio.h
// scanf is short for scan formatted
// scanf is a standard library function
// scanf is a function that takes 2 parameters
// 1. A string
// 2. A list of variables
// There are 3 rules for scanf
// 1. The string must contain a % for each variable
// 2. The string must contain a data type for each variable
// 3. The variables must be in the same order as the data types in the string
// scanf returns the number of variables that were read
// if you use scanf to read a value for one of the basic variable types preceded by an & sign
// if you use scanf to read a string into a character array you must not use the & sign
// scanf uses white space to separate the input
// scanf is the inverse of printf which converts integers floating point numbers and characters and c strings to
// --to text that is to be displayed on screen
// stdin is short for standard input
// stdin is the default input stream

/*
#include <stdio.h>
int main() {
    char str[100];
    int i;

    printf("Enter a value :");
    scanf("%s %d", str, &i); // the & sign is used to get the address of the variable
    //the %s is used to read a string and the %d is used to read an integer
    // you can use %lf to read a double and %c to read a character and %f to read a float and %x to read a hexadecimal and %Lf to read a long double
    // the string will be read into the str variable and the integer will be read into the i variable

    printf("\nYou entered: %s %d ", str, i);

    return 0;
}
*/

8. variables

// variables are used to store data in memory
// variables are named memory locations
// the rules for naming variables are that they must start with a letter or an underscore and can be followed by letters, numbers, or underscores
/*
These are valid variable names
Jason
myFlag
i
J5x7
my_data
_anotherVariable
These are invalid variable names
temp$value - this is invalid because it contains a $
my flag - this is invalid because it contains a space
3Jason - this is invalid because it starts with a number
int - this is invalid because it is a keyword

*/

9. data types
/*
There are multiple types of data
 1. int - integer
 2. float - floating point number
 3. double - double precision floating point number
 4. char - character
 5. string - string of characters
 6. _Bool - boolean
 7. void - void
 8. long - long integer
 9. short - short integer
 10. unsigned - unsigned integer
 11. signed - signed integer
*/
//int is a 4 byte integer
//it goes type-specifier variable-name;
//int is a signed integer
//int x; // this is a variable declaration
//x = 10; // this is a variable assignment
//int x,y,z; // this is a variable declaration with multiple variables
//x = 10; y = 10; z = 10; // this is a variable assignment with multiple variables
// You can assign a hexadecimal value to an integer by using the 0x prefix
// You can assign an octal value to an integer by using the 0 prefix
// You can assign a binary value to an integer by using the 0b prefix
// You can assign a character to an integer by using the single quotes
//Float is a 4 byte floating point number
//float is a single precision floating point number
//float x; // this is a variable declaration
//x = 10.5; // this is a variable assignment
//float x,y,z; // this is a variable declaration with multiple variables
//x = 10.5; y = 10.5; z = 10.5; // this is a variable assignment with multiple variables
//Double is a 8 byte floating point number
//double is a double precision floating point number
//double x; // this is a variable declaration
//x = 10.5; // this is a variable assignment
//float jason = 23.3333; // this is a variable declaration and assignment
//double x=10.5,y=10.5,z=10.5; // this is a variable declaration and assignment with multiple variables
//_Bool is a 1 byte boolean
//_Bool is a boolean
//_Bool x = 1; // this is a variable declaration and assignment
// to use the keyword bool you must include stdbool.h
// with stdbool.h you can use bool instead of _Bool and true instead of 1 and false instead of 0
// short int is a 2 byte integer and is a signed integer
//c offers words like short and long to specify the size of an integer
// unsigned int is a 4 byte integer and is an unsigned integer
// unsigned are only used for positive numbers
// a long double is a 16 byte floating point number and is followed by the letter L
// long double x = 1.234e+7L; // this is a variable declaration and assignment

10. enums and chars
// enums are used to define a set of named constants
// they are a data type that allow a programmer to define a variable and specify the valid values that could be store in that variable
// it can create a variable called myColor and specify that the only valid values for that variable are red, green, and blue
// First you must define the enum and give it a name
// initiate by the keyword enum then the name of the data type then list the identifiers
// the identifiers are the names of the constants
// enum primaryColor {red, yellow, blue}; // this is an enum declaration
// to declare a variable to be of type enum primaryColor you would do the following
// use the keyword enum followed by the enumerated type name followed by the variable name
// enum primaryColor myColor, gregsColor; // this is an enum declaration with multiple variables
// now myColor and gregsColor are of type enum primaryColor and can only be assigned the values red, yellow, or blue
// enum month {january, february, march, april, may, june, july, august, september, october, november, december};
// the compiler treats enumeration identifiers as integers constants first name in list is 0, second is 1, third is 2, etc
// enum month thisMonth;
// thisMonth = january; // thisMonth is assigned the value 0
// thisMonth = february; // thisMonth is assigned the value 1
// if you want a specific integer value for an identifier you can do the following
// enum month {january = 1, february, march, april, may, june, july, august, september, october, november, december};
// now january is 1, february is 2, march is 3, etc
// enum direction {up, down, left=10, right};
// now up is 0, down is 1, left is 10, right is 11
// char is a 1 byte character and will hold a single character
// char uses single quotes
// char x; // this is a variable declaration
// x = 'a'; // this is a variable assignment for a character
// char broiled = 'b'; // this is a variable declaration and assignment
// broiled = 'T'; // this is a valid assignment
// broiled = 'Tom'; // this is an invalid assignment
// broiled = T; // this is an invalid assignment
// broiled = "T" // this is an invalid assignment
// if you omit the quotes it will think you are trying to assign a variable
// double quotes are used for strings
// you can also use numerical values to assign a character
// char x = 65; // this is ok for ASCII character 65 is A but this is poor programming practice
// escape characters are used to represent non-printable characters
// \n is a newline
// \t is a tab
// \b is a backspace
// \r is a carriage return
// \v is a vertical tab
// \f is a form feed
// \a is an alert
// \? is a question mark
/*
#include <stdio.h>

int main()
{
    char myChar = '\n';

    printf("%c", myChar);

    return 0;

}
// this will print a new line the myChar variable is assigned the value of a new line
result = '
 '



*/

11. format specifiers

// format specifiers are used to format the output of printf
// %i is used for integers
// %f is used for floating point numbers
// %d is used for decimal numbers
// %g is used for double precision floating point numbers
// %c is used for characters
// %s is used for strings
// %e is used for scientific notation
// %o is used for octal numbers
// %x is used for hexadecimal numbers
// %u is used for unsigned integers
// %p is used for pointers
/*
int main()
{
    int integerVar = 100;
    float floatingVar = 331.79;
    double doubleVar = 8.44e+11;
    char charVar = 'W';

    _Bool boolVar = 0;

    printf("integerVar = %i\n", integerVar);
    printf("floatingVar = %f\n", floatingVar);
    printf("doubleVar = %e\n", doubleVar);
    printf("doubleVar = %g\n", doubleVar);
    printf("charVar = %c\n", charVar);
    printf("boolVar = %i\n", boolVar);
    printf("%.1f", 1.2345); // this will print 1.2 since the .1 specifies the number of decimal places to print
}
*/

12. command line arguments

// command line arguments are used to pass information to a program when it is executed
/*
#include <stdio.h>
#include <stdlib.h>

int main(int argc, char *argv[])
{
    int numberOfArguments = argc;
    char *argument1 = argv[0];
    char *argument2 = argv[1];

    printf("Number of arguments = %d\n", numberOfArguments);
    printf("Argument 1 is the program name: %s\n", argument1);
    printf("Argument 2 is the first command line argument: %s", argument2);

    return 0;
}

*/

13. operators

// operators are used to perform operations on variables and values
// there are 6 types of operators
// arithmetic operators (+, -, *, /, %)
// assignment operators (=, +=, -=, *=, /=, %=, <<=, >>=, &=, ^=, |=)a
// comparison operators (==, !=, >, <, >=, <=)
// logical operators (&&, ||, !)
// bitwise operators (&, |, ^, ~, <<, >>)
// ternary operators (?:)
// unary operators (+, -, ++, --, !, &, *, sizeof, _Alignof, _Generic, _Noreturn, _Static_assert, _Thread_local)
// sizeof is used to determine the size of a variable or data type
// relational operators are used to compare two values
// + is addition
// - is subtraction
// * is multiplication
// / is division
// % is modulus (remainder)
// = is assignment
// += is addition assignment
// -= is subtraction assignment
// *= is multiplication assignment
// /= is division assignment
// %= is modulus assignment
// <<= is left shift assignment (shifts the bits of the first operand to the left by the number of bits specified by the second operand)
// >>= is right shift assignment (shifts the bits of the first operand to the right by the number of bits specified by the second operand)
// &= is bitwise AND assignment (performs a bitwise AND operation between the first and second operands and assigns the result to the first operand)
// bitwise compares each bit of the first operand to the corresponding bit of the second operand and returns a value where the corresponding bit is set if both bits are set
// 0001 & 0011 = 0001
// == is equal to
// != is not equal to
// > is greater than
// < is less than
// >= is greater than or equal to
// <= is less than or equal to
// && is logical AND
// || is logical OR
// ! is logical NOT
// & is bitwise AND
// | is bitwise OR
// ^ is bitwise XOR
// ~ is bitwise NOT
// << is left shift (shifts the bits of the first operand to the left by the number of bits specified by the second operand)
// >> is right shift (shifts the bits of the first operand to the right by the number of bits specified by the second operand)
// ?: is ternary operator (condition ? expression1 : expression2) if condition is true then expression1 is evaluated and returned otherwise expression2 is evaluated and returned
// + is unary plus
/*
#include <stdio.h>
int main()
{
    int a = 21;
    int c = 18;
    int remainder = 0;
    c = a;
    printf("Value of c = %d \n", --c);

    return 0;
}
#include <stdio.h>
#include <stdbool.h>

int main()
{
    _Bool a = true;
    _Bool c = false;
    _Bool result;
    result = !a;

    printf("Value of c or a = %d \n", result);

    return 0;
}



*/
