# uniqueBlocks.py
# Removes duplicate elements from a list, breaks it into blocks,
# bogosorts each one, merges them back into a large list,
# then adds the duplicates back in.
# A lot faster than vanilla bogosort on large lists. :P

from sys import argv
from random import randint, shuffle
import time

#------------------------------------------------------------------------------
#check for item in list
def checkList(x, unique):
    for y in unique:
        if x == y:
            return False
    return True

#------------------------------------------------------------------------------
#function for expanding a list
def expandList(sorted, value):
    exList = []
    for i in sorted:
        for f in range(value[i]):
            exList.append(i)
    return exList

#------------------------------------------------------------------------------
#reduces the list to unique numbers
def listOptimization(listOrigin):
    listUnique = list()
    highest = max(listOrigin)
    counts = [0 for x in range(highest + 1)]

    for x in listOrigin:
        counts[x] += 1
        if checkList(x, listUnique):
            listUnique.append(x)
    return listUnique, counts

#------------------------------------------------------------------------------
# Checks if a list is sorted
def isSorted(list):
    for i in range(1, len(list)):
        if(list[i - 1] > list[i]):
            return False
    return True

#------------------------------------------------------------------------------
# Breaks a list into blocks, bogosorts them, then merges them back together
def bogoBlock(array):
    blockSize = 5;  # Magic konstant
    blocks = list()
    outArray = list()
    scratchArray = list()
    blockIndex = 0;

    # Slice the list into blocks
    while blockIndex < len(array):
        blocks.append(list(array[blockIndex:blockIndex + blockSize]))
        blockIndex += blockSize

    # Bogosort each block
    for block in blocks:
        while not isSorted(block):
            shuffle(block)

    # Stack-merge the blocks into one big list again
    for block in blocks:
        if len(outArray) == 0:
            outArray = list(block)
            continue
        else:
            scratchArray = list(outArray)
            outArray = list()
        while len(scratchArray) > 0 or len(block) > 0:
            if len(scratchArray) == 0:
                outArray.extend(block)
                break
            elif len(block) == 0:
                outArray.extend(scratchArray)
                break
            elif scratchArray[0] <= block[0]:
                outArray.append(scratchArray.pop(0))
            elif block[0] < scratchArray[0]:
                outArray.append(block.pop(0))

    return outArray

#------------------------------------------------------------------------------
# Main function
def main():
    length = 10  # Default list length
    if (len(argv) >= 2):
        length = int(argv[1])
        print("Building a {}-element list.".format(length))
    else:
        print("No length specified. Building a 10-element list.")

    # Create random array using list comprehension
    if length >= 100:
        array = [randint(0, round(length*0.1)) for i in range(length)]
    else:
        array = [randint(0, 10) for i in range(length)]

    t0 = time.time()

    # print(array)
    uniqueArray, frequencies = listOptimization(array)
    uniqueSorted = bogoBlock(uniqueArray)
    array = expandList(uniqueSorted, frequencies)
    t1 = time.time()
    tt = t1 - t0
    print(array, tt)

main()
