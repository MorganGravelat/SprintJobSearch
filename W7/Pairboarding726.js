/* Objective:
    - function isIsomorphic()
    - identify is string is isomorphic aka e g g AND a d d follow the same pattern
    - return if isomorphic true and if not false
    Edge-Cases:
        - Notes:
            -strings are different lengths
            -strings are empty
                - if either case is hit
                    - return false
    Strategy:
        - Check for edge cases
        - Declare a dictionary for the characters within the two strings
        - Create a for loop, that loops through the length of the first string
        - If this is the first occurance of a letter, match a key value pair with the same index of character in the other string
        -






*/

function isIsomorphic(string_one, string_two) {

    if (string_one.length !== string_two.length) return false;
    if (string_one.length < 1 || string_two.length < 1) return false;

    let charHashMap = {}

    for (let i = 0; i < string_one.length; i++) {
        let char_one = string_one[i] // p
        let char_two = string_two[i] // t 'p': 't' / 'a': 'i' / 'e': 'l' / 'r': 'e'

        if (charHashMap[char_one] === undefined) {
            charHashMap[char_one] === char_two
        }
        else if (charHashMap[char_one] !== char_two) {
            return false
        }
    }
    return true
}

console.log(isIsomorphic("paper", 'title'));


/* Objective:
    - function isBalanced()
    - identify if string input has a balance of opening and closing parentheses
    - return true if balanced and false if unbalanced
    Edge-Cases:
        -strings are empty
        -string is odd
            -if either case is true, return false
    Strategy:
        - Check for edge cases
        - Declare a counter that evaluates the opening and closing parantheses and stays zero when they are balanced







*/


function isBalanced(string) {
    if (string.length < 1 || string.length % 2 !== 0) {
        return false;
    }

    let counter = 0;

    for (let i = 0; i < string.length; i++) {
        if (string[i] === "(") {
            counter--;
            console.log(counter)
        }
        else if(string[i] === ")") {
            counter++;
            console.log(counter)
        }
    }
    if (counter !== 0) return false
    else return true;
}

console.log(isBalanced('(()))')) //false
console.log(isBalanced('((())))')) //true
