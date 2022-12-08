//class and a struct
#include <iostream>
#include <string>
using namespace std;

class Kyle {
    private:
    string name;

    public:
    void setName(string x) {
        name = x;
    }
    string getName() const {
        return name;
    }
    void speak() {
        cout << "I am " << name << " and I am dumb." << endl;
    }
    };

int main() {
    Kyle kyle;
    kyle.setName("Kyle");
    kyle.speak();
    return 0;
}
