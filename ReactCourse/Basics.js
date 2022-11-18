const person = {
    name: 'Max',
}

export default person; //You can export objects and functions

//utility.js
export const clean = () => {return 0} //You can export functions;
export const baseData = 10; //You can export variables
//You can import objects and functions
import person from './person.js'; // if the person.js was a file you could import it like this
//and access the person object like this

//default export
import person from './person.js'; //You can import objects and functions
import prs from './person.js'; //You can import objects and functions under a different name if it is the default export


//CLASSES
class Human {
    constructor() {
        this.gender = 'male';
    }
    printGender() {
        console.log(this.gender);
    }
}

class Person extends Human {
    constructor() {
        super(); //This constructor will call the constructor of the Human class and add gender to the Person class
        this.name = 'Max'; //You can create properties in the constructor with this
        this.gender = 'female'; //You can override properties in the constructor with this

    }

    printMyName() {
        console.log(this.name);
    }
}

const person = new Person();
person.printMyName();
//Max
person.printGender();
//female even though you are calling the original Human class printGender method YOU OVERWROTE IT IN THE NEW CLASS

//There is a modern syntax for initializing properties in classes
//OLD PROPERTY SYNTAX
constructor() {
    this.myProperty = 'value';
//MODERN SYNTAX
myProperty = 'value';

//OLD METHOD SYNTAX
printMyName() {...}
//MODERN SYNTAX
printMyName = () => {...} //We will be using the modern syntax for both method and property initialization

class Human {

    gender = 'male';

    printGender = () => {
        console.log(this.gender);
    }
}

class Person extends Human {
        name = 'Max'; //You can create properties in the constructor with this
        gender = 'female'; //You can override properties in the constructor with this


    printMyName = () => {
        console.log(this.name);
    }
}

const person = new Person();
person.printMyName();
//Max
person.printGender();


//SPREAD & REST OPERATORS
//SPREAD
const numbers = [1, 2, 3];
const newNumbers = [...numbers, 4]; //This will create a new array with the numbers array and add 4 to it
console.log(newNumbers); //[1, 2, 3, 4]

const person = {
    name: 'Max'
};

const newPerson = {
    ...person,
    age: 28
}

console.log(newPerson); //{name: "Max", age: 28}
//REST
const filter = (...args) => { //This will create an array with all the arguments passed to the function
    return args.filter(el => el === 1); //filter function will return an array with all the elements that pass the condition
}
let numbers = [1, 2, 3];
console.log(filter(...numbers)); //[1]

//DESTRUCTURING
//ARRAY DESTRUCTURING
let numbers = [1, 2, 3];

//[num1, num2, num3] = numbers; //This will create 3 variables with the values of the numbers array
//YOU CAN GRAB IN BETWEEN VALUES
[num1, , num3] = numbers; //This will create 3 variables with the values of the numbers array
console.log(num1, num2, num3); //1 2 3
let {name,age} = {name:1, age:3}; //This will create 2 variables with the values of the keys name and age
console.log(`${name}, AND ${age}`); //1 3


//REFERENCE AND PRIMITIVE TYPES REFERENCE
const number = 1; //This is a primitive type
const num2 = number; //This will create a copy of the number variable
console.log(num2); //1

const person = {
    name: 'Max'
};

const secondPerson = person; //This will create a reference to the person object

person.name = 'Manu'; //This will change the name of the person object and the secondPerson object

//{name: "Manu"} Second Person is just a pointer to person and thus changes made to person will be reflected in secondPerson
console.log(secondPerson);
//You can use spread to create a copy of an object that does not just point
const person = {
    name: 'Max'
};
const secondPerson = {
    ...person
};

person.name = 'Manu'; //This will change the name of the person object and the secondPerson object

console.log(secondPerson);
console.log(person);


//ARRAYS FUNCTIONS

const numbers = [1, 2, 3];
const doubleNumArray = numbers.map((num) => { //Map performs a function on every element of the array you use it on
    return num * 2;
});
console.log(doubleNumArray); //[2, 4, 6]

//Components
//Components are the building blocks of React
//Components are just functions that return JSX
//This is a functional component App.js
function App() {
    return (
      <div> //This is JSX
        <h2>Let's get started!</h2> //JSX You can input html in your javascript
      </div> //JSX special syntax for html in javascript created by React
    );
  }

  export default App; //You can export components
  //This is a class component App.js
//*This is translated in the background to the functional component below
function App() {
    return /*#__PURE__*/Object(react_jsx_dev_runtime__WEBPACK_IMPORTED_MODULE_0__["jsxDEV"])("div", {
      children: /*#__PURE__*/Object(react_jsx_dev_runtime__WEBPACK_IMPORTED_MODULE_0__["jsxDEV"])("h2", {
        children: "Let's get started!"
      }, void 0, false, {
        fileName: _jsxFileName,
        lineNumber: 4,
        columnNumber: 7
      }, this)
    }, void 0, false, {
      fileName: _jsxFileName,
      lineNumber: 3,
      columnNumber: 5
    }, this);
  }
//You can import App into the root and run it
import ReactDOM from 'react-dom/client';

import './index.css';
import App from './App';

const root = ReactDOM.createRoot(document.getElementById('root')); //This is the new way to render in React 18
root.render(<App />); //THIS IS JSX

//components can be classes or functions //The naming convention is to capitalize the first letter of the component and use camel case i.e. ExpenseItem.j
console.log(4%5); //This will return 4
