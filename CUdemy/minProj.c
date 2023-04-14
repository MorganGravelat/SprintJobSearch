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


*/
