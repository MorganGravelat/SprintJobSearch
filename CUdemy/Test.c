/*
COP3223 Summer 2023 Assignment 2_3
Copyright 2023 Gravelat Morgan
*/

#include <stdio.h>
#include <stdlib.h>
#include <time.h>

#define TOTAL_SEATS 6
#define FIRST_CLASS_CAPACITY 3

// Function to print the boarding pass based on seat number and class type
void print_boarding_pass(int seatNumber, int classType) {
    if (classType == 1) {
        printf("Your seat is assigned to first class seat %d\n", seatNumber);
    } else {
        printf("Your seat is assigned to economy seat %d\n", seatNumber);
    }
}

// Function to search for an available seat within a given range
int search_seat(int seats[], int start, int end) {
    int availableSeats[TOTAL_SEATS] = {0};  // Array to store available seats
    int count = 0;  // Counter for available seats

    // Iterate over the seats within the given range
    for (int i = start; i <= end; i++) {
        if (seats[i] == 0) {
            availableSeats[count] = i;  // Store the index of available seat
            count++;
        }
    }

    if (count == 0) {
        return -1;  // No available seats found
    }

    // Generate a random index within the available seats
    int randomIndex = rand() % count;
    return availableSeats[randomIndex];  // Return the selected seat index
}

int main() {
    int seats[TOTAL_SEATS] = {0};  // Array to represent the seating chart
    int allBoarded = 0;  // Variable to track if everyone has boarded 
    
    srand(time(0));  // Initialize random seed for seat selection
    
    while (!allBoarded) {
        int choice;
        printf("Please type 1 for \"first class\"\n");
        printf("Please type 2 for \"economy\"\n");
        scanf("%d", &choice);

        if (choice == 1) {
            // First class seat selection
            int seatNumber = search_seat(seats, 0, FIRST_CLASS_CAPACITY - 1);

            if (seatNumber != -1) {
                seats[seatNumber] = 1;  // Mark the seat as occupied
                print_boarding_pass(seatNumber + 1, choice);  // Print boarding pass
            } else {
                printf("No seat available in first class.\n");

                // Check if there are available seats in economy class
                if (search_seat(seats, FIRST_CLASS_CAPACITY, TOTAL_SEATS - 1) != -1) {
                    int transferChoice;
                    printf("Do you want a seat in economy class? ");
                    scanf("%d", &transferChoice);

                    if (transferChoice == 1) {
                        // Economy class seat selection
                        seatNumber = search_seat(seats, FIRST_CLASS_CAPACITY, TOTAL_SEATS - 1);

                        if (seatNumber != -1) {
                            seats[seatNumber] = 1;
                            print_boarding_pass(seatNumber + 1, 2);  // Print boarding pass for economy class
                        } else {
                            printf("No seat available in economy class.\n");
                        }
                    } else {
                        printf("Next flight leaves in 3 hours.\n");
                    }
                } else {
                    printf("Next flight leaves in 3 hours.\n");
                }
            }
        } else if (choice == 2) {
            // Economy class seat selection
            int seatNumber = search_seat(seats, FIRST_CLASS_CAPACITY, TOTAL_SEATS - 1);

            if (seatNumber != -1) {
                seats[seatNumber] = 1;  // Mark the seat as occupied
                print_boarding_pass(seatNumber + 1, choice);  // Print boarding pass
            } else {
                printf("No seat available in economy class.\n");

                // Check if there are available seats in first class
                if (search_seat(seats, 0, FIRST_CLASS_CAPACITY - 1) != -1) {
                    int transferChoice;
                    printf("Do you want a seat in first class? ");
                    scanf("%d", &transferChoice);

                    if (transferChoice == 1) {
                        // First class seat selection
                        seatNumber = search_seat(seats, 0, FIRST_CLASS_CAPACITY - 1);

                        if (seatNumber != -1) {
                            seats[seatNumber] = 1;
                            print_boarding_pass(seatNumber + 1, 1);  // Print boarding pass for first class
                        } else {
                            printf("No seat available in first class.\n");
                        }
                    } else {
                        printf("Next flight leaves in 3 hours.\n");
                    }
                } else {
                    printf("Next flight leaves in 3 hours.\n");
                }
            }
        }

        printf("Has everyone boarded? ");
        scanf("%d", &allBoarded);
    }

    return 0;
}
