from random import randint

def random_list(count):
    numbers = []
    for i in range(count):
        numbers.append(randint(0, 10))
    return numbers

def merge(left, right):
    result = []
    i, j = 0, 0
    while i < len (left) and j < len (right):

        if left[i] <= right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1

    result += left[i:]
    result += right[j:]
    return result

def mergesort(stuff):

    if len(stuff) == 0 or len(stuff) == 1:
        return stuff

    else:

        mid = int(len(stuff) / 2)
        left = mergesort(stuff[:mid])
        right = mergesort(stuff[mid:])
        return merge(right, left)

stuff = random_list(10)

print ("Unsorted list: ", stuff)

print ("Sorted list: ", mergesort(stuff))
