# Binary Search Program

def BinarySearch (arr, k, beg, last):

    while beg <= last:
        mid = beg + (last - beg)//2
        if arr[mid] == k:
            return mid

        elif arr[mid] < k:
            beg = mid + 1

        else:
            last = mid - 1

    return -1

# For Binary Searching in the Array, the Array must be sorted
array = [12, 14, 15, 16, 20, 24, 26, 28, 30, 40]

print ('\n The Array is:-\n Array:', array)

print ('\n\n\t -------- Binary Search --------')

while True:
    print (' Do you want to Search any Number?')
    ch = input (' Your Answer ("Y" for Yes):')

    if (ch == 'Y' or ch == 'y'):
        x = int (input (' Enter the number you want to search in the Array: '))
        result = BinarySearch (array, x, 0, len(array)-1)

        if (result == -1):
            print(' Number not found in the given array..\n')

        else:
            print(' Element found at Position No.:', result+1, '\n')

    else:
        print('\n')
        break
