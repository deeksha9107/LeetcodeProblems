# 702. Search in a Sorted Array of Unknown Size
# Medium
# You have a sorted array of unique elements and an unknown size. You do not have an access to the array but you can use 
# the ArrayReader interface to access it. You can call ArrayReader.get(i) that:
# returns the value at the ith index (0-indexed) of the secret array (i.e., secret[i]), or
# returns 231 - 1 if the i is out of the boundary of the array.
# You are also given an integer target.
# Return the index k of the hidden array where secret[k] == target or return -1 otherwise.
# You must write an algorithm with O(log n) runtime complexity.
# Input: secret = [-1,0,3,5,9,12], target = 9
# Output: 4
# Explanation: 9 exists in secret and its index is 4.

# """
# This is ArrayReader's API interface.
# You should not implement it, or speculate about its implementation
# """
#class ArrayReader:
#    def get(self, index: int) -> int:

class Solution:
    def search(self, reader: 'ArrayReader', target: int) -> int:
        low = 0
        high = 1
        while (reader.get(high) < target):
            low = high
            high = 2*high
        while (low <= high):
            mid = (low + high)//2
            if reader.get(mid) == target:
                return mid
            if target < reader.get(mid):
                high = mid - 1
            else:
                low = mid + 1
        return -1