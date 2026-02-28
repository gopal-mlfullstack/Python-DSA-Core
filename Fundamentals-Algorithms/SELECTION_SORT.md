# Selection Sort Algorithm 

## Problem Statement 
Given an array of integers, sort the array in ascending order.

## Approach 
Selection Sort finds the smallest element in the array, and swaps between smallest element with the current element. After each pass, the smallest element moves to its correct position. 

## Algorithm Steps 
1. Assume first element is the smallest.
2. Now using inner loop find the actual smallest element.[We know that after each pass smallest element will be its right position, so we do NOT compare from first element again, We compare from i + 1, because elements before i are already sorted.]
3. Swap the current element and smallest element each pass.

## Pseudocode 
for i in 0 to n - 1:
  small_index = i 
  for j in i + 1 to n - 1:
    if arr[j] < arr[small_index]:
      small_index = j
  
  swap(arr[i], arr[small_index])

## Example/Dry Run 
Input: [5, 3, 2] 

Pass 1:
* Initial minimum = 5
* Compare with 3 -> new minimum -> 3 
* Compare with 2 -> new minimum -> 2 
* swap 5 and 2 -> [2, 3, 5]

Pass 2:
* Initial minimum = 3
* Comapare with 5 -> new minimum -> No changes
Output: [2, 3, 5]


## Complexity Analysis 
- Time Complexity: O(n²)
- Space Complexity: O(1)
