
##############################################################################################################
#
#   Linear Search - VERSION 1
#   This function compare the target number with each element of the array
#   If the target number is present, then return its location
#
##############################################################################################################


# Driver Code
array = [2, 3, 4, 40, 70, 10, 84, 59, 10]
size = len(array)
target = 10

def searching(array, size, target): # 3 parameters: the array, size of the array, target number
    for i in range(size): # One by one compare the target number with each element of the array
        if (array[i] == target): # check if the target number matches an element in the list
            return i # If the target number is present then return its location
    return -1 # didn't found the number

# Calling the function and printing the result
result = searching(array, size, target)
if result == -1:
    print("Element is not present in array")
else:
    print("Element is present at index", result)


# OUTPUT =>> Element is present at index 5
