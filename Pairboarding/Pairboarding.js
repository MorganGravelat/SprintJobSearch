/*
Problem 1
Jewels and Stones

You are given two strings, J and S. String J represents the types of stones that are jewels. String S represents all of the stones that you have. Each character in string S is a type of stone you have. You want to know how many of your stones are also jewels.

Contraints

    The letters in J are guaranteed distinct.
    All characters in J and S are letters.
    Letters are case-sensitive, so "a" is considered a different type of stone from "A".

Example 1:

Input: J = "aA", S = "aAAbbbb"
Output: 3

Example 2:

Input: J = "z", S = "ZZ"
Output: 0




Objective:
    - given two strings
    - each character is type of stone
    - return how many jewels in stone ring

Edge-Cases:
    - Notes:
        - all the characters in jewel string are unique
    - if either string is an empty string
        - return 0
Strategy:
    - declare counter variable
    - declar dictionary
    - iterate over jewel string
        - if current character is not in dictionary
            - add to dictionary
        0 iterate through the stone string
            - if current stone character key exists in dictionary
                - increment the counter by one
*/


function numJewels(jewels, allStones) {
    let count = 0;
    const store = {};

    for (let i = 0; i < jewels.length; i++) {
      store[jewels[i]] = true;
    }

    for (let j = 0; j < allStones.length; j++) {
      if (store[allStones[j]]) count += 1;
    };

    return count;
  }


function isIsomorphic(string_one, string_two) {
    if (string_one.length !== string_two.length) return false

    let charDict = {}

    for (let i = 0; i < string_one.length; i++) {
        let char_one = string_one[i]
        let char_two = string_two[i]

        if (charDict[char_one] === undefined) {
            charDict[char_one] = char_two
        }
        else if (charDict[char_one] !== char_two) {
            return false
        }
    }

    return true
}

console.log(isIsomorphic("egg", 'add')); // true


function sortStack(stack) { //[4, 2, 1]
    let smallerValue = 0
    let largerValue = 0
    if (stack.length <= 1) {
      return stack
    }

    let valueOne = stack.pop() //value = 1 [4, 2] // val = 2
    console.log(stack)
    sortStack(stack) [4, 2]
    let valueTwo = stack.pop() //value = 2 [4]

    if (valueOne < valueTwo) {
      smallerValue = valueOne
      largerValue = valueTwo
    }
    else {
      smallerValue = valueTwo
      largerValue = valueOne
    }
    stack.push(smallerValue)
    sortStack(stack)
    stack.push(largerValue)

    return stack
  }
