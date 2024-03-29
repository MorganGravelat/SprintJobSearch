/*
#include <stdio.h>
#include <stdlib.h>

int main()
{
    double width, height, perimeter, area;
    scanf("Give the width %e\n now give the height %e", &width, &height);
    perimeter = 2.0 * (height + width);
    area = height * width;
    printf("The perimeter is %e and the area is %e", perimeter, area);
    return 0;
}

#include <stdio.h>
#include <stdlib.h>

int main()
{
    double width, height, perimeter, area;
    printf("Give the width\n");
    scanf("%lf", &width); // this uses scanf to get the width and height
    printf("Give the height\n");
    scanf("%lf", &height);
    perimeter = 2.0 * (height + width);
    printf("The width is %.1f and the height is %.1f\n", width, height);
    area = height * width;
    printf("The perimeter is %.1f and the area is %.1f", perimeter, area);
    return 0;
}


#include <stdio.h>
#include <stdlib.h>

int main(int argc, char *argv[])
{
    double width=atoi(argv[1]), height=atoi(argv[2]), perimeter, area; //converting char to double with atoi

    //Performing perimeter calculation and then displaying the information
    perimeter = 2.0 * (height + width);
    printf("The width is %.1f and the height is %.1f\n", width, height);
    area = height * width;
    printf("The perimeter is %.1f and the area is %.1f", perimeter, area);
    return 0;
}


*/
/* ENUM Project
#include <stdio.h>


int main()
{
    enum Company {GOOGLE, FACEBOOK, XEROX, YAHOO, EBAY=11, MICROSOFT};
    enum Company comp1 = XEROX, comp2 = GOOGLE, comp3 = EBAY;
    printf("The value of Xerox: %i\n", comp1); // the value of Xerox is 2
    printf("The value of Google: %i\n", comp2); // the value of Google is 0
    printf("The value of Ebay: %i", comp3); // the value of Ebay is 11
    return 0;

}


ALL OPERATORS

#include <stdio.h>

int main() {
    int a = 10, b = 20;
    int result;

    // Arithmetic operators
    result = a + b;
    printf("%d + %d = %d\n", a, b, result);

    result = a - b;
    printf("%d - %d = %d\n", a, b, result);

    result = a * b;
    printf("%d * %d = %d\n", a, b, result);

    result = b / a;
    printf("%d / %d = %d\n", b, a, result);

    result = b % a;
    printf("%d %% %d = %d\n", b, a, result);

    // Relational operators
    if (a == b) {
        printf("%d == %d is true\n", a, b);
    } else {
        printf("%d == %d is false\n", a, b);
    }

    if (a != b) {
        printf("%d != %d is true\n", a, b);
    } else {
        printf("%d != %d is false\n", a, b);
    }

    if (a < b) {
        printf("%d < %d is true\n", a, b);
    } else {
        printf("%d < %d is false\n", a, b);
    }

    if (a > b) {
        printf("%d > %d is true\n", a, b);
    } else {
        printf("%d > %d is false\n", a, b);
    }

    if (a <= b) {
        printf("%d <= %d is true\n", a, b);
    } else {
        printf("%d <= %d is false\n", a, b);
    }

    if (a >= b) {
        printf("%d >= %d is true\n", a, b);
    } else {
        printf("%d >= %d is false\n", a, b);
    }

    // Logical operators
    int c = 5, d = 6, e = 0;

    if (c && d) {
        printf("%d && %d is true\n", c, d);
    } else {
        printf("%d && %d is false\n", c, d);
    }

    if (c && e) {
        printf("%d && %d is true\n", c, e);
    } else {
        printf("%d && %d is false\n", c, e);
    }

    if (c || d) {
        printf("%d || %d is true\n", c, d);
    } else {
        printf("%d || %d is false\n", c, d);
    }

    if (c || e) {
        printf("%d || %d is true\n", c, e);
    } else {
        printf("%d || %d is false\n", c, e);
    }

    if (!e) {
        printf("!%d is true\n", e);
    } else {
        printf("!%d is false\n", e);
    }

    return 0;
}
*/
/*
#include <stdio.h>

int main()
{
    int minutes;
    int minInDay = 60*24;
    int minInYear = minInDay * 365;
    double days;
    double years;

    printf("Enter a value in minutes :");
    scanf("%d", &minutes); // this uses scanf to get the minutes remember the &

    days = (double)minutes / minInDay; // this is the conversion to double
    years = (double)minutes / minInYear; // make sure to put the (double) in front of the variable

    printf("minutes = %d\n days = %lf\n years = %lf", minutes, days, years);
    return 0;
}


function zigzagTraverse(array) {
  const height = array.length - 1;
  const width = array[0].length - 1;
  const result = [];
  let row = 0;
  let col = 0;
  let goingDown = true;
  while (!isOutOfBounds(row, col, height, width)) {
    result.push(array[row][col]);
    if (goingDown) {
      if (col === 0 || row === height) {
        goingDown = false;
        if (row === height) {
          col++;
        } else {
          row++;
        }
      } else {
        row++;
        col--;
      }
    } else {
      if (row === 0 || col === width) {
        goingDown = true;
        if (col === width) {
          row++;
        } else {
          col++;
        }
      } else {
        row--;
        col++;
      }
    }
  }
  return result;
}



#include <stdio.h>
#include <stdlib.h>

int main()
{

    printf("Variables of type char occupy %u\n", sizeof(char)); //the size will be 1 byte
    printf("Variables of type short occupy %u\n", sizeof(short)); // the size will be 2 bytes
    printf("Variables of type int occupy %u\n", sizeof(int)); // the size will be 4 bytes
    printf("Variables of type long occupy %u\n", sizeof(long)); // the size will be 4 bytes or 8 bytes in 64 bit systems
    printf("Variables of type long long occupy %u\n", sizeof(long long)); // the size will be 8 bytes
    printf("Variables of type float occupy %u\n", sizeof(float)); // the size will be 4 bytes
    printf("Variables of type double occupy %u\n", sizeof(double)); // the size will be 8 bytes
    printf("Variables of type long double occupy %u\n", sizeof(long double)); // the size will be 16 bytes

    return 0;
}

//if statement I forgot to put in

int main()
{
    int number_to_test, remainder;

    printf ("Enter your number to be tested: ");
    scanf ("%i", &number_to_test);

    remainder = number_to_test % 2;

    if (remainder == 0) {
        printf ("The number is even.\n");
    }
    else {
        printf( "The number is odd.\n");
    }

    return 0;
}
//Nested if statements

if (gameIsOver == 0) {
    if (player1Score > player2Score) {
        printf ("Player 1 wins.\n");
    }
    else if (player2Score > player1Score) {
        printf ("Player 2 wins.\n");
    }
    else {
        printf ("The game is a tie.\n");
    }
else {
    printf ("The game is over.\n");
}

//ternerary operator in C
//variable = (condition) ? expressionTrue : expressionFalse;
// if condition is true then expressionTrue is executed otherwise expressionFalse is executed
y = 8;
x = (y > 7) ? 1 : 2; // x is 1 because y is greater than 7

//switch statement in C
switch (expression) {
    case constant1:
        statement(s);
        break; // this is optional but it is good practice to put it in there to avoid fall through
    case constant2:
        statement(s);
        break; // the only reason you would not put a break in is if you wanted to fall through to the next case
    .
    .
    .
    default:












        statement(s);
}


// C program that calculates your weekly pay

#include <stdio.h>
#include <stdlib.h>

int main()
{
    double hoursWorked;
    double hourlyRate;
    double weeklyPay;

    printf("Enter the number of hours worked this week: ");
    scanf("%lf", &hoursWorked);

    printf("Enter your hourly rate: ");
    scanf("%lf", &hourlyRate);

    if (hoursWorked <= 40) {
        weeklyPay = hoursWorked * hourlyRate;
    }
    else {
        weeklyPay = 40 * hourlyRate;
        weeklyPay += (hoursWorked - 40) * (hourlyRate * 1.5);
    }

    printf("Your weekly pay is %.2lf\n", weeklyPay);

    return 0;
}

#include <stdio.h>
#include <stdlib.h>
int main() {
    double hoursWorked;
    double hourlyRate = 12.00;
    double weeklyPay;

    printf("Enter the number of hours worked this week: ");
    scanf("%lf", &hoursWorked);

    if (hoursWorked <= 40) {
        weeklyPay = hoursWorked * hourlyRate;
        printf("hours worked if is %.2lf\n", weeklyPay);
    }
    else {
        weeklyPay = 40 * hourlyRate;
        weeklyPay += (hoursWorked - 40) * (hourlyRate * 1.5);
        printf("hours worked else is %.2lf\n", weeklyPay);
    }

    if (weeklyPay <= 300.00) {
        weeklyPay = 300.00 * 0.85;
        printf("if pay is %.2lf\n", weeklyPay);
    } else if (weeklyPay > 300.00 && weeklyPay <= 450.00) {
        weeklyPay = 300.00 * 0.85;
        printf("Else if pay is %.2lf\n", weeklyPay);
        weeklyPay += (weeklyPay - 300.00) * 0.80;
        printf("Else if pay is %.2lf\n", weeklyPay);
    } else {
        weeklyPay = (300.00 * 0.85) + (150.00 * 0.80);
        printf("Else pay is %.2lf\n", weeklyPay);
        weeklyPay = weeklyPay + (weeklyPay - 450.00) * 0.75;
        printf("Second else pay is %.2lf\n", weeklyPay);
    }

    printf("Your weekly pay is %.2lf\n", weeklyPay);
}
*/
/*
Mini project follow along for program that goes through dynamically adding grades to an averager with a while loop
#include <stdio.h>
#include <stdlib.h>

int main()
{
    //int num = 3;

    //loop 1: 3*3 = 9
    //loop 2: 3*3*3 = 27
    //loop 3: 3*3*3*3 = 81
    //loop 4: 3*3*3*3*3 = 243
    //get the number, it is 243

    //use while statement
    /*while (num<=100) {
        //calculate the power of 3
        num = num * 3;
    }
    printf("the first power of 3 greater than 100 is %d", num);*/

    // give you the number and exp, please use while statement to calculate
    //the power
    // 5 ^ 2 = 5 * 5 = 25
    /*
    //Exponential Number While loop
    int number = 5;
    int result = number;
    int exp = 5;
    int count = 1;
    while (count < exp) {
        printf("Count:%d / Exp:%d / Number:%d / Result:%d\n", count, exp, number, result);
        result = result * number;
        printf("%d\n", result);
        count += 1;
    }
    printf("The answer is: %d", result);
    */
    //A class of 10 students, their grade for the quiz are avaialable
    //Write a program to calculate the class average for the quiz
    //Use while structure

        //init
        /*
        int total = 0;
        int counter = 1;
        int students = 10;
        int grade = 0;
        int average = 0;
        printf("%s", "how many students are there?: ");
        scanf("%d", &students);
        //get student grades and calculate the average
        //while counter is less or equal to 10
        while (counter <= students) {
            //input student's grade
            printf("%s", "enter student's grade: ");
            scanf("%d", &grade);
            while (grade < 0 || grade > 100) {
               printf("%s", "Grades must be above 0 and below 100: ");
               scanf("%d", &grade);
            }
            //add the grade to the total
            total += grade;
            //increase the counter by 1
            counter += 1;
        }

        average = total / students;
        printf("The average is %d", average);
        //input student's grade
        //add the grade to the total
        */
        /*
        //init variables
        double total = 0;
        double average = 0;
        double grade = 0;
        int counter = 0;
        //get student's grade, sum the grades. when user enter -1, means end of program

        //get first user input
        printf("%s", "please enter the grade: ");
        scanf("%f", &grade);

        while (grade != -1) {
            total = (double)total + grade;
            counter += 1;
            printf("%s", "please enter the grade: ");
            scanf("%d", &grade);
        }

        //printf("total is %d, counter is %d", total, counter);
        //calculate the average and print out the result
        //converting the data type: explicitly and implicitly
        average = total /counter;
        printf("the average of %d is %.2f", counter, average);*/

        //use while structure to print out a pattern
        //example of 4*4
        //* * * *
        //* * * *
        //* * * *
        //* * * *
/*
        int row = 0;
        int column = 0;
        int size = 0;

        printf("%s", "Please enter the size of the table: ");
        scanf("%d", &size)
}




    //init
    int row = 0; //counter for number of rows
    int column = 0; //counter for number of columns
    int size = 0; //user input size of n*n table
    //get user input
    printf("%s", "please enter the size of the table: ");
    scanf("%d", &size);
    //print the table
    while (row < size) { //print for each row
        if (row == 0 || row == size-1) {
            while (column < size) { //print each stars in that row
                printf("%s", "* ");
                column += 1;
        }
        else {
            //for rows in between
            // check if it is the first or last column
            if (column == 0 || column == size - 1) {
                printf("%s", "* ");
            }
            else {
                printf("%s", "  ")
            }
            column += 1;
        }
        }
        row += 1;
        column = 0;
        puts(" ");
    }

*/
/*
Working grade averager

    /*
    //init
    int row = 0; //counter for number of rows
    int column = 0; //counter for number of columns
    int size = 0; //user input size of n*n table
    //get user input
    printf("%s", "please enter the size of the table: ");
    scanf("%d", &size);
    //print the table
    while (row < size) { //print for each row
        if (row == 0 || row == size-1) {
            while (column < size) { //print each stars in that row
                printf("%s", "* ");
                column += 1;
        }
        else {
            //for rows in between
            // check if it is the first or last column
            if (column == 0 || column == size - 1) {
                printf("%s", "* ");
            }
            else {
                printf("%s", "  ")
            }
            column += 1;
        }
        }
        row += 1;
        column = 0;
        puts(" ");
    }
    */
    //A class of 10 students, their grade for the quiz are avaialable
    //Write a program to calculate the class average for the quiz
    //Use while structure

        //init
        /*
        int total = 0;
        int counter = 1;
        int students = 10;
        int grade = 0;
        int average = 0;
        printf("%s", "how many students are there?: ");
        scanf("%d", &students);
        //get student grades and calculate the average
        //while counter is less or equal to 10
        while (counter <= students) {
            //input student's grade
            printf("%s", "enter student's grade: ");
            scanf("%d", &grade);
            while (grade < 0 || grade > 100) {
               printf("%s", "Grades must be above 0 and below 100: ");
               scanf("%d", &grade);
            }
            //add the grade to the total
            total += grade;
            //increase the counter by 1
            counter += 1;
        }

        average = total / students;
        printf("The average is %d", average);
        //input student's grade
        //add the grade to the total
        */
        /*
        //init variables
        double total = 0;
        double average = 0;
        int grade = 0; //For the input of -1 the double will break the system. Use int instead.
        int counter = 0;
        //get student's grade, sum the grades. when user enter -1, means end of program

        //get first user input
        printf("%s", "please enter the grade: ");
        scanf("%d", &grade);

        while (grade != -1.0) {
            total = total + grade;
            counter += 1;
            printf("%s", "please enter the grade: ");
            scanf("%d", &grade);
        }

        //printf("total is %d, counter is %d", total, counter);
        //calculate the average and print out the result
        //converting the data type: explicitly and implicitly
        average = (double)total /counter;
        printf("the average of %d is %.2f", counter, average);
        */
       /*
#include <stdio.h>
#include <stdlib.h>
#include <ctype.h>

int main()
{

    char grade = 0;
    printf("%s", "Please enter your grade: ");
    for (int i = 0; i < 4; i++) {
        grade = getchar() //getchar will get the first character in stdio

        //printf("char is %c", grade);
        if (grade != " ") {
            putchar(grade);
        }
    }

/*
    //scanf("%c", &grade);
    grade = getchar(); //you can scan a char like this but will only get one character
    grade = toupper(grade); // this will make lower case inputs appear as uppercase for the switch.
    switch (grade) {
case 'A':
    puts("you get A");
    break;
case 'B':
    puts("you get B");
    break;
case 'C':
    puts("You get C");
    break;
case 'D':
    puts("you get D");
    break;
default:
    puts("Sorry you get F");

    }
*/
/*
    return 0;

}


//DO WHILE LOOP BELOW
int main(void)
{
    int i = 1;
    while (i <= 6) {
        printf("%s", "Using while loop");
        printf("%d ", i);
            i++;
    }
    i--;
    puts("");
    //do while statement below
    do {
        printf("%s", "Using do while loop");
        printf("%d ", i);
        i--;
    } while(i > 0); //A do while is guaranteed to run once where a while will only run during the condition being true

    //return 0; only needed if the main does not have (void) inside the parenthesis

}
*/
/*
break and continue example
int main(void)
{
    for (int i = 0; i < 10; i++) {
        if (i == 6) {
            continue; //Will print 012345789 //or break prints 012345 if you want to completely cancedl out the loop after 6
        }
        printf("%d", i);
    }
    puts("\njump out of the loop");
    //return 0; only needed if the main does not have (void) inside the parenthesis

}
'
#include <stdio.h>
#include <string.h>

int main(void) {
    int a = 0;
    int b = 3;

    //truth table
    // a    b  a && b
    // 0    0  0
    // 0    1  0
    // 1    0  0
    // 1    1  1
}


//ask user to input the size, then please print out below pattern.
// if user enter 4, the pattern should be
//*
//**
//***
//****

#include <stdio.h>
#include <string.h>

int main(void) {
    char a = "*"
    char[] = "";
    int size = 0;

    puts("Please enter the size of the pattern: ");
    scanf("%d", &size);

    for (int i = 0; i < size; i++) {
        strcat(a, "*");
        puts(a);
    }

}

#include <stdio.h>
//#include <stdlib.h>
//#include <ctype.h>
//#include <string.h> //my version used this but below is the no library needed version

int main(void) {
    /*
    char pattern[] = "";
    int size = 0;

    puts("Please enter the size of the pattern: ");
    scanf("%d", &size);

    for (int i = 0; i < size; i++) {
        strcat(pattern, "*");
        puts(pattern);
    }
    */
/*
    int row = 0;
    printf("%s", "please enter the row: ");
    scanf("%d", &row);

    for (int i = 1; i <= row; i++){
        for (int j = 1; j <= i; j++) {
            printf("%s", "*");
        }
        puts(" ");
    }
    puts (" ");
    for (int i = 0; i < row; i++) {
        for (int j = 0; j < row; j++) {
            if (j < i) {
                printf("%s", " ");
            }
            else {
                printf("%s", "*");
            }
        }
        puts(" ");
    }
}

*/

/*
#include <stdio.h>
#include <stdlib.h>
#include <math.h>

int main(void) {
    int sum; //a) Sum the odd integers between 1 and 99 using a for statement. Use the integer variables sum and count.
    int x = 1;
    for (int i = 1; i < 100; i++) {
        if (i % 2 != 0) {
            sum += i;
            printf("Sum: %d and I: %d\n", sum,i);
        }
    }
    //b) Print the value 333.546372 in a field width of 15 characters with precisions of 1, 2, 3, 4 and 5. Left-align the output. What are the five values that print?
    printf("\n%-15.1f \n%-15.2f \n%-15.3f \n%-15.4f \n%-15.5f",333.546372,333.546372,333.546372,333.546372,333.546372);
    //c) Calculate the value of 2.5 raised to the power of 3 using the pow function. Print the result with a precision of 2 in a field width of 10 positions. What is the value that prints?
    printf("\n2.5 to the power of 3: %10.2f", pow(2.5,3));
    puts("");
    //d) Print the integers from 1 to 20 using a while loop and the counter variable x. Print only five integers per line. [Hint: Use the calculation x % 5. When this is 0, print a newline character, otherwise print a tab character.]
    while (x <= 20) {
        if (x % 5 == 0) {
            printf("%d\n", x);
        }
        else {
            printf("%d\t", x);
        }
        x++;

    }
    puts("");
    //e) Repeat Exercise 4.3(d) using a for statement
    for (int i = 1; i <= 20; i++) {
        if (i % 5 == 0) {
            printf("%d\n", i);
        }
        else {
            printf("%d\t", i);
        }
    }
}



//LAB 3B
#include <stdio.h>
#include <stdlib.h>
#include <math.h>

int main(void) {
    int sum = 0;

    for (int i = 0; i <= 1000; i++) {
        if (i % 2 == 0 && i % 3 != 0) {
            sum += i;
            printf("\nCurrent Sum: %d AND i: %d", sum, i);
        }
    }
    printf("\nEnd Sum: %d", sum);
}
    /*
    char pattern[] = "";
    int size = 0;

    puts("Please enter the size of the pattern: ");
    scanf("%d", &size);

    for (int i = 0; i < size; i++) {
        strcat(pattern, "*");
        puts(pattern);
    }
    */

    int row = 0;
    printf("%s", "please enter the row: ");
    scanf("%d", &row);
    /*
    for (int i = 1; i <= row; i++){
        for (int j = 1; j <= i; j++) {
            printf("%s", "*");
        }
        puts(" ");
    }
    for (int i = row; i >= 1; i--){
        for (int j = 1; j <= i; j++) {
            printf("%s", "*");
        }
        puts(" ");
    }
    */

    /*
    for (int i = 0; i < row; i++){
        for (int j = row; j > i; j--) {
            printf("%s", "*");
        }
        puts(" ");
    }
    *///below prints out 4
    //****
    // ***
    //  **
    //   *
    puts(" ");
    for (int i = 0; i < row; i++){
        for (int j = 0; j < i; j++) {
            printf("%s", " ");
        }
        for (int k = i; k < row; k++) {
            printf("%s", "*");
        }
        puts(" ");
    }
    puts (" ");
    for (int i = 0; i < row; i++) {
        for (int j = 0; j < row; j++) {
            if (j < i) {
                printf("%s", " ");
            }
            else {
                printf("%s", "*");
            }
        }
        puts(" ");
    }

    //divide and conquer
    //standard library function, include the proper headers to use those functions. Like printf, scanf
    //quick and easy to use
    //standard library functions are portable, they work on all systems


    /*
COP3223 Summer 2023 Assignment 1_1
Copyright 2023 Gravelat Morgan
*/

#include <stdio.h>

int main(void) {
    int hours;        // Stores the hours worked each time you input the amount for an employee
    float hourly;     // Stores the hourly pay made by the employee
    float salary;     // Temporary variable to store the overall amount made by the employee

    // This loop will run forever until it is broken out of by the if statement below
    while (1) {
        // Prompt for the user to input the number of hours the employee worked
        printf("%s", "Enter # of hours worked (-1 to end): ");
        scanf("%d", &hours);

        // If the user's input for hours is -1, then the loop is terminated
        if (hours == -1) {
            break;
        }

        // Prompt for the user to input the hourly pay of the employee
        printf("%s", "Enter hourly rate of the worker ($00.00): ");
        scanf("%f", &hourly);

        // Calculate the salary based on whether the hours worked exceed 40 hours or not
        if (hours > 40) {
            // For hours over 40, calculate the salary with time and a half pay
            salary = (hourly * 40) + ((hourly * 1.5) * (hours - 40));
        }
        else {
            // For hours less than or equal to 40, calculate the salary without overtime
            salary = hourly * hours;
        }

        // Print the calculated salary of the employee to the console
        printf("Salary is $%.2f\n\n\n", salary);
    }

    return 0;
}



/*
COP3223 Summer 2023 Assignment 1_3
Copyright 2023 Gravelat Morgan
*/

#include <stdio.h>

int main(void) {
    int rows, i, j, space, asterisks;

    // Prompt the user to input an odd number between 1 and 19 for the rows of the diamond
    printf("Please enter an odd number of rows between 1 and 19: ");
    scanf("%d", &rows);

    // Ensure the user inputs an odd number between 1 and 19
    while (rows % 2 == 0 || rows < 1 || rows > 19) {
        printf("Please enter an odd number of rows between 1 and 19: ");
        scanf("%d", &rows);
    }

    // Create the upper half of the diamond
    for (i = 1; i <= rows; i += 2) {
        // Calculate the space before the asterisk
        space = (rows - i) / 2;
        // Calculate the number of asterisks per row
        asterisks = i;

        // Print the space that leads the tip of the diamond
        for (j = 1; j <= space; j++) {
            printf("%s", " ");
        }

        // Print the asterisks for the top of the diamond
        for (j = 1; j <= asterisks; j++) {
            printf("%s", "*");
        }

        //Skip to the next line for each iteration of the loop
        printf("\n%s", "");
    }

    // Create the lower half of the diamond
    for (i = rows - 2; i >= 1; i -= 2) {
        // Calculate the space before the asterisk
        space = (rows - i) / 2;
        // Calculate the number of asterisks per row
        asterisks = i;

        // Print the leading spaces
        for (j = 1; j <= space; j++) {
            printf("%s", " ");
        }

        // Print the asterisks for the lower part of the diamond
        for (j = 1; j <= asterisks; j++) {
            printf("%s", "*");
        }

        //Skip to the next line for each iteration of the loop
        //printf with new line
        //classwork update pending
        printf("\n%s", "");
    }
}

    /*
    char pattern[] = "";
    int size = 0;

    puts("Please enter the size of the pattern: ");
    scanf("%d", &size);

    for (int i = 0; i < size; i++) {
        strcat(pattern, "*");
        puts(pattern);
    }
    */

    //int row = 0;
    //printf("%s", "please enter the row: ");
    //scanf("%d", &row);
    /*
    for (int i = 1; i <= row; i++){
        for (int j = 1; j <= i; j++) {
            printf("%s", "*");
        }
        puts(" ");
    }
    for (int i = row; i >= 1; i--){
        for (int j = 1; j <= i; j++) {
            printf("%s", "*");
        }
        puts(" ");
    }
    */

    /*
    for (int i = 0; i < row; i++){
        for (int j = row; j > i; j--) {
            printf("%s", "*");
        }
        puts(" ");
    }
    *///below prints out 4
    //****
    // ***
    //  **
    //   *
    /*
    puts(" ");
    for (int i = 0; i < row; i++){
        for (int j = 0; j < i; j++) {
            printf("%s", " ");
        }
        for (int k = i; k < row; k++) {
            printf("%s", "*");
        }
        puts(" ");
    }
    puts (" ");
    for (int i = 0; i < row; i++) {
        for (int j = 0; j < row; j++) {
            if (j < i) {
                printf("%s", " ");
            }
            else {
                printf("%s", "*");
            }
        }
        puts(" ");
    }
    */
    printf("Hello");



    //Djistance formula simple project
    #include <stdio.h>
#include <math.h>

// Helper function that calculates the distance
double distance(double x1, double y1, double x2, double y2) {
    // Calculating the difference between x and y
    double dist_x = x2 - x1;
    double dist_y = y2 - y1;

    // Using the formula x2 - x1^2 and y2 - y1^2 with the sqrt() and pow() math.h functions
    return sqrt(pow(dist_x, 2) + pow(dist_y, 2));
}

double main() {
    double x1, y1, x2, y2;

    // Prompting the user for the first positions x and y values
    printf("Enter the first points X and Y coordinates Enter(x then y):\n");
    scanf("%lf %lf", &x1, &y1);

    // Prompting the user for the second positions x and y values
    printf("Enter the second points X and Y coordinates Enter(x then y):\n");
    scanf("%lf %lf", &x2, &y2);

    // Calling the distance helper function to calculate the distance
    //  between the two points and return the value to dist
    double dist = distance(x1, y1, x2, y2);

    // Printing the calculated distance with three decimals
    printf("The distance between these points is: %.3lf\n", dist);

    return dist;
}



/*
COP3223 Summer 2023 Assignment 2_1
Copyright 2023 Gravelat Morgan
*/

#include <stdio.h>
#include <stdlib.h>
#include <time.h>

// Function to generate a random number within the specified difficulty level
int numberPicker(int diff) {
    int num;
    if (diff == 1) {
        num = rand() % 10 + 1;   // Generating a random number between 1 and 10 (inclusive)
    } else if (diff == 2) {
        num = rand() % 100 + 1;  // Generating a random number between 1 and 100 (inclusive)
    } else {
        num = rand() % 1000 + 1; // Generating a random number between 1 and 1000 (inclusive)
    }

    return num;
}

int main(void) {
    int play = 1;         // Variable to control the game loop
    int difficulty;       // Variable that holds the difficulty setting of the game per run
    int number;           // Variable that holds the number that the player is trying to guess each game
    int guess;            // Variable that holds the guess the user gave
    int guesses = 0;      // Counter to keep track of the number of guesses

    srand(time(NULL));   // Seed the random number generator with the current time

    while (play) {
        printf("Let's play Guess the Number\n");
        printf("Pick a difficulty level (1, 2, 3): ");
        scanf("%d", &difficulty);  // Prompt the user to choose the difficulty level

        number = numberPicker(difficulty);  // Generate a random number based on the chosen difficulty

        printf("I have my number. What's your guess? ");
        scanf("%d", &guess);
        guesses++;

        while (guess != number && guesses < 8) {  // Keep looping until the guess is correct or the maximum number of guesses is reached
            guesses++;
            if (guess > number) {
                printf("Too high. Guess again: ");  // Provide feedback if the guess is too high
            } else {
                printf("Too low. Guess again: ");   // Provide feedback if the guess is too low
            }
            scanf("%d", &guess);  // Prompt the user for the next guess
        }

        if (guesses < 8) {
            printf("You got it in %d guesses!\n", guesses);  // Display the number of guesses if the number is correctly guessed
        } else {
            printf("Better luck next time\n");  // Display a message if the maximum number of guesses is reached
        }

        guesses = 0;  // Reset the guess counter for the next game
        printf("Play again? (1 for yes or 0 for no): ");
        scanf("%d", &play);  // Prompt the user if they want to play again
    }

    return 0;
}


/**
 * @param {string} s
 * @param {string} t
 * @return {boolean}
 */
var isOneEditDistance = function(s, t) {
  const len = Math.max(s.length, t.length)
  for (let i = 0; i < len; i++) {
    if (s[i] !== t[i]) {
      return s.slice(i) === t.slice(i+1)
        || s.slice(i+1) === t.slice(i)
        || s.slice(i+1) === t.slice(i+1)
    }
  }
  return false;
};

*/
/*

    Poker Shuffle C Program

*/


#include <stdio.h>
#include <stdlib.h>
#include <time.h>

#define SUITS 4
#define FACES 13
#define CARDS 52

// Prototypes
void shuffle(int deck[][FACES]);
void deal(int deck[][FACES], const char *face[], const char *suit[], int hand[][2]);
int hasPair(const int hand[][2]);
int hasTwoPairs(const int hand[][2]);
int hasThreeOfAKind(const int hand[][2]);
int hasFourOfAKind(const int hand[][2]);
int hasFlush(const int hand[][2]);
int hasStraight(const int hand[][2]);

int main(void) {
    // Creating deck array
    int deck[SUITS][FACES] = {0};

    srand(time(NULL)); // Setting time for random generation
    shuffle(deck); // Shuffling deck

    // Creating suits array
    const char *suit[SUITS] = {"Hearts", "Diamonds", "Clubs", "Spades"};

    // Creating face array
    const char *face[FACES] = {"Ace", "Deuce", "Three", "Four", "Five",
                               "Six", "Seven", "Eight", "Nine", "Ten",
                               "Jack", "Queen", "King"};

    int hand[5][2] = {0}; // Creating array for hand information
    deal(deck, face, suit, hand); // Running the deal function with all the necessary arguments

    // If statements to check for each kind of hand possibility
    if (hasPair(hand)) {
        printf("The hand has a pair.\n");
    }

    if (hasTwoPairs(hand)) {
        printf("The hand has two pairs.\n");
    }

    if (hasThreeOfAKind(hand)) {
        printf("The hand has three of a kind.\n");
    }

    if (hasFourOfAKind(hand)) {
        printf("The hand has four of a kind.\n");
    }

    if (hasFlush(hand)) {
        printf("The hand has a flush.\n");
    }

    if (hasStraight(hand)) {
        printf("The hand has a straight.\n");
    }

    return 0;
}

// Shuffle the deck
void shuffle(int deck[][FACES]) {
    // Randomly choosing slots for the cards
    for (size_t card = 1; card <= CARDS; ++card) {
        size_t row = 0; // Row number
        size_t column = 0; // Column number

        // Do-while structure to choose locations until empty slot is found
        do {
            row = rand() % SUITS;
            column = rand() % FACES;
        } while(deck[row][column] != 0);

        deck[row][column] = card; // Places card data into chosen spot
    }
}

// Function that deals out the hand
void deal(int deck[][FACES], const char *face[], const char *suit[], int hand[][2]) {
    // Chooses a card for each card in the user's hand
    for (size_t card = 1; card <= 5; ++card) {
        // Loops through the rows in the deck
        for (size_t row = 0; row < SUITS; ++row) {
            // Loops through the current row's columns
            for (size_t column = 0; column < FACES; ++column) {
                // If a current card is there, it displays
                if (deck[row][column] == card) {
                    printf("%5s of %-8s\n", face[column], suit[row]); // Should still be two column format
                    hand[card - 1][0] = column; // Stores the face value in the hand
                    hand[card - 1][1] = row; // Stores the suit value in the hand
                }
            }
        }
    }
}
// Determine if hand has a pair
int hasPair(const int hand[][2]) {
    int frequency[FACES] = {0}; // array to store frequency of each face value

    // Count the frequency of each face value
    for (int i = 0; i < 5; ++i) {
        frequency[hand[i][0]]++;
    }

    // Check if any face value has a frequency of 2
    for (int i = 0; i < FACES; ++i) {
        if (frequency[i] == 2) {
            return 1; // Pair found
        }
    }

    return 0; // No pair found
}
// Determine if hand has two pairs
int hasTwoPairs(const int hand[][2]) {
    int frequency[FACES] = {0}; // array to store frequency of each face value
    int pairCount = 0; // count of pairs

    // Count the frequency of each face value
    for (int i = 0; i < 5; ++i) {
        frequency[hand[i][0]]++;
    }

    // Check if any face value has a frequency of 2
    for (int i = 0; i < FACES; ++i) {
        if (frequency[i] == 2) {
            pairCount++;
        }
    }

    return pairCount == 2; // Two pairs found if the pair count is 2
}

// Determine if hand has three of a kind
int hasThreeOfAKind(const int hand[][2]) {
    int frequency[FACES] = {0}; // array to store frequency of each face value

    // Count the frequency of each face value
    for (int i = 0; i < 5; ++i) {
        frequency[hand[i][0]]++;
    }

    // Check if any face value has a frequency of 3
    for (int i = 0; i < FACES; ++i) {
        if (frequency[i] == 3) {
            return 1; // Three of a kind found
        }
    }

    return 0; // No three of a kind found
}

// Determine if hand has four of a kind
int hasFourOfAKind(const int hand[][2]) {
    int frequency[FACES] = {0}; // array to store frequency of each face value

    // Count the frequency of each face value
    for (int i = 0; i < 5; ++i) {
        frequency[hand[i][0]]++;
    }

    // Check if any face value has a frequency of 4
    for (int i = 0; i < FACES; ++i) {
        if (frequency[i] == 4) {
            return 1; // Four of a kind found
        }
    }

    return 0; // No four of a kind found
}
// Determine if hand hasa flush
int hasFlush(const int hand[][2]) {
    int suit = hand[0][1]; // Suit of the first card

    // Check if all cards have the same suit
    for (int i = 1; i < 5; ++i) {
        if (hand[i][1] != suit) {
            return 0; // Not a flush
        }
    }

    return 1; // Flush found
}

// Determine if hand has a straight
int hasStraight(const int hand[][2]) {
    int frequency[FACES] = {0}; // array to store frequency of each face value

    // Count the frequency of each face value
    for (int i = 0; i < 5; ++i) {
        frequency[hand[i][0]]++;
    }

    // Check for a straight starting from Ace
    if (frequency[0] && frequency[1] && frequency[2] && frequency[3] && frequency[12]) {
        return 1; // Straight found
    }

    // Check for a straight starting from other face values
    for (int i = 1; i <= 9; ++i) {
        if (frequency[i] && frequency[i+1] && frequency[i+2] && frequency[i+3] && frequency[i+4]) {
            return 1; // Straight found
        }
    }

    return 0; // No straight found
}
// END OF POKER HAND PROGRAM
