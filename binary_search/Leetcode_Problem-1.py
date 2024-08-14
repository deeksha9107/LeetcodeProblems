# Leetcode Problem-1
# Binary Search
# 33. Search in Rotated Sorted Array
# https://leetcode.com/problems/search-in-rotated-sorted-array/description/
# Medium Problem

# There is an integer array nums sorted in ascending order (with distinct values).
# Prior to being passed to your function, nums is possibly rotated at an unknown pivot index k (1 <= k < nums.length) 
# such that the resulting array is [nums[k], nums[k+1], ..., nums[n-1], nums[0], nums[1], ..., nums[k-1]] (0-indexed). 
# For example, [0,1,2,4,5,6,7] might be rotated at pivot index 3 and become [4,5,6,7,0,1,2].
# Given the array nums after the possible rotation and an integer target, return the index of target if it is in nums, 
# or -1 if it is not in nums.
# You must write an algorithm with O(log n) runtime complexity.

# Step 1: Read Questions
    # Points Noted: 
        # It is sorted --> No repeats coz given distinct values
        # If not rotated --> return -1
        # No Negative numbers
        # Searching if target is present in an array

# Step 2: Verify Constraints

# Step 3: Write out Test Cases
    # Input: nums = [4,5,6,7,0,1,2], target = 0 Output: 4
    # Input: nums = [4,5,6,7,0,1,2], target = 3 Output: -1
    # Input: nums = [1], target = 0 Output: -1

# Step 4: Solution without code
    # Brute Force Approach: Since searching in a sorted array --> Linear Search --> O(n)
    # 
# Step 5: Write out solution in code
# Step 6: Double check for errors
# Step 7: Testing solution
# Step 8: Space & Time Complexity