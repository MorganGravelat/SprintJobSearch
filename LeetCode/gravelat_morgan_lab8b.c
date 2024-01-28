#include <stdio.h>
#include <stdlib.h>



void expandSize(int **arr, int *size);
void displayArray(int *arr, int size);
int search(int *arr, int size, int num);


int main() {
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