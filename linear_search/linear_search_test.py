import time


def linearSearch(searched_item, list):
    found = False
    i = 0

    while i < len(list) and not found:
            if list[i] == searched_item:
                found = True
            i = i + 1
    return found


# Run Time - Linear Search Test

def calculatingRuntime(linearSearch, myItem, myList):
    start = time.perf_counter() # Here the algorithm starts counting how many operations the pc is doing
    result = linearSearch(myItem, myList)  # calling the function and storing in a variable
    end = time.perf_counter() # the counting stops
    elapsed = (end - start) * 100000 # 100000 is how many tic my pc has to do
    return elapsed


list = [-125, -50, -1, 0, 1, 5, 7, 10, 12, 20, 26, 30, 50, 127, 500, 833, 900, 1000, 12345, 123456]
searched_number = int(input("What number do you want to find? "))
isitFound = linearSearch(searched_number, list)
timetoFind = calculatingRuntime(linearSearch, searched_number, list)

if (isitFound):
    print("Your item is in the list")
    print("Time to find the searched item: ", timetoFind)
else:
    print("Your item is not in the list")
    print("Time to find: ", timetoFind)

