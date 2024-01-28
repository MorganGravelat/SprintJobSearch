#include <stdio.h>
#include <stdlib.h>
//Above are the neccessary headers for the assignment

#define ALPHABET_LENGTH 26 //A constant length for the alphabet that I can use in creeation of the frequency array and the loop that finds new letters

int main() {
    // Use malloc to allocate memory for the two input messages
    char *firstMessage = (char *)malloc(100002 * sizeof(char));
    char *secondMessage = (char *)malloc(100002 * sizeof(char));

    // Input the first message
    fgets(firstMessage, 100002, stdin);

    // Input the second Message
    fgets(secondMessage, 100002, stdin);

    // Arrays to store the frequency of each letter in the first and second message
    int firstFreq[ALPHABET_LENGTH] = {0}; //Two frequency arrays filled with 0's thaat are 26 length 0-25 if indexed
    int secondFreq[ALPHABET_LENGTH] = {0};


    int newLettersCount = 0; // Variable to count the number of new letters needed

    // Populate frequency array for the original message
    for (int i = 0; firstMessage[i] != '\0'; i++) {
        if (firstMessage[i] != ' ') {
            firstFreq[firstMessage[i] - 'A']++;
        }
    }

    // Populate frequency array for the new message
    for (int i = 0; secondMessage[i] != '\0'; i++) {
        if (secondMessage[i] != ' ') {
            secondFreq[secondMessage[i] - 'A']++;
        }
    }

    // Calculate the number of new letters needed
    for (int i = 0; i < ALPHABET_LENGTH; i++) {
        if (firstFreq[i] < secondFreq[i]) {
            newLettersCount += secondFreq[i] - firstFreq[i];
        }
    }

    // Print the result
    printf("%d\n", newLettersCount);

    // Free allocated memory
    free(firstMessage);
    free(secondMessage);

    return 0;
}
