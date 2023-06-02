function threeNumberSum(arr, targetSum) {
    arr.sort((a,b) => a - b);
    const threes = [];
    for (let i = 0; i < arr.length - 2; i++) {
      let left = i + 1;
      let right = arr.length - 1;
      while (left < right) {
        const currentSum = arr[i] + arr[left] + arr[right];
        if (currentSum === targetSum ) {
          threes.push([arr[i], arr[left], arr[right]]);
          left++;
          right--;
        } else if (currentSum < targetSum) {
          left++;
        } else if (currentSum > targetSum) {
          right--;
        }
      }
    }
    return threes
}
//firstDuplicateValue problem Algo Expert
function firstDuplicateValue(array) {
    numbers_found = {} // I used a hash table to store the numbers I've seen
    for (let i = 0; i < array.length; i++) {
      ele = array[i] //
      if (!(ele in numbers_found)) {
        numbers_found[ele] = ele
      }
      else {
        return ele
      }
    }
    return -1;
  }
//NON CONTRUCTIBLE CHANGE PROBLEM
//If you do not know how to solve a problem, in array problems sort the input array and play around with the array
//You have an array like [5,7,1,1,2,3,22] and you want to find the smallest number that you cannot make
// YOu can sort the array into [1,1,2,3,5,7,22] and then you can see that the smallest number you cannot make is 20
// If the first value of the sorted list is not 1 then you can return 1
// YOu can go through and add the numbers 1 + 1 = 2, 2 + 2 = 4, 4 + 3 = 7, 7 + 5 = 12, 12 + 7 = 19, 19 + 22 = 41
// You can see that the smallest number you cannot make is 20 since all numbers added make 19
// We have a set of coins U = [1] all coins in the set
// We have a set of coins V = 1
// C = 1
// We can use math if V > C+1 then we can return C+1
// If V <= C+1 then we can add V to C and set V = C + V
// We can do this for all the coins in the array
//This would be O(n log n) time and O(1) space'
function nonconstructibleChange(coins) {
    let newCoins = coins.sort( function( a , b){
      if(a > b) return 1;
      if(a < b) return -1;
      return 0;
  });
    let currentChangeCreated = 0
    for (let i = 0; i < coins.length; i++) {
      coin = coins[i]
      if (coin > currentChangeCreated + 1) {
        return currentChangeCreated+1
      }
      currentChangeCreated += coin
    }
    return currentChangeCreated+1
  }



///////////////////Find closest value in BST
function findClosestValueInBst(tree, target) {
    let currentTree = tree;//We set the current tree to the tree
    let stillSearching = true;//We set a boolean to true
    let closest = Infinity;//We set the closest current number to infinity so that we can compare it to the current tree value
    if (!tree) return "No tree was given!"; //If there is no tree we return a string

    while (stillSearching) { //While we are still searching
      if (currentTree.value === target) return target; //If the current tree value is equal to the target we return the target
      if (Math.abs(target - closest) > Math.abs(target - currentTree.value)) { //If the absolute value of the target minus the closest is greater than the absolute value of the target minus the current tree value
         closest = currentTree.value; //We set the closest to the current tree value
      }
      if (currentTree.value > target) {
        if (!currentTree.left) {//If there is no left child
          stillSearching = false;//We set the boolean to false
          break;
        }
        currentTree = currentTree.left
      }
      else {
        if (!currentTree.right) {//If there is no right child
          stillSearching = false;//We set the boolean to false
          break;
        }
        currentTree = currentTree.right
      }
    }
    return closest
  }

  // This is the class of the input tree. Do not edit.
  class BST {//We create a class for the BST
    constructor(value) {//We create a constructor for the BST
      this.value = value;//We set the value of the BST to the value
      this.left = null;
      this.right = null;
    }
  }


  //Branch Sums

  //We take a binary tree and call a recursive call on every left and right node
    //We add the value of the current node to the sum
    //We check if the current node has a left and right child
    //If it does not we push the sum to the sums array
    //If it does we call the recursive function on the left and right child
    //We return the sums array
    //This is O(n) time and O(n) space
    function branchSums(root) {
        const sums = [];
        calculateBranchSums(root, 0, sums);
        return sums;
    }
    function calculateBranchSums(node, runningSum, sums) {
        if (!node) return;
        const newRunningSum = runningSum + node.value;
        if (!node.left && !node.right) {
            sums.push(newRunningSum);
            return;
        }
        calculateBranchSums(node.left, newRunningSum, sums);
        calculateBranchSums(node.right, newRunningSum, sums);
    }
// STEP BY STEP
//Minimum pies for every friend to get even amount of slices of pizza
function minPies(friends, slices) {
    let remain = slices
    let friend;
    while (remain > 0) {
        friend = remain
        remain = friends % remain
    }
    let result = ((friends / friend) * slices)/slices;
    console.log(result)
    return result
}

minPies(4, 2)
/////////////////////////CLASS PHOTOS!!!!
// def classPhotos(redShirtHeights, blueShirtHeights):
//     redShirtHeights.sort() #arr = sorted(redShirtHeights) for no mutation
//     blueShirtHeights.sort()
//     red_is_front = redShirtHeights[0] > blueShirtHeights[0]
//     for a, b in zip(redShirtHeights, blueShirtHeights):
//         if red_is_front:
//             if b >= a:
//                 return False
//         else:
//             if a >= b:
//                 return False
//     return True


//This is O(n log n) time and O(1) space
//q: What is the difference between a sorted array and a sorted list?
//a: A sorted array is a list that is sorted in place, a sorted list is a list that is sorted and returned
/////////////////////////REMOVE DUPLICATES IN LINKED LIST
// def removeDuplicatesFromLinkedList(linkedList):
//     currentNode = linkedList
//     while currentNode is not None:
//         nextNode = currentNode.next
//         while nextNode is not None and nextNode.value == currentNode.value:
//             nextNode = nextNode.next

//         currentNode.next = nextNode
//         currentNode = nextNode

//     return linkedList
/////////////////////////FIND NODE DEPTHS BELOW
// def nodeDepths(root):
//     stack = [[root]]
//     total = 0
//     depth = 0
//     tempArr = []
//     while len(stack[0]):
//         tempRoot = stack.pop(0)
//         tempArr = []
//         for node in tempRoot:
//             total+=depth
//             if node.left:
//                 print(total, node.value, depth, "total")
//                 tempArr.append(node.left)
//             if node.right:
//                 print(total, node.value, depth, "total")
//                 tempArr.append(node.right)
//         print(tempArr)
//         depth+=1
//         stack.append(tempArr)
//     return total
////////GENIUS COPILOT SOLUTION
// def nodeDepthsHelper(node, depth):
//     if node is None:
//         return 0
//     return depth + nodeDepthsHelper(node.left, depth + 1) + nodeDepthsHelper(node.right, depth + 1)

// def nodeDepths(root):
//     # Write your code here.
//     return nodeDepthsHelper(root, 0)
/////////////////////////FIND NODE DEPTHS ABOVE
//region FIND DEPTH FIRST SEARCH NAMES ALL
// class Node:
//     def __init__(self, name):
//         self.children = []
//         self.name = name

//     def addChild(self, name):
//         self.children.append(Node(name))
//         return self

//     def depthFirstSearch(self, array):
//         array.append(self.name)
//         for node in self.children:
//             node.depthFirstSearch(array)
//         return array

//endregion FIND DEPTH FIRST SEARCH NAMES ALL
/////MIN WAITING TIME  BEGIN!!!!
// def minimumWaitingTime(queries):
//     queries.sort()
//     return sum([sum(queries[0:i]) for i, j in enumerate(queries)])
// #i=0 []
// #i=1 [1] 1 [1]
// #i=2 [1,2] 3 [1,3]
// #i=3 [1,2,2] 5 [1,3,5]
// #i=4 [1,2,2,3] 8 [1,3,5,8]
// #i=5 [1,2,2,3,6] 14 #ENDS BEFORE THIS
/////MIN WAITING TIME  END!!!!

/////PRODUCT SUM BEGIN!!!!
// def productSum(array,depth=1):
//     sum = 0
//     for ele in array:
//         if type(ele) == type([]):
//             sum += productSum(ele, depth+1)
//         else:
//             sum += ele
//     return sum * depth

//HEAD HURTY
// def productSum(array, depth=1):
//     return sum([productSum(x, depth+1) if type(x) is list else x for x in array]) * depth
/////PRODUCT SUM END!!!!
//BINARY SEARCH
//BRYCE VERSION
def binarySearch(array, target):
    if len(array) < 1:
        print(midIndex)
        return False
    midIndex = len(array)//2
    currentNum = array[midIndex]#// rounds down when dividing
    print(midIndex,currentNum)
    if currentNum == target:
        return midIndex
    elif target < currentNum:
        print(array[:midIndex],"lessThan")
        return midIndex - binarySearch(array[:midIndex], target)
    else:
        print(array[midIndex:],"moreThan")
        return midIndex + binarySearch(array[midIndex:], target)
//MORGAN VERSIOn
def binarySearch(array, target):
    left = 0
    right = len(array) - 1
    while left <= right:
        middle = (left + right) // 2
        match = array[middle]
        if target == match:
            return middle
        elif target < match:
            right = middle - 1
        else:
            left = middle + 1
    return -1
//MORGAN VERSION ABOVE

//THREE HIGHEST NUMS BELOW
from math import inf
def findThreeLargestNumbers(array):
    threeNums = [-inf, -inf, -inf]
    for num in array:
        for index, i in enumerate(threeNums):
            if num > i:
                threeNums.insert(index, num)
                threeNums.pop()
                break
    return sorted(threeNums, reverse=False)
//THREE HIGHEST NUMS ABOVE

////BUBBLE SORT BELOW
def bubbleSort(array):
    sorted = False
    count = 0
    while not sorted:
        sorted = True
        for i in range(len(array) - 1 - count):
            if array[i] > array[i+1]:
                array[i], array[i+1] = array[i+1], array[i]
                sorted=False
        count += 1
    return array

//// Apartment Hunting BEGIN
from math import inf

def apartmentHunting(blocks, reqs):
    answer = inf
    blockDistancesDict = {
        i: {
        req: inf for req in reqs
        } for i in range(len(blocks))
    }

    for blockIndex, block in enumerate(blocks):
        for req in reqs:
            if block[req] is True:
                for key in blockDistancesDict:
                    blockDistancesDict[key][req] = min(blockDistancesDict[key][req], abs(blockIndex - key))
    print(blockDistancesDict,"ourDICT")
    var2 = [max(blockDistancesDict[block].values()) for block in blockDistancesDict]
    print(var2)
    print(var2.index(min(var2)))
    return var2.index(min(var2))
//// Apartment Hunting END
//// Calender Matching BEGIN CURRENTLY BROKEN
def calendarMatching(calendar1, dailyBounds1, calendar2, dailyBounds2, meetingDuration):
    dailyB1 = [convert_time(i) for i in dailyBounds1]
    dailyB2 = [convert_time(i) for i in dailyBounds2]
    dayStart = max(dailyB1[0],dailyB2[0])
    dayEnd = min(dailyB1[1],dailyB2[1])
    availabletime = [[dayStart, dayEnd]]
    for ele in calendar1:
        length = convert_time(ele[1]) - convert_time(ele[0])
        for index, time in enumerate(availabletime):
            if convert_time(ele[0]) in range(time[0],time[1]):
                availabletime[index] = adder(*split_time(ele[0],length,time))
            elif convert_time(ele[1]) in range(time[0],time[1]):
                availabletime[index] = adder(*split_time(ele[1],length,time))
    print(availabletime)
    return -1

def split_time(start_time, duration, time_range):
    lower_time = convert_time(time_range[0])
    upper_time = convert_time(time_range[1])
    lower_range = [lower_time, start_time]
    upper_range = [clock_add(start_time, duration), upper_time]

    return [lower_range, upper_range]


def clock_add(time, duration):
    time = convert_time(time)
    time += duration
    return convert_time(time)

def adder(*args):
    newList = []
    for i in args:
        newList.append(i)
    return newList

def convert_time(time):
    if type(time) is str:
        time = time.split(':')
        hrs = int(time[0]) * 60
        mins = int(time[1]) + hrs
        return mins
    else:
        hrs = int(time / 60)
        mins = int(time % 60)
        return f"{hrs:02d}:{mins:02d}"

//// Calender Matching END
//// Selection Sort BEGIN
function selectionSort(array) {
    let startIdx = 0;
    while (startIdx < array.length - 1) {
        let smallestIdx = startIdx;
        for (let i = startIdx + 1; i < array.length; i++) {
            if (array[smallestIdx] > array[i]) smallestIdx = i;
        }
        swap(startIdx, smallestIdx, array);
        startIdx++;
    }
    return array;
}

function swap(i, j, array) {
    const temp = array[j];
    array[j] = array[i];
    array[i] = temp;
}
//// Selection Sort END
/////////////MOVE ELEMENT TO END BEGIN
function moveElementToEnd(array, toMove) {
    let left = 0;
    let right = array.length - 1;
    while (left < right) {
        while (left < right && array[right] === toMove) right--;
        if (array[left] === toMove) swap(left, right, array);
        left++;
    }
    return array;
}

function swap(i, j, array) {
    const temp = array[j];
    array[j] = array[i];
    array[i] = temp;
}
/////////////MOVE ELEMENT TO END END
/////INSERTTION SORT BEGIN
function insertionSort(array) {
    for(let i = 1; i < array.length; i++) {
      let j = i;
      while(j > 0 && array[j] < array[j-1]) {
        [array[j],array[j-1]] = [array[j-1], array[j]]
        j -= 1;
      }
    }
    return array;
  }
/////INSERTTION SORT END
//////Semordnilap BEGIN

function semordnilap(words) {
    const wordsSet = new Set(words);
    const semordnilapPairs = [];

    for (const word of words) {
      const reverse = word.split('').reverse().join('');
      if (wordsSet.has(reverse) && reverse !== word) {
        semordnilapPairs.push([word, reverse]);
        wordsSet.delete(word);
        wordsSet.delete(reverse);
      }
    }

    return semordnilapPairs;
  }
///////Semordnilap END
///////Selection Sort BEGIN
function selectionSort(array) {
    let Index = 0;
    while (Index < array.length - 1) {
      let SmallIndex = Index;
      for (let i = Index+1; i < array.length; i++) {
        if (array[SmallIndex] > array[i]) SmallIndex = i;
      }
      [array[Index], array[SmallIndex]] = [array[SmallIndex], array[Index]]
      Index++;
      console.log(array)
    }
    return array
  }
///////Selection Sort END
//////////
function caesarCipherEncryptor(string, key) {
    const newletters = [];
    const newKey = key % 26;
    for (const letter of string) {
      newletters.push(getNewletter(letter, newKey));
    }
    return newletters.join('');
  }

  function caesarCipherEncryptor(string, key) {

    return string.split("").map((ele,index)=>{ return String.fromCharCode(((ele.charCodeAt(0) + key) - 97) % 26 + 97)}).join('')

  }
string = "AAAAAAAAAAAAABBCCCCDD"
function runLengthEncoding(string) {
    let output = ""
    let counter = 0;
    for (let i = 0; i < string.length; i++) {
      let ele = string[i];
      let ele2 = string[i+1];
      counter++
      if (counter === 9){
          output+= `${counter}${ele}`
          counter = 0;
      }
      if ((ele !== ele2 || ele2 === undefined) && counter > 0 ) {
        output += `${counter}${ele}`;
        counter = 0;
      }
      console.log("output,counter,ele1/2",output, counter, ele,ele2)

    }
   return output
 }
runLengthEncoding(string);

function moveElementToEnd(array, toMove) {
    let i = 0;
     let j = array.length - 1;
     while (i < j) {
       while (i < j && array[j] === toMove) j--;
       if (array[i] === toMove) swap(i, j, array);
       i++;
     }
     return array;
   }

   function swap(i, j, array) {
     const temp = array[j];
     array[j] = array[i]
     array[i] = temp;
   }

array = [-1, -5, 10]
function isMonotonic(array) {
    if (array.length <= 2) return true;

    let direction = null;
    for (let i = 0; i < array.length-1; i++) {
      console.log(array[i],array[i+1], direction, array[i+1] > array[i])
      if (direction === null && (array[i+1] < array[i] || array[i+1] > array[i])) {
        direction = array[i+1] > array[i]
      }
      if ((direction && (array[i+1] < array[i])) || (!direction && (array[i+1] > array[i]))) {
        return false;
      }
    }
    return true;
  }
console.log(isMonotonic(array));

let scores = [8, 4, 2, 1, 3, 6, 7, 9, 5]

function minRewards(scores) {
    const rewards = scores.map(_=>1); // [1,1,1,1,1,1,1,1,1]
    for (let i = 1; i < scores.length; i++) { // [1,1,1,1,1,1,1,1,1],
      let j = i - 1; // 0
      if (scores[i] > scores[j]) { // 4 > 8
        rewards[i] = rewards[j] + 1; // [1,2,1,1,1,1,1,1,1]
        console.log(rewards, i, j)
      } else {
        while (j >= 0 && scores[j] > scores[j+1]) { // 0 >= 0 && 8 > 4
          rewards[j] = Math.max(rewards[j], rewards[j+1] + 1); // [2,2,1,1,1,1,1,1,1]
          j--; // -1
        }
        console.log(rewards, i, j)
      }
    }
    return rewards.reduce((a,b) => a + b); // 15
  }


minRewards(scores)

function fourNumberSum(array, targetSum) { //array = [7, 6, 4, -1, 1, 2] targetSum = 16
    const allPairSums = {} //Hash Table Sum of all pairs
    const quadruplets = [] // Array of quadruplets

    for (let i = 1; i < array.length - 1; i++) {// i1 j2 / i2 j3 / i3 j4 / i4 j5
      console.log(i, "This is I")
      for (let j = i + 1; j < array.length; j++) {
        console.log(j, "This is J")
        const currentSum = array[i] + array[j]; // 10 / 3 / 0 / 3
        const difference = targetSum - currentSum; // 6 / 13 / 16 / 13
        console.log(currentSum, difference, 'Current Sum AND Difference')
        if (difference in allPairSums) { // if 6 / 13 / 16 / 13
          for (const pair of allPairSums[difference]) {
            console.log(pair, "This is Pair")
            quadruplets.push(pair.concat([array[i], array[j]])); //Pushing the pair if applicable
            console.log(quadruplets, "This is quadruplets array")
          }
        }
      }
      for (let k = 0; k < i; k++) {
        const currentSum = array[i] + array[k];
        console.log(currentSum, "Current sum K Loop")
        if (!(currentSum in allPairSums)) {
          allPairSums[currentSum] = [[array[k], array[i]]];
          console.log(allPairSums, "All pair sums K loop")
        } else {
          allPairSums[currentSum].push([array[k], array[i]]);
          console.log(allPairSums, "All pair sums ELSE K loop")

        }
      }
    }
    console.log(quadruplets, "End of loops RETURN statement")
    return quadruplets;
  }

//   Objective:
//     - given string
//     - given array of strings
//     - find all substrings of string that are contained in array
//     - return true if duplicates appear else false
//    - return array of true and false values based off of if the substring is contained in the array+


// Edge-Cases:
//     - Array is length 0 return false
// Strategy:
//     - check base case
//     - Initialize a Hash Table Memo var with value of {}
//     - Add nums to Hash table until all nums have been sorted through
//     - Return true if any nums already inside hash table
//     - O(n) Time O(n) space
function multiStringSearch(bigString, smallStrings) {
    smallStrArr = []
    for (let i = 0; i < smallStrings.length; i++) {
      let decision = false;
      decision = false;
      let word = smallStrings[i]
      console.log(word, decision)
      for (let j = 0; j < bigString.length; j++) {
          if (bigString[j] === word[0] && !decision && word.length > 1) {
            for (let h = 1; h < word.length; h++) {
              if (word[h] !== bigString[j+h]) {
                break;
              }
              else if (h === word.length - 1) {
                smallStrArr.push(true)
                decision = true;
              }
            }
          }
          else if (word.length === 1) {
            smallStrArr.push(true)
            decision = true;
          }
          if (j === bigString.length - 1) {
            smallStrArr.push(false);
          }
          if (decision) {
            break;
          }
      }
    }
    return smallStrArr
  }

  function minNumberOfJumps(array) {
    let n = array.length;
    let jumps = new Array(n).fill(Infinity);
    jumps[0] = 0

    for (let i = 1; i < n; i++) {
      for (let j = 0; j < i; j++) {
        if (j + array[j] >= i) {
          jumps[i] = Math.min(jumps[i], jumps[j] + 1)
        }
      }
    }

    return jumps[n-1]
  }


//   Objective:
//     - given string
//     - given array of strings
//     - find all substrings of string that are contained in array
//     - return true if duplicates appear else false
//    - return array of true and false values based off of if the substring is contained in the array+


// Edge-Cases:
//     - Array is length 0 return false
// Strategy:
//     - check base case
//     - Initialize a Hash Table Memo var with value of {}
//     - Add nums to Hash table until all nums have been sorted through
//     - Return true if any nums already inside hash table
//     - O(n) Time O(n) space

//Objective
//  -Give an array of numbers
//  - Find numbers in the array that are strictly increasing until they reach the tip(highest number) and then strictly decrease
//  - Return the length of the longest mountain
// Edge-cases
//  - If there is no mountain return 0
//  - If there is only one mountain return the length of the mountain
//  - If there are no numbers return 0
// Strategy
//  - Check base case
//  - Initialize a variable called longestMountain with a value of 0
//  - Initialize a variable called mountain with a value of 0
//  - Initialize a variable called mountainStart with a value of false
//  - Initialize a variable called mountainEnd with a value of false
//  - Loop through the array
//  - If the current number is less than the next number and mountainStart is false
//  - Set mountainStart to true
[1, 2, 3, 3, 4, 0, 10, 6, 5, -1, -3, 2, 3]

class UnionFind { // 0(n) time and space
  constructor(n) {
    this.parent = new Array(n).fill(0).map((e, i) => i); // 0(n) time and space
    this.rank = new Array(n).fill(0); // 0(n) time and space
  }

  find(x) { // 0(1) amortized time
    if (this.parent[x] !== x) {
      this.parent[x] = this.find(this.parent[x]);
    }
    return this.parent[x];
  }

  union(x, y) { // 0(1) amortized time and space
    let rootX = this.find(x);
    let rootY = this.find(y);

    if (rootX === rootY) return;

    if (this.rank[rootX] > this.rank[rootY]) {
      this.parent[rootY] = rootX;
    } else if (this.rank[rootX] < this.rank[rootY]) {
      this.parent[rootX] = rootY;
    } else {
      this.parent[rootY] = rootX;
      this.rank[rootX] += 1;
    }
  }
}

function validIPAddresses(string) {
    let validIPs = [];
    let ip = [];
    for (let i = 1; i < Math.min(string.length, 4); i++) {
        let currentIP = string.slice(0, i);
        if (isValid(currentIP)) {
        ip.push(currentIP);
        helper(string.slice(i), ip, validIPs);
        ip.pop();
        }
    }
    return validIPs;
}


function largestComponent(adjacencyList) {
	let found = new Set()
	let largeComponent = 0;
	For (let node in adjacencyList) {
		If (!found.has(node)) {
			const size = traverse(adjacencyList, found, node);
			If (size > largeComponent) {
				largeComponent = size
}
		}

}
return largeComponent
}




function traverse(adjacencyList, found, node) {
	found.add(node)
			let currentComponent = 1
			const neighbor = adjacencyList[node]
			For (let n in neighbor) {
				If (!found.has(n)) {
					currentComponent += traverse(adjencyList, found, n);
}
}
return currentComponent

}



// Longest Common Subsequence
// Objective:
//     - Given two strings, find the longest common subsequence
//     - A subsequence is a sequence that can be derived from another sequence by deleting some or no elements without changing the order of the remaining elements
//     - Return the length of the longest common subsequence
// Edge Cases:
//     - If one of the strings is empty return 0
//     - If the strings are the same return the length of the string
// Strategy:
//     - Check base case
//     - Initialize a variable called longest with a value of 0
//     - Initialize a variable called current with a value of 0
//     - Initialize a variable called currentStart with a value of 0
//     - Initialize a variable called currentEnd with a value of 0
//     - Loop through the first string
//     - Loop through the second string
//     - If the current letter in the first string is equal to the current letter in the second string
//     - Set currentStart to the current index of the first string
//     - Set currentEnd to the current index of the second string
//     - While the current letter in the first string is equal to the current letter in the second string
//     - Increment current
//     - Increment currentStart
//     - Increment currentEnd
//     - If current is greater than longest
//     - Set longest to current
//     - Set current to 0
//     - Set currentStart to 0
//     - Set currentEnd to 0
//     - Return longest

function longestCommonSubsequence(str1, str2) {
    const lcs = [];
    for (let i = 0; i < str1.length + 1; i++) {
        lcs.push(new Array(str2.length + 1).fill(0));
    }
    for (let i = 1; i < str1.length + 1; i++) {
        for (let j = 1; j < str2.length + 1; j++) {
            if (str1[i - 1] === str2[j - 1]) {
                lcs[i][j] = lcs[i - 1][j - 1] + 1;
            } else {
                lcs[i][j] = Math.max(lcs[i - 1][j], lcs[i][j - 1]);
            }
        }
    }
    return lcs[str1.length][str2.length];
}

//Leetcode problem
//Add two nuumbers
// # Definition for singly-linked list.
// # class ListNode(object):
// #     def __init__(self, val=0, next=None):
// #         self.val = val
// #         self.next = next
// class Solution(object):
//     def addTwoNumbers(self, l1, l2):
//         """
//         :type l1: ListNode
//         :type l2: ListNode
//         :rtype: ListNode
//         """
//         return self.helper(l1,l2,False)

//     def helper(self,l1, l2,hasCarry):

//         if l1 is None and l2 is None:
//             return ListNode(1,None) if hasCarry else None

//         if l1 is not None and l2 is not None:

//             digit = l1.val + l2.val + 1 if hasCarry else l1.val + l2.val

//             if digit >= 10:
//                 lastDigit = int(str(digit)[len(str(digit)) - 1])
//                 return ListNode(lastDigit, self.helper(l1.next, l2.next, True))
//             else:
//                 return ListNode(digit, self.helper(l1.next, l2.next, False))

//         elif l1 is not None and l2 is None:

//             digit = l1.val + 1 if hasCarry else l1.val

//             if digit >= 10:
//                 lastDigit = int(str(digit)[len(str(digit)) - 1])
//                 return ListNode(lastDigit, self.helper(l1.next, l2, True))
//             else:
//                 return ListNode(digit, self.helper(l1.next, l2, False))

//         elif l1 is None and l2 is not None:
//             digit = l2.val + 1 if hasCarry else l2.val

//             if digit >= 10:
//                 lastDigit = int(str(digit)[len(str(digit)) - 1])
//                 return ListNode(lastDigit, self.helper(l1, l2.next, True))
//             else:
//                 return ListNode(digit, self.helper(l1, l2.next, False))

//         return None


/*
function cycleInGraph (edges) {
const numberOfNodes =
edges.length;
}
const visited = new Array(numberOfNodes).fill(false);
const currentlyInStack = new Array(numberOfNodes).fill(false);
for (let node = 0; node < numberOfNodes; node++) {
}
if (visited [node]) continue;
const containsCycle = isNodeInCycle(node, edges, visited, currentlyInStack); if (containsCycle) return true;
return false;
function isNodeInCycle (node, edges, visited, currentlyInStack) {
visited[node] = true;
currentlyInStack [node ] = true;
const neighbors = edges [node]; for (const neighbor of neighbors) { if (!visited [neighbor]) {
const containsCycle
isNodeInCycle(neighbor, edges, visited, currentlyInStack);
if (containsCycle) return true;
} else if (currentlyInStack [neighbor]) { return true;
}
}
}
currentlyInStack[node] = false; return false;

Find the score of all prefixes of an Array
def findPrefixScore(self, nums: List[int]) -> List[int]:
        m=nums[0]
        nums[0]*=2
        for i in range(1,len(nums)):
            m = max(m, nums[i])
            nums[i] += nums[i-1] + m
        return nums








        //Powerset

        //Objective:
        // - Given an array of unique integers, return all possible subsets (the power set)
        // - The solution set must not contain duplicate subsets
        // - Return the solution in any order
        // - The solution set must not contain duplicate subsets
        // - Return the solution in any order

        //Strategy:
        // - Initialize a variable called result with a value of an empty array
        // - Initialize a variable called current with a value of an empty array
        // - Initialize a variable called start with a value of 0
        // - Initialize a variable called end with a value of the length of the array
        // - Invoke the helper function with the array, start, end, current, and result
        // - Return result


        function powerset(array) {
            if (idx === null) {
                idx = array.length - 1;
            }
            if (idx < 0) {
                return [[]];
            }
            const ele = array[idx];
            const subsets = powerset(array, idx - 1);
            const length = subsets.length;
            for (let i = 0; i < length; i++) {
                const currentSubset = subsets[i];
                subsets.push(currentSubset.concat(ele));
            }
            return subsets;
        }





        //Geenrate Parentheses
var generateParenthesis = function(n) {
    var ans = []

    const work = (str,leftScore,rightScore) => {
        if(
            rightScore > leftScore ||
            rightScore > n ||
            leftScore > n
          ){
            return
        }
        if(leftScore === n && rightScore === n){
            ans.push(str)
            return
        }

        work(str+"(",leftScore+1,rightScore)
        work(str+")",leftScore,rightScore+1)
    }
    work("",0,0)
    console.log(ans)
    return ans
};


*/
/*
void printLinkedListInReverse(struct ImmutableListNode* head) {
    if(head->getNext(head) != NULL)
        printLinkedListInReverse(head->getNext(head));

    head->printValue(head);
}



| Column Name   | Type    |
+---------------+---------+
| sale_date     | date    |
| fruit         | enum    |
| sold_num      | int     |
+---------------+---------+
(sale_date, fruit) is the primary key for this table.
This table contains the sales of "apples" and "oranges" sold each day.


Write an SQL query to report the difference between the number of apples and oranges sold each day.

Return the result table ordered by sale_date.

The query result format is in the following example.



Example 1:

Input:
Sales table:
+------------+------------+-------------+
| sale_date  | fruit      | sold_num    |
+------------+------------+-------------+
| 2020-05-01 | apples     | 10          |
| 2020-05-01 | oranges    | 8           |
| 2020-05-02 | apples     | 15          |
| 2020-05-02 | oranges    | 15          |
| 2020-05-03 | apples     | 20          |
| 2020-05-03 | oranges    | 0           |
| 2020-05-04 | apples     | 15          |
| 2020-05-04 | oranges    | 16          |
+------------+------------+-------------+
Output:
+------------+--------------+
| sale_date  | diff         |
+------------+--------------+
| 2020-05-01 | 2            |
| 2020-05-02 | 0            |
| 2020-05-03 | 20           |
| 2020-05-04 | -1           |
+------------+--------------+
Explanation:
Day 2020-05-01, 10 apples and 8 oranges were sold (Difference  10 - 8 = 2).
Day 2020-05-02, 15 apples and 15 oranges were sold (Difference 15 - 15 = 0).
Day 2020-05-03, 20 apples and 0 oranges were sold (Difference 20 - 0 = 20).
Day 2020-05-04, 15 apples and 16 oranges were sold (Difference 15 - 16 = -1).

# Write your MySQL query statement below

select sale_date, sum(case when fruit='apples' then sold_num else -sold_num end) as diff
from sales
group by sale_date
*/

Minimum Path Sum
Medium
10.7K
138
company
Google
company
Amazon
company
Bloomberg
Given a m x n grid filled with non-negative numbers, find a path from top left to bottom right, which minimizes the sum of all numbers along its path.

Note: You can only move either down or right at any point in time.



Example 1:


Input: grid = [[1,3,1],[1,5,1],[4,2,1]]
Output: 7
Explanation: Because the path 1 → 3 → 1 → 1 → 1 minimizes the sum.
Example 2:

Input: grid = [[1,2,3],[4,5,6]]
Output: 12


Constraints:

m == grid.length
n == grid[i].length
1 <= m, n <= 200
0 <= grid[i][j] <= 100

//Miniumum Path Sum in a grid ANSWER
var minPathSum = function(grid) {
    let row = grid.length;
    let col = grid[0].length;
    for(let i=0;i<row;i++) {
        for(let j=0;j<col;j++) {
            if(i == 0 && j== 0) {
                continue
            } else if( i== 0) {
                grid[i][j] += grid[i][j-1]
            } else if ( j== 0) {
                grid[i][j] += grid[i-1][j]
            } else {
                grid[i][j] += Math.min(grid[i-1][j],grid[i][j-1])
            }
        }
    }
    return grid[row-1][col-1]
};
/*
There are n gas stations along a circular route, where the amount of gas at the ith station is gas[i].

You have a car with an unlimited gas tank and it costs cost[i] of gas to travel from the ith station to its next (i + 1)th station. You begin the journey with an empty tank at one of the gas stations.

Given two integer arrays gas and cost, return the starting gas station's index if you can travel around the circuit once in the clockwise direction,
otherwise return -1. If there exists a solution, it is guaranteed to be unique
*/
var canCompleteCircuit = function(gas, cost) {
    let step = 0;
    let currentPos = 0;
    let currentGas = gas[currentPos];
    let numberOfTimeTried = 1;
    let output = 0;

    const getNextPos = (curr) => curr === gas.length - 1 ? 0 : ++curr;

    while(step <= gas.length) {
        if (numberOfTimeTried > gas.length) return -1;
        if (currentGas < cost[currentPos]) {
            currentPos = getNextPos(currentPos);
            numberOfTimeTried += step + 1;
            step = 0;
            currentGas = gas[currentPos];
            output = currentPos;
            continue;
        }
        currentGas -= cost[currentPos];
        currentPos = getNextPos(currentPos);
        currentGas += gas[currentPos];
        step++;
    }

    return output;
};


/*
Given an array of asyncronous functions functions and a pool limit n, return an asyncronous function promisePool. It should return a promise that resolves when all the input functions resolve.

Pool limit is defined as the maximum number promises that can be pending at once.
promisePool should begin execution of as many functions as possible and continue executing new functions when old promises resolve.
promisePool should execute functions[i] then functions[i + 1] then functions[i + 2], etc. When the last promise resolves, promisePool should also resolve.

For example, if n = 1, promisePool will execute one function at a time in series. However, if n = 2, it first executes two functions. When either of the two functions resolve,
a 3rd function should be executed (if available), and so on until there are no functions left to execute.

You can assume all functions never reject. It is acceptable for promisePool to return a promise that resolves any value.

Done in typescript

type F = () => Promise<any>

const promisePool = (fn: F[], n: number): Promise<any> => {
    let next = () => fn[n++]?.().then(next)
    return Promise.all(fn.slice(0, n).map(f => f().then(next)))
}

/**
 * @param {Function[]} functions
 * @param {number} n
 * @return {Function}
 */
var promisePool = async function(functions, n) {
    let next=()=>functions[n++]?.().then(next);
    return Promise.all(functions.slice(0,n).map(f=>f().then(next)));

};
DONE IN JAVASCRIPT alternative

function multiply(a, b) {
    // any zero
    if ([a, b].includes(`0`)) {
        return `0`
    }

    // get length of a, b
    const [lenA, lenB] = [a.length, b.length]

    // set nums for calculate
    let nums = Array(lenA + lenB).fill(0), index = nums.length - 1

    // reverse loop from a
    for (let i = lenA - 1; i >= 0; i--) {
        let key = index--

        // reverse loop from b
        for (let j = lenB - 1; j >= 0; j--) {
            const v = +a[i] * +b[j] + nums[key]

            // current
            nums[key] = v % 10
            // carry
            nums[--key] += Math.floor(v / 10)
        }
    }

    // remove `0` noneed
    return nums.join('').replace(/^0+/, '')
}
//Max Product
// Objective:
//     - Given an integer array nums, find a contiguous non-empty subarray within the array that has the largest product, and return the product.
// Time O(n)
// Space O(1)
var maxProduct = function(nums) {

    let result = nums[0]
    let currMax = nums[0]
    let currMin = nums[0]

    for (let i=1; i<nums.length; i++) {
        let localMax = Math.max(currMax * nums[i], nums[i], currMin * nums[i])
        let localMin = Math.min(currMax * nums[i], nums[i], currMin * nums[i])

        currMax = Math.max(localMax, localMin)
        currMin = Math.min(localMax, localMin)

        result = Math.max(result, currMax)


    }

    return result



};

/*
You are playing the Bulls and Cows game with your friend.

You write down a secret number and ask your friend to guess what the number is. When your friend makes a guess, you provide a hint with the following info:

The number of "bulls", which are digits in the guess that are in the correct position.
The number of "cows", which are digits in the guess that are in your secret number but are located in the wrong position. Specifically, the non-bull digits in the guess that could be rearranged such that they become bulls.
Given the secret number secret and your friend's guess guess, return the hint for your friend's guess.

The hint should be formatted as "xAyB", where x is the number of bulls and y is the number of cows. Note that both secret and guess may contain duplicate digits.
*/

//Solution
var getHint = function(secret, guess) {
    let bulls = 0, cows = 0;
    let secretMap = new Map(), guessMap = new Map();

    for (let i = 0; i < secret.length; i++) {
        if (secret[i] === guess[i]){
            bulls++;
        } else {
            secretMap.set(secret[i], (secretMap.get(secret[i]) || 0) + 1);
            guessMap.set(guess[i], (guessMap.get(guess[i]) || 0) + 1);
        }
    }

    for (let key of guessMap.keys()) {
        if (secretMap.has(key)) {
            cows += Math.min(secretMap.get(key), guessMap.get(key));
        }
    }

    return `${bulls}A${cows}B`;
};

var maxArea = function (height) {
    var leftIndex = 0;
    var rightIndex = height.length - 1;
    var maxStoredWater = 0;

    while (leftIndex < rightIndex) {
        const leftHeight = height[leftIndex];
        const rightHeight = height[rightIndex];
        const width = rightIndex - leftIndex;
        const smallerHeight = leftHeight < rightHeight ? leftHeight : rightHeight;
        const storedWater = width * smallerHeight;

        maxStoredWater = storedWater > maxStoredWater ? storedWater : maxStoredWater;
        smallerHeight == leftHeight ? leftIndex++ : rightIndex--;
    }

    return maxStoredWater;
};
// Remove Nth Node
var removeNthFromEnd = function(head, n) {
    let fast = head, slow = head
    for (let i = 0; i < n; i++) fast = fast.next
    if (!fast) return head.next
    while (fast.next) fast = fast.next, slow = slow.next
    slow.next = slow.next.next
    return head
}; //javascript solution
class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        fast, slow = head, head
        for _ in range(n): fast = fast.next
        if not fast: return head.next
        while fast.next: fast, slow = fast.next, slow.next
        slow.next = slow.next.next
        return head// python solution

/*
Suppose you are at a party with n people labeled from 0 to n - 1 and among them, there may exist one celebrity. The definition of a celebrity is that all the other n - 1 people know the celebrity, but the celebrity does not know any of them.

Now you want to find out who the celebrity is or verify that there is not one. You are only allowed to ask questions like: "Hi, A. Do you know B?" to get information about whether A knows B. You need to find out the celebrity (or verify there is not one) by asking as few questions as possible (in the asymptotic sense).

You are given a helper function bool knows(a, b) that tells you whether a knows b. Implement a function int findCelebrity(n). There will be exactly one celebrity if they are at the party.

Return the celebrity's label if there is a celebrity at the party. If there is no celebrity, return -1.
        */
       //Find the Celebrity
       /*
def findCelebrity(self, n): //Python Version
    x = 0
    for i in xrange(n):
        if knows(x, i):
            x = i
    if any(knows(x, i) for i in xrange(x)):
        return -1
    if any(not knows(i, x) for i in xrange(n)):
        return -1
    return x
       */

    // Javascript SOlution
    var solution = function(knows) {
        /**
         * @param {integer} n Total people
         * @return {integer} The celebrity
         */
        return function(n) {
            let c = 0;
            for (let i=1;i<n;i++) {
                if (knows(c,i)) {
                    c = i;
                }
            }

            for (let i=0;i<n;i++) {
                if (i!=c) {
                    if (!knows(i,c) || knows(c,i)) {
                        return -1;
                    }
                }
            }

            return c;

        };
    };
    //Subbaray Sort with python

def subarraySort(array):
    leftValue = -1
    rightValue = -1
    maxValue = array[0]
    for i in range(1, len(array)):
        if array[i] < maxValue:
            rightValue = i
            leftValue = i
        else:
            maxValue = array[i]
    minValue = array[len(array)-1]
    for i in reversed(range(0, len(array))):
        if array[i] > minValue:
            rightValue = i
        else:
            minValue = array[i]
    return [leftValue, rightValue]

    //Palindrome Pairs
    var palindromePairs = function(words) {

        for i, word in enumerate(words):

        if word in backward and backward[word] != i:
            res.append([i, backward[word]])

        if word != "" and "" in backward and word == word[::-1]:
            res.append([i, backward[""]])
            res.append([backward[""], i])

        for j in range(len(word)):
            if word[j:] in backward and word[:j] == word[j-1::-1]:
                res.append([backward[word[j:]], i])
            if word[:j] in backward and word[j:] == word[:j-1:-1]:
                res.append([i, backward[word[:j]]])

        return res
    };

//2348. Number of Zero-Filled Subarrays
/*
Given an integer array nums, return the number of subarrays filled with 0.

A subarray is a contiguous non-empty sequence of elements within an array.
*/
class Solution:
    def zeroFilledSubarray(self, nums: List[int]) -> int:
        res=0
        for x,g in groupby(nums):
            t=len(list(g))

            if x==0:
                res+=comb(t+1,2)
        return res

/*
105. Construct Binary Tree from Preorder and Inorder Traversal
Given two integer arrays preorder and inorder where preorder is the preorder traversal
of a binary tree and inorder is the inorder traversal of the same tree,
construct and return the binary tree.

Input: preorder = [3,9,20,15,7], inorder = [9,3,15,20,7]
Output: [3,9,20,null,null,15,7]


const buildTree = (preorder, inorder) => {
  if (!preorder.length || !inorder.length) return null;

  let root = new TreeNode(preorder[0]);
  let mid = inorder.indexOf(preorder[0]);
  root.left = buildTree(preorder.slice(1, mid + 1), inorder.slice(0, mid));
  root.right = buildTree(preorder.slice(mid + 1), inorder.slice(mid + 1));
  return root;
};
*/
