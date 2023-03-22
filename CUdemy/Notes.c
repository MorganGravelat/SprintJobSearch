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
