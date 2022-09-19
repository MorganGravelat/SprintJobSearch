#include <iostream>
#include <fstream>
#include <cmath>
#include <string>
#include <vector>
#include <algorithm>

using namespace std;

int main()
{
    string file; //txt files
    char letters; //alphabet
    char output[100]; //output of code
    int alph[26] = {65,66,67,68,69,70,71,72,73,74,75,76,77,78,79,80,81,82,83,84,85,86,87,88,89,90};

    cout << "File? ";
    cin >> file;


    ifstream myReadFile;
    myReadFile.open(file);
    if (myReadFile.is_open())
    {
        while (!myReadFile.eof())
        {
            myReadFile >> output;

            cout << output << string(1, ' '); //creates a space between words

        }

    }
    myReadFile.close();

    return 0;
}
