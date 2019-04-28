
#Linear Search


def LinearSearch(a,item):

    i = 0
    while i < len(a):
        if a[i]== item:
            return i
        i = i + 1
    return -1


# Binary search

def BinarySearch(a,item):

    lowerIndex = 0
    upperIndex = len(a)-1

    while lowerIndex <= upperIndex:

        midIndex = (lowerIndex+upperIndex)//2

        if a[midIndex] == item:
            return midIndex
        else:
            if a[midIndex] < item:
                lowerIndex = midIndex+1
            else:
                upperIndex = midIndex-1

    return -1
