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
////////////////////////FIND DEPTH FIRST SEARCH NAMES ALL
// def depthFirstSearch(self, array):
// array.append(self.name)
// for node in self.children:
//     node.depthFirstSearch(array)
// return array
////////////////////////FIND DEPTH FIRST SEARCH NAMES ALL END
