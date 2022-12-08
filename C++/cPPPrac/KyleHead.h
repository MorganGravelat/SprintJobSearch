# pragma once
# include "KyleHead.h"
# include <iostream>
# include <string>

using namespace std;



class Kyle {
    private:
        string name;
        string insult;
        int age;
    public:
    Kyle();
    string getPerson() const;
    void setPerson(string p);

    string getInsult() const;
    void setInsult(string i);

    void print() const;

};
