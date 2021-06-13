
##############################################################################################################
#
#   Linear Search - VERSION 3
#
#
##############################################################################################################

def searching(list, size, number):
    i=0 #index 0

    while i < size and list[i] != number: #loop stops if checked the whole list or found the target number
        i = i+1 #check the next number

        if i == size: # if the search is done through all the elements and the number is not found
            return -1 #
    return i #else, the return the element found

list = [1,2,7,0,5,6,8,9,7]
number = 7
size = len(list)

# Calling the function and saving in the variable result
result = searching(list, size, number)

if result == -1:
    print("Number is not present in list")
else:
    print(f"Number number {number} is present at index", result)


# OUTPUT =>> Number number 7 is present at index 2