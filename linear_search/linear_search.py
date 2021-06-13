

# Python3 code to linearly search x in arr[].
# If x is present then return its location,
# otherwise return -1

#Start from the leftmost element of arr[] and one by one compare x with each element of arr[]
#If x matches with an element, return the index.
#If x doesn’t match with any of elements, return -1.


# Driver Code
array = [2, 3, 4, 10, 40]
size = len(array)
target = 10

def searching(array, size, target): # 3 parameters: the array, size of the array, target number
    for i in range(size):
        if (array[i] == target):
            return i # returns the index
    return -1 # didn't found the number

# Calling the function and printing the result
result = searching(array, size, target)
if result == -1:
    print("Element is not present in array")
else:
    print("Element is present at index", result)

    #Output = Element is present at index 3

    # ANOTHER VERSION


'''   
# ALTERNATIVE VERSION:
# aqui vai achar todas as ocorrencias, etnao usar para o caso de um n q repete na lista

def search(list,n):
    for i in range(len(list)):
        if list[i] == n:
            print(i)
    return -1
list = [1,2,3,4,5,6,7,8,9,0]
n = 7
search(list,n)
'''
