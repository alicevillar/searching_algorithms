arr = [1, 12, 15, 17, 20, 21]
x = int(input("Enter value to search array: "))
low = 1
high = len(arr)
found = False
while found == False:
    mid = low + (high - low) // 2
    if arr[mid] < x:
        low = mid + 1
    elif arr[mid] > x:
        high = mid - 1
    elif arr[mid] == x:
        print("Present in list in index", mid)
        found = True
    else:
        print("Not in list")
        break