        }
        else {
            coding = -13;

        }
    }

    if (any_of(begin(alph), end(alph), [=](int n) {return n == z; })) {

        store = (z - 65) + coding;
        if (store > 26) {
            store = store % 26;
        }
    }
    else if (isNum) {


    }
    return store; // what the function will output (end)
}


int main()
{
    string file; //txt files
    char letters; //alphabet
    char output[100]; //output of code
    bool x;
    char y;
    string result;

    cout << "File? ";
    cin >> file;


    ifstream myReadFile;
    myReadFile.open(file);
    if (myReadFile.is_open())
    {
        while (!myReadFile.eof())
        {
            myReadFile >> output;
            for (int i = 0; i < strlen(output); i++) {
                x = isupper(output[i]);
                y = toupper(output[i]);

                cout << mainFun(y, x, file);

            }
            cout << output << string(1, ' '); //creates a space between words



        }

    }

    myReadFile.close();

    return 0;
}
