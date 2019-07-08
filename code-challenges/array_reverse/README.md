# Reverse an Array
This program takes in an array and returns it in reverse order.

## Challenge
Write a function called reverse_array which takes an array as an argument. Without utilizing any of the built-in methods available to your language, return an array with elements in reversed order.

## Approach & Efficiency
In the first approach I used the slice constructor. I sliced the indices from the beginning to end with a step of -1, then printed the slice. 

In the second approach I first created an empty list. Then used the len() function to find the length and subtracted 1 to find the indices. I used a for loop to loop through each item in the array. For each item in the array, I appended the last index to the empty list. I also subtracted 1 from the index each time to access and append the next last item from the array. Finally, I printed the list. 


## Solution
![Whiteboard Solution](https://github.com/tammytdo/data-structures-and-algorithms/blob/master/assets/array_reverse.JPG)