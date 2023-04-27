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

*/
