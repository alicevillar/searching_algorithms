

list = [1, 12, 15, 17, 20, 21, 22, 55, 66, 78, 90]
x = int(input("Enter the number to search: "))
low = 1
high = len(list)
isitfound = False


while isitfound == False:
    # Find the middle element in the sorted list.
    # How? Sum the number of the first position with the last position and do an integer division.
    mid = low + (high - low) // 2
    if list[mid] < x: # If the search element is smaller than middle element, repeat for the left sublist of the middle element.
        low = mid + 1
    elif list[mid] > x: # If the search element is larger than middle element, repeat for the right sublist of the middle element.
        high = mid - 1
    elif list[mid] == x: # Compare the search element with the middle element in the sorted list.
        print("Present in list in index", mid) # If mid is the element we are looking for, we return its index.
        isitfound = True
    else:
        print("Not in list")
        break