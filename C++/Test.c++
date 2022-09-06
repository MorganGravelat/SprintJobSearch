#include <iostream>
#include <string>
#include <iomanip>
#include <cmath>
#include <fstream>

using namespace std;

int main()
{
    string txt;
    char firstChar;
    int coordNum;
    bool first_second = true;
    cout << "Data? "; cin >> txt; cout << endl;
    ifstream inFile (txt);


    if (inFile.is_open())
    {
        while (getline (inFile, txt))
        {
            if (first_second)
            {
              firstChar = txt[0];
              coordNum = txt[1];
              cout << int(firstChar)
              cout << "Origin";
              cout << setw(16) << setfill('.');
              cout << txt << endl;
              first_second = false;
            }
            else
            {
              cout << "Destination";
              cout << setw(11) << setfill('.');
              cout << txt << endl;
            }
            // cout << txt << '\n';
        }
        cout << "Miles";
        inFile.close();
    }
    else cout << "Unable to open file";
    return 0;

}
