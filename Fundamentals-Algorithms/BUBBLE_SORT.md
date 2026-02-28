# Bubble Sort Algorithm 

## Problem Statement:
Given an array of integers, sort the array in ascending order. 

## Approach 
Bubble Sort repeatedly compares adjacent elements and swaps them
if they are in wrong order. After each pass, the largest element moves to the end of the array. 

## Algorithm Steps
1. Start from the first element of the array. 
2. Compare the current element with the next element. 
3. swap them if the current element is greater. 
4. Repeat for all elements. 
5. Continue passes until the array is sorted. 


## Pseudocode 
for i from 0  to n-1:
    for j from 0 to n - i - 2:
        if arr[j] > arr[j+1]:
            swap(arr[j], arr[j + 1]) 

## Example 
Input: [5, 3, 2] 

Pass 1: 
- Compare 5 and 3 -> swap -> [3, 5, 2] 
- Compare 3 and 2 -> swap -> [3, 2, 5] 

Pass 2:

- compare 3 and 2 -> swap -> [2, 3, 5]

Output: [2, 3, 5]

## Complexity Analysis 
- Time Complexity: O(n**2) 
- Space Complexity: O(1)

## Key Points
- Simple and easy to understand
- Not efficient for large datasets 
- Stable sorting algorithm
