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
function nonConstructibleChange(coins) {
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
    availableTime = [[dayStart, dayEnd]]
    for ele in calendar1:
        length = convert_time(ele[1]) - convert_time(ele[0])
        for index, time in enumerate(availableTime):
            if convert_time(ele[0]) in range(time[0],time[1]):
                availableTime[index] = adder(*split_time(ele[0],length,time))
            elif convert_time(ele[1]) in range(time[0],time[1]):
                availableTime[index] = adder(*split_time(ele[1],length,time))
    print(availableTime)
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
    const newLetters = [];
    const newKey = key % 26;
    for (const letter of string) {
      newLetters.push(getNewLetter(letter, newKey));
    }
    return newLetters.join('');
  }

  function caesarCipherEncryptor(string, key) {

    return string.split("").map((ele,index)=>{ return String.fromCharCode(((ele.charCodeAt(0) + key) - 97) % 26 + 97)}).join('')

  }
