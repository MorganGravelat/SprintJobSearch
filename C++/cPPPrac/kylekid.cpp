#include <iostream>
#include <string>
#include <cstring>
#include <iomanip>
#include "KyleHead.h"

using namespace std;

Kyle::Kyle() {
    name = "Andrew";
    insult = "Big Dumb Hero To the Mexican People";
    age = 10000
}

string Kyle::getPerson() const {
    return name;
}
void Kyle::setPerson(string p) {
    name = p;
}

string Kyle::getInsult() const {
    return insult;
}
void Kyle::setInsult(string i) {
    insult = i;
}

void Kyle::print() const {
    cout << name << " is " << age << " years old and also a " << insult << endl;
}
