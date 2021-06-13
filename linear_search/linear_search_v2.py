
##############################################################################################################
#
#   Linear Search - VERSION 2
#   If the target element is present in the list more than once, this function will return the locations
#
##############################################################################################################


def search(list,target):
    for i in range(len(list)): # One by one compare the target number with each element of the array
        if list[i] == target: # check if the target number matches an element in the list
            print(i) # If the target number is present then return all the locations
    return -1


list = [1,2,7,4,5,6,7,8,9,7]
target = 7

search(list,target)

# OUTPUT =>>
# 2
# 6
# 9

