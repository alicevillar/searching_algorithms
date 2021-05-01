pos = -1
def binary_se(A,k):
    l = 0;
    h = len(A) - 1;
    while h >= l:
        mid = (h+l) // 2

        if A[mid] == k:
            globals()['pos'] = mid
            return 'k is found'
        else:
            if A[mid] < k:
                l = mid +1
            else:
                h = mid - 1

    return 'k is not found'

A = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]
k = 12

if binary_se(A,k):
    print('found', pos + 1)
else:
    print('not found') 