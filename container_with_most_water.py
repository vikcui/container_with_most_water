# author: YANG CUI
"""
Given n non-negative integers a1, a2, ..., an , where each represents a point at
coordinate (i, ai). n vertical lines are drawn such that the two endpoints of line i is
at (i, ai) and (i, 0). Find two lines, which together with x-axis forms a container,
such that the container contains the most water.

Note: You may not slant the container and n is at least 2.
"""

def container_with_most_water(inputArray):
    """
    :param inputArray: the array that contains all the heights at each index
    :return: the maximum area contained
    : time complexity: O(n)
    : space complexity: O(1)
    """
    # proof by contradition that the algo works
    # compute the length of the array
    arrayLen = len(inputArray)
    # left edge and right edge position
    leftPos = 0
    rightPos = arrayLen - 1
    # maximum area contained
    maxArea = (rightPos - leftPos) * min(inputArray[leftPos], inputArray[rightPos])
    # basic loop structure to step thru all possibilities to find the maximum area
    while leftPos != rightPos:
        currentArea = 0
        if inputArray[leftPos] <= inputArray[rightPos]:
            leftPos += 1
            currentArea = (rightPos - leftPos) * min(inputArray[leftPos], inputArray[rightPos])
            if currentArea > maxArea:
                maxArea = currentArea
        else:
            rightPos -= 1
            currentArea = (rightPos - leftPos) * min(inputArray[leftPos], inputArray[rightPos])
            if currentArea > maxArea:
                maxArea = currentArea
    return maxArea



print(container_with_most_water([1, 8, 6, 2, 5, 4, 8, 3, 7]))

