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
class Person {
    constructor() {
        this.name = 'Max'; //You can create properties in the constructor with this

    }

    printMyName() {
        console.log(this.name);
    }
}
