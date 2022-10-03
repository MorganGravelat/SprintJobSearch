#include <iostream>
#include <cmath>
#include <iomanip>
#include <algorithm>
#include <string>
#include <string.h>
#include <fstream>
#include <limits>
#include <cstdlib>


//THREE FUNCTIONS ARE REQUIRED OTHER THAN INT MAIN

using namespace std;
int flippedNum;

int dishNum() {
	int lineNumber;
	srand(time(0)); // To seed the random number
	int sign = rand() % 5 + 1; // To establish a randomized number

	cout << "Num? ";
	cin >> lineNumber; // *** THIS IS THE NUMBER INPUT ***

	if (lineNumber < 1 || lineNumber > 5) {

		lineNumber = sign;
	}

	return lineNumber;
}


string periods(string line) // Helper function taking in string of word selected by user
{
	string dots;
	for (int i = 0; i < line.length(); i++) // String line loop
	{

		char elem = line[i];

		if (elem != ' ') // DOUBLE QUOTES ARE CONSIDERED CONST CHAR, SINGLE QUOTES ARE CHAR
		{
			dots += '.';

		}
		else dots += ' ';



	}






	return dots;


}

string letters(string line) {
	string guesses;
	string userLett; //User inputs letters 
	

	cout << "Letters? ";

	cin.ignore();	     // Stops a new line from happening
	getline(cin, guesses); // Inputs the guess (With spaces)
	
	for (int i = 0; i < line.length(); i++) { // GOES THROUGH EVERY CHARACTER, IF GUESS INCLUDES THE CHAR OR THE CHAR IS A SPACE, ADDS CHAR BACK

		char ele = line[i];

		if (ele == ' ') {

			userLett += ele;

		}
		else if (guesses.find(ele) < guesses.length()) {

		
			userLett += ele;
			flippedNum++;
		
		}
		else {

			userLett += '.';

		}


	}
	cout << "You have flipped " << flippedNum << " letters" << endl << endl;
	
	

	return userLett;
}




int getLine() {

	string line; // Variable I am using for COUT'ing the specific line
	ifstream file("dishes.txt"); // Pulls information from the .txt file
	int currentLine = 0; // For the system to loop through the lines, "0" initializes the variable for usage
	int lineNumber = dishNum(); // Variable for user input saying which line to pick
	string peds;
	string guess;
	bool guessing = true;
	int strikes = 0;

	while (file.is_open()) // While the file is currently opened
	{
		currentLine++; // Increment to each line to match the line the user inputted
		getline(file, line); // "File" represents where the info is being pulled from, "line" represents the variable depicting what line is being read
		if (currentLine == lineNumber) break; // Stops the loop if the line that the computer is currently on matches the number the user inputted
	}
	

	peds = periods(line);


	cout << endl;
	cout << peds << endl;
	cout << letters(line) << endl;

	
	while (guessing) {
		cout << "Dish? ";
		getline(cin, guess); // Inputs the guess (With spaces)
		if (guess == line)
		{	
			guessing = false;
			cout << endl;
			cout << "Congrats! ";
			cout << "You have won $" << flippedNum * 100 << endl;
			break;
		}
		strikes++;
		if (strikes <= 2) {
			
			cout << endl << strikes << " strikes" << endl;

		}

		else {
	
			guessing = false;
			cout << endl;
			cout << strikes << " strikes!" << endl;
			cout << "It was: " << line;
		}
		

	}
	
	file.close();

	return 0;
}







int main()
{

	getLine();
	

	

	return 0; 
}

