# Linear Search Program 

def LinearSearch (arr, k):

    for j in range (len(arr)):
        if (arr[j] == k):
            return j

    return -1

array = []

n = int (input ('\n How many values you want to insert in the Array? \n Your Answer: '))

for i in range (0, n):
    a = int (input (' Enter a Number (for Insertion in Array): '))
    array.append(a)
    a = 0

print (' After Insertion, the Array is:-\n Array: ', array)

print ('\n\n\t -------- Linear Search --------')

while True:
    print (' Do you want to Search any Number?')
    ch = input (' Your Answer ("Y" for Yes): ')

    if (ch == 'Y' or ch == 'y'):
        x = int (input (' Enter the number you want to search in the Array: '))
        result = LinearSearch (array, x)

        if (result == -1):
            print(' Number not found in the given array..\n')

        else:
            print(' Element found at Position: ', result+1, '\n')

    else:
        print('\n')
        break
