/*
Please write a program which do following:

1) Allow user keep entering numbers until user enter -1, which indicates user entered all numbers

2) Store the numbers in a dynamic array.

3) Initialize the dynamic array size to 4

4) Display all the elements

5) Ask user to enter a number and search if that number is in the array.

6) Create a function called expandSize which double the size of the array when the its size reaches the limit

7) Create a function called displayArray which print out all the elements in the array

8) Create a function called search, which search is a given number is inside the array. Return the index of that number if it is in the array, return -1 if the number not found in the array.

9) All functions include at least one parameter which receive the dynamic array by reference
*/

#include <stdio.h>
#include <stdlib.h>



void expandSize(int **arr, int *size);
void displayArray(int *arr, int size);
int search(int *arr, int size, int num);
void sortArray(int *arr, int siz)

int main()
{
    int *numbers = (int *)malloc(4 * sizeof(int));
    int size = 4;
    int ind = 0;
    int num;

    printf("Enter numbers (-1 to stop):\n");

    while(1) {
        scanf("%d", &num);

        if (num == -1) { //test bracket need
            break;
        }

        numbers[ind++] = num;

        if (ind == size) {
            expandSize(&numbers, &size);
        }

    }

    printf("%s\n","All elements:");
    displayArray(numbers, ind);

    printf("%s\n", "Enter a number to search: ");
    scanf("%d", &num);

    int index = search(numbers, ind, num);
    if (index != -1) {
        printf("Number %d is found at the index of %d.\n", num, index);
    } else {
        printf("Number %d not found.\n", num);
    }

    free(numbers);
    return 0;
    //int numbers[SIZE] = {0}; // initialize all elements to 0 {0,0,0,0,0}
    //malloc - memory allocation
    //calloc - memory allocation and initialize all elements to 0
    //realloc - reallocate memory
    //free - free memory
    // malloc is a function that allocate memory it is used to allocate memory for a variable or an array of variables of any data type
    // you can make an array of any size using malloc like this: int *array = (int *)malloc(100*sizeof(int));
    // this will make an array of 100 integers

}

void displayArray(int *arr, int size) {
    for (int i = 0; i < size; i++) {
        printf("%d ", arr[i]);
    }
    printf("\n");
}

int search(int *arr, int size, int num) {
    for (int i = 0; i < size; i++) {
        if (arr[i] == num) {
            return i;
        }
    }
    return -1;
}

void expandSize(int **arr, int *size) {
    *size *= 2;
    int *newArr = (int *)realloc(*arr, (*size) * sizeof(int));
    *arr = newArr;
}
/*

NEW BINARY FUNCTION


*/

#include <stdio.h>
#include <stdlib.h>



void expandSize(int **arr, int *size);
void displayArray(int *arr, int size);
int search(int *arr, int size, int num);
void sortFunction(int *arr, int size);

int main()
{
    int *numbers = (int *)malloc(4 * sizeof(int));
    int size = 4;
    int count = 0;
    int num;

    printf("Enter numbers (-1 to stop):\n");

    while(1) {
        scanf("%d", &num);

        if (num == -1) { //test bracket need
            break;
        }
        numbers[count++] = num;

        if (count == size) {
            expandSize(&numbers, &size);
        }

    }

    sortFunction(numbers, count);
    printf("%s\n","All elements:");
    displayArray(numbers, count);

    printf("%s\n", "Enter a number to search: ");
    scanf("%d", &num);

    int index = search(numbers, count, num);
    if (index != -1) {
        printf("Number %d is found at the index of %d.\n", num, index);
    } else {
        printf("Number %d not found.\n", num);
    }

    free(numbers);
    return 0;
    //int numbers[SIZE] = {0}; // initialize all elements to 0 {0,0,0,0,0}
    //malloc - memory allocation
    //calloc - memory allocation and initialize all elements to 0
    //realloc - reallocate memory
    //free - free memory
    // malloc is a function that allocate memory it is used to allocate memory for a variable or an array of variables of any data type
    // you can make an array of any size using malloc like this: int *array = (int *)malloc(100*sizeof(int));
    // this will make an array of 100 integers

}

void displayArray(int *arr, int size) {
    for (int i = 0; i < size; i++) {
        printf("%d ", arr[i]);
    }
    printf("\n");
}

int search(int *arr, int size, int num) {
    for (int i = 0; i < size; i++) {
        if (arr[i] == num) {
            return i;
        }
    }
    return -1;
}

void expandSize(int **arr, int *size) {
    *size *= 2;
    int *newArr = (int *)realloc(*arr, (*size) * sizeof(int));
    *arr = newArr;
}

void sortFunction(int *arr, int size) {
    for (int i = 1; i < size; i++) {
        int key = arr[i];
        int left = 0;
        int right = i - 1;
        int j;
        while (left <= right) {
            int mid = (left + right) / 2;

            if (key < arr[mid]) {
                right = mid - 1;
            } else {
                left = mid + 1;
            }
        }

        for (j = i - 1; j >= left; j--) {
            arr[j + 1] = arr[j];
        }
        arr[j + 1] = key;

    }
}
// void insertFunction(int *arr, int size, int num) {
//     int i = size - 1;

//     while (i >= 0 && arr[i] > num) {
//      arr[i + 1] = arr[i];
//      i--;
//     }
//     arr[i+1] = num;
// }

//BELOW CODE
#include <stdio.h>
#include <stdlib.h>



void expandSize(int **arr, int *size);
void displayArray(int *arr, int size);
int search(int *arr, int size, int num);
void sortFunction(int *arr, int size);

int main()
{
    int *numbers = (int *)malloc(4 * sizeof(int));
    int size = 4;
    int count = 0;
    int num;

    printf("Enter numbers (-1 to stop):\n");

    while(1) {
        scanf("%d", &num);

        if (num == -1) { //test bracket need
            break;
        }
        numbers[count++] = num;

        if (count == size) {
            expandSize(&numbers, &size);
        }

    }

    sortFunction(numbers, count);
    printf("%s\n","All elements:");
    displayArray(numbers, count);

    printf("%s\n", "Enter a number to search: ");
    scanf("%d", &num);

    int index = search(numbers, count, num);
    if (index != -1) {
        printf("Number %d is found at the index of %d.\n", num, index);
    } else {
        printf("Number %d not found.\n", num);
    }

    free(numbers);
    return 0;

}

void displayArray(int *arr, int size) {
    for (int i = 0; i < size; i++) {
        printf("%d ", arr[i]);
    }
    printf("\n");
}

int search(int *arr, int size, int num) {
    for (int i = 0; i < size; i++) {
        if (arr[i] == num) {
            return i;
        }
    }
    return -1;
}

void expandSize(int **arr, int *size) {
    *size *= 2;
    int *newArr = (int *)realloc(*arr, (*size) * sizeof(int));
    *arr = newArr;
}

void sortFunction(int *arr, int size) { //[4, 2, 3, 1]
    for (int i = 1; i < size; i++) { // i1
        int key = arr[i];
        int left = 0;
        int right = i - 1;
        int j;
        while (left <= right) {
            int mid = (left + right) / 2;

            if (key < arr[mid]) {
                right = mid - 1;
            } else {
                left = mid + 1;
            }
        }

        for (j = i - 1; j >= left; j--) {
            arr[j + 1] = arr[j];
        }
        arr[j + 1] = key;

    }
}
