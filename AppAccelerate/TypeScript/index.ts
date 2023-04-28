// let x = 4; // Error: Cannot redeclare block-scoped variable 'x'.
//x.length(); // Error: Property 'length' does not exist on type 'number'.

// let x = 4; Test
// console.log(x); //

let x = 4;
let y: number = 4;
let s: string = 'string';
let b: boolean = true;
let v: any = false;

let isAnswered: boolean = true;

console.log(x);
//num = '5'; // Error: Type '"5"' is not assignable to type 'number'.

//let strArray: string = []; // Error: Type 'string[]' is not assignable to type 'string'.
let strArray: string[] = []; // OK
let strAr: Array<string> = []; // OK

//strArray.push(6); // Error: Argument of type '6' is not assignable to parameter of type 'string'.

let user : [number, string] = [1, 'Steve'];

user.push(7); // OK This works because push is a method of Array

console.log(user);

// Enum is group of contstants
// In Javascript we define constants using Object
// const Color = { Red: 0, Green: 1, Blue: 2 };
// const small = 0;
// In Typescript we can define constants using Enum
// enum Color { Red, Green, Blue };
// enum Color { Red = 0, Green = 1, Blue = 2 };
enum Color { Red = 5, Green, Blue };
enum Size { Small = 1};
//Size.small = 2; // Error: Property 'small' does not exist on type 'typeof Size'.
console.log(Size); // { '1': 'Small', '2': 'Medium', '3': 'Large', Small: 1, Medium: 2, Large: 3 }

console.log(Size.Small); // 1

let un: number | string;

const person: {id: number, user: string} = { id: 0, user:"Steve"};
// you need to initialize all the properties of the object
function myLog (x: any): void {
    console.log(x);
}

// const printUser = (name: string, age: number, pw: string, id: number, isSubscribed: boolean): void => {

// }

// const printUser = () : string => {
//     return "Hello"; // OK because return type is string
// }
interface userInterface { // Interface is a contract that defines the structure of an object
    name: string, pw:string, id: number, issSubscribed: boolean
}
const printUser = (user: userInterface) : string => {
    return user.name; // OK because return type is string and user is of type userInterface
}
