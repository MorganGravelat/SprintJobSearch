// //Below is javascript code Beginning of BIG O refresher practice
const nemo = ['nemo'];

function findNemo(array) {
    for (let i = 0; i < array.length; i++) {
        if (array[i] === 'nemo') {
            console.log('Found NEMO!');
        }
    }
}

// findNemo(nemo);
// // end of this script
// // Below I am going to alter this script with testers for big O testing
const nemo2 = ['nemo'];
function findNemo2(array) {
    let t0 = performance.now();
    for (let i = 0; i < array.length; i++) {
        if (array[i] === 'nemo') {
            console.log('Found NEMO!');
        }
    }
    let t1 = performance.now();
    console.log('Call to find Nemo took ' + (t1-t0) + ' milliseconds');
}
findNemo2(nemo2);


const large = new Array(100000).fill('nem')
large.push('nemo')
findNemo2(large);

//BETTER BIG O TESTING

const nemo3 = ['nemo'];

function findNemo3(array) {
    let t0 = performance.now();
    for (let i = 0; i < array.length; i++) {
        if (array[i] === 'nemo') {
            console.log('Found NEMO!');
        }
    }
    let t1 = performance.now();
    console.log('Call to find Nemo took ' + (t1-t0) + ' milliseconds');
}


// O(n) above O(1) below

function compressFirstBox(boxes) {
	console.log(boxes[0]);
}

const boxes = [0,1,2,3,4,5]

function logFirstTwoBoxes(boxes) {
    console.log(boxes[0]);
    console.log(boxes[1]);
}

logFirstTwoBoxes(boxes); //O(2);


//FIXING FIND NEMO FUNCTION

const nemo4 = ['nemo'];

function findNemo4(array) {
    for (let i = 0; i < array.length; i++) {
        if (array[i] === 'nemo') {
            console.log('Found NEMO!');
            break;
        }
    }
}

findNemo4(nemo4);
