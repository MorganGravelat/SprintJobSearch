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


function compressBoxesTwice(boxes, boxes2) {
    boxes.forEach(function(boxes) {
        console.log(boxes);
    })

    boxes2.forEach(function(boxes) {
        console.log(boxes);
    })
}
//THIS IS O(a+b) the two boxes determine the complexity. I believe it would boil down to O(n)


const Bboxes = ['a','b','c','d','e'];
function logAllPairsOfArray(array) {
    for (let i = 0; i < array.length; i++) {
        for (let j = i+1; j < array.length; j++) {
            console.log(array[i], array[j]);
        }
    }
}
logAllPairsOfArray(Bboxes);
//THIS IS O(n^2)


//SPACE COMPLEXITY BELOW
function boooo(n) {
    for (let i = 0; i < n.length; i++) {
        console.log("BOOOOOOOO")
    }
}

boooo([1,2,3,4,5]); //TIME COMPLEXITY O(n) SPACE COMPLEXITY O(1)

function arrayOfHiNTimes(n) {
    let hiArray=[];
    for (let i = 0; i < n.length; i++) {
        hiArray[i] = 'hi';
    }
    return hiArray;
}

console.log(arrayOfHiNTimes(6));

'helwoshejhekhiuhudsh'.length; //O(1)

const larger = new Array(100000).fill('nemo');

function findNemo4(array) {
    for (let i = 0; i < array.length; i++) {
        if (array[i] === 'nemo') {
            console.log('Found NEMO!');
        }
    }
}

findNemo(everyone);

const findNemo5 = array => {
    array.forEach(i =>  {
        if(i === 'nemo') {
            console.log('Found NEMO!');
        }
    })
}



