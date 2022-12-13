#include <iostream>


using namespace std;

int* sortAscending(int numbers[], int size) {
	int* sortNumber = new int[size];
	for (int i = 0; i < size; i++) {
		sortNumber[i] = numbers[i];
	}
	for (int i = 0; i < size; i++) {
		for (int j = i + 1; j < size; j++) {
			if (sortNumber[i] > sortNumber[j]) {
				int var = sortNumber[i];
				sortNumber[i] = sortNumber[j];
				sortNumber[j] = var;
			}
		}
	}
	return sortNumber;
}

int main() {
	int numbers[] = { 2, 5, 1 ,3, 10, 8, 7, 4, 6 };
	int size = sizeof(numbers) / 4;
	int* sortedNumbers = sortAscending(numbers, size);
	for (int i = 0; i < size; i++) {
		cout << sortedNumbers[i] << " ";
	}
	return 0;
}
