/*
COP3223 Summer 2023 Assignment 2_3
Copyright 2023 Gravelat Morgan
*/

#include <stdio.h>

#define TOTAL_SEATS 6
#define FIRST_CLASS_CAPACITY 3

int main() {
    int seats[TOTAL_SEATS] = {0}; // Array to represent the seating chart (0 for empty, 1 for occupied)

    int boarded = 0; // Variable to track if everyone has boarded (0 for not boarded, 1 for boarded)

    while (!boarded) {
        int choice;
        printf("Please type 1 for \"first class\"\n");
        printf("Please type 2 for \"economy\"\n");
        scanf("%d", &choice);

        if (choice == 1) {
            // First class seat assignment
            int i;
            for (i = 0; i < FIRST_CLASS_CAPACITY; i++) {
                if (seats[i] == 0) {
                    seats[i] = 1; // Assign the seat
                    printf("Your seat is assigned to first class seat %d\n", i + 1);
                    break;
                }
            }

            if (i == FIRST_CLASS_CAPACITY) {
                // No first class seats available
                printf("Next flight leaves in 3 hours.\n");
            }
        } else if (choice == 2) {
            // Economy seat assignment
            int i;
            for (i = FIRST_CLASS_CAPACITY; i < TOTAL_SEATS; i++) {
                if (seats[i] == 0) {
                    seats[i] = 1; // Assign the seat
                    printf("Your seat is assigned to economy seat %d\n", i + 1);
                    break;
                }
            }

            if (i == TOTAL_SEATS) {
                // No economy seats available
                printf("No seat available in economy, do you want a seat in first class? ");
                scanf("%d", &choice);

                if (choice == 1) {
                    int j;
                    for (j = 0; j < FIRST_CLASS_CAPACITY; j++) {
                        if (seats[j] == 0) {
                            seats[j] = 1; // Assign the first class seat
                            printf("Your seat is assigned to first class seat %d\n", j + 1);
                            break;
                        }
                    }

                    if (j == FIRST_CLASS_CAPACITY) {
                        // No first class seats available
                        printf("Next flight leaves in 3 hours.\n");
                    }
                } else {
                    printf("Next flight leaves in 3 hours.\n");
                }
            }
        }

        printf("Has everyone boarded? ");
        scanf("%d", &boarded);
    }

    return 0;
}
