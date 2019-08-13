# Blog Notes: Insertion Sort
Speaking of slow and inefficient algoithms, insertion sort is much the same. This intuitive method of sorting often occurs when sorting a hand of cards in a card game.

Insertion sort is more efficient than bubble sort because it divides the list into a "sorted" and an "unsorted" section. It iterates over each element in a collection and orders the elements, usually in ascending order.

## Learning Objectives
What
Will
The
Students
Learn
Today

## Information Flow
Main Point
Supporting Points
Another main point
More details
Go here

## Diagram
Include your “Visual” here

## Algorithm
Describe in detail how the algorithm works. Include small code snippets to possibly support the points

## Pseudocode
InsertionSort(int[] arr)

    FOR i = 1 to arr.length

        int j <-- i - 1
        int temp <-- arr[i]
    
        WHILE j >= 0 AND temp < arr[j]
            arr[j + 1] <-- arr[j]
            j <-- j - 1
        
        arr[j + 1] <-- temp


## Readings and References
**Watch**
[Insert-sort with Romanian folk dance](https://www.youtube.com/watch?v=ROalU379l3U)

**Read**
[Geeks for Geeks: Insertion Sort](https://www.geeksforgeeks.org/insertion-sort/)
[BaseCS: Inching Towards Insertion Sort](https://medium.com/basecs/inching-towards-insertion-sort-9799274430da)

**Bookmark**
[Insertion Sort Wikipedia](https://en.wikipedia.org/wiki/Insertion_sort)
