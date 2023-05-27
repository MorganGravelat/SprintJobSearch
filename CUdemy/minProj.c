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
*/
