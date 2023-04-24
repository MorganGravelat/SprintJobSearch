"use strict";
// let x = 4; // Error: Cannot redeclare block-scoped variable 'x'.
//x.length(); // Error: Property 'length' does not exist on type 'number'.
// let x = 4;
// console.log(x); //
let x = 4;
let y = 4;
let s = 'string';
let b = true;
let v = false;
let isAnswered = true;
console.log(x);
//num = '5'; // Error: Type '"5"' is not assignable to type 'number'.
//let strArray: string = []; // Error: Type 'string[]' is not assignable to type 'string'.
let strArray = []; // OK
let strAr = []; // OK
//strArray.push(6); // Error: Argument of type '6' is not assignable to parameter of type 'string'.
let user = [1, 'Steve'];
user.push(7); // OK This works because push is a method of Array
console.log(user);
// Enum is group of contstants
// In Javascript we define constants using Object
// const Color = { Red: 0, Green: 1, Blue: 2 };
// const small = 0;
// In Typescript we can define constants using Enum
// enum Color { Red, Green, Blue };
// enum Color { Red = 0, Green = 1, Blue = 2 };
var Color;
(function (Color) {
    Color[Color["Red"] = 5] = "Red";
    Color[Color["Green"] = 6] = "Green";
    Color[Color["Blue"] = 7] = "Blue";
})(Color || (Color = {}));
;
var Size;
(function (Size) {
    Size[Size["Small"] = 1] = "Small";
    Size[Size["Medium"] = 2] = "Medium";
    Size[Size["Large"] = 3] = "Large";
})(Size || (Size = {}));
;
console.log(Size); // { '1': 'Small', '2': 'Medium', '3': 'Large', Small: 1, Medium: 2, Large: 3 }
