<h1>Searching Algorithms </h1>

> This repository contains a personal study of the following search algorithms: Linear Search, Binary Search and Jump Search. 
 
## Files

# Linear Search 

The Linear Search algorithm consists of iterating over an array and returning the index of the first occurrence of an item once it is found. 
Here are different versions of the Linear Search algorithm.  

* [linear_search_v1.py](https://github.com/alicevillar/Searching_Algorithms/blob/main/linear_search/linear_search_v1.py) =>  This version uses a for loop. The target number is compared with each element of the array. If the target number is present then return its location. If the target element is present in the list more than once, the function will only return the first location.
 
* [linear_search_v2.py](https://github.com/alicevillar/Searching_Algorithms/blob/main/linear_search/linear_search_v2.py) => This version uses a for loop. In this second version,  the loop will keep repeating. Thus, even if the target element is present in the list more than once, the function will return all the locations.   

* [linear_search_v3.py](https://github.com/alicevillar/Searching_Algorithms/blob/main/linear_search/linear_search_v3.py) =>  This version uses a while loop. The algorithm compares the target number with each element of the array. If the target number is present then return its location. If the target element is present in the list more than once, the function will only return the first location.  

* [linear_search_test.py](https://github.com/alicevillar/Searching_Algorithms/blob/main/linear_search/linear_search_test.py) ==> This version uses the while loop from version 3. Here the Run Time is verified with Python time module.  

#### Observations

* The time complexity of linear search is O(n), meaning that the time taken to execute increases with the number of items in our input list.
* Linear search is not often used in practice, because it is not as fast or efficient as other search algorithms.
* Linear search is a good fit for when we need to find the first occurrence of an item in an unsorted collection because. Unlike most other search algorithms, it does not require that a collection be sorted before searching begins.


# Binary Search 

* [binary_search.py](https://github.com/alicevillar/Searching_Algorithms/blob/main/binary_search/binary_search.py) ==> Binary search with a while loop. 

#### Observations

* Binary search follows a divide and conquer methodology. It is faster than linear search but requires that the array be sorted before the algorithm is executed.
* Assuming that we're searching for a value X in a sorted array, the algorithm compares X to the value of the middle element of the array, which we'll call mid.
* If mid is the element we are looking for (best case), we return its index.
* If not, we identify whether X is smaller or greater than mid, and discard the other side of the array.
* Ifnhhhn follow the same steps, choosing a new value for mid, comparing it with val and discarding half of the possible matches in each iteration of the algorithm.



### Roadmap 

In the future, I intend to include the following algorithms in this repository:

* The Ubiquitous Binary Search
* Recursive program to linearly search an element in a given array
* Recursive function to do substring search 

### References

[GreeksforGreeks](https://www.geeksforgeeks.org/linear-search/)

[Search ALgorithms in Python](https://stackabuse.com/search-algorithms-in-python)

