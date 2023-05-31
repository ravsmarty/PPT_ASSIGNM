"""


💡 **Q1.** Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

You can return the answer in any order.

**Example:**
Input: nums = [2,7,11,15], target = 9
Output0 [0,1]

**Explanation:** Because nums[0] + nums[1] == 9, we return [0, 1][



"""

             #SOLUTIONS

#ALGORITHM
"""
1.Initialize an empty dictionary (hash map) called complement_dict.
2.Iterate through the array nums using an index i and the corresponding value num.
3.Calculate the complement by subtracting num from the target value: complement = target - num.
4.Check if the complement exists in the complement_dict by using the in operator: if complement in complement_dict:.
5.If the complement exists, it means we have found the two numbers that add up to the target. In this case, we return the indices of the complement and the current number by accessing their values in the complement_dict: [complement_dict[complement], i].
6.If the complement doesn't exist in the complement_dict, we add the current number num as a key in the complement_dict, with its corresponding index i as the value: complement_dict[num] = i.
7.If no solution is found after iterating through the entire array, we return an empty list [].

"""

# TC:  O(N)
# SC = O(N)


#CODE

"""
def twoSum(nums, target):
    # Create a dictionary to store the complement of each number
    complement_dict = {}
    
    # Iterate through the array
    for i, num in enumerate(nums):
        # Calculate the complement for the current number
        complement = target - num
        
        # Check if the complement exists in the dictionary
        if complement in complement_dict:
            # Return the indices of the two numbers
            return [complement_dict[complement], i]
        
        # Add the current number and its index to the dictionary
        complement_dict[num] = i

    # If no solution is found, return an empty list
    return []

# Test the function
nums = [2, 7, 11, 15]
target = 9
print(twoSum(nums, target))  # Output: [0, 1]

"""


"""

💡 **Q2.** Given an integer array nums and an integer val, remove all occurrences of val in nums in-place. The order of the elements may be changed. Then return the number of elements in nums which are not equal to val.

Consider the number of elements in nums which are not equal to val be k, to get accepted, you need to do the following things:

- Change the array nums such that the first k elements of nums contain the elements which are not equal to val. The remaining elements of nums are not important as well as the size of nums.
- Return k.

**Example :**
Input: nums = [3,2,2,3], val = 3
Output: 2, nums = [2,2,_*,_*]

**Explanation:** Your function should return k = 2, with the first two elements of nums being 2. It does not matter what you leave beyond the returned k (hence they are underscores)[



"""


#SOLUTIONS

#CODE

"""
def removeElement(nums, val):
    i = 0  # Pointer for elements not equal to val

    for j in range(len(nums)):
        if nums[j] != val:
            nums[i] = nums[j]
            i += 1

    return i


nums = [3, 2, 2, 3]
val = 3
result = removeElement(nums, val)
print(result)  # Output: 2
print(nums)    # Output: [2, 2, _, _]

"""

#ALGORITHMS

"""
1.Initialize two pointers, i and j, both pointing to the start of the nums array.
2.Iterate through the nums array with the j pointer.
3.If nums[j] is equal to val, move the j pointer to the next element.
4.If nums[j] is not equal to val, set nums[i] to nums[j] and increment both i and j pointers.
5.Continue this process until the j pointer reaches the end of the array.
6.Return the value of i, which represents the number of elements in nums that are not equal to val.


"""

#TC=O(N)
#SC=O(1)



"""

💡 **Q3.** Given a sorted array of distinct integers and a target value, return the index if the target is found. If not, return the index where it would be if it were inserted in order.

You must write an algorithm with O(log n) runtime complexity.

**Example 1:**
Input: nums = [1,3,5,6], target = 5

Output: 2



"""

#CODE


"""
def searchInsert(nums, target):
    left, right = 0, len(nums) - 1

    while left <= right:
        mid = (left + right) // 2

        if nums[mid] == target:
            return mid
        elif nums[mid] < target:
            left = mid + 1
        else:
            right = mid - 1

    return left


nums = [1, 3, 5, 6]
target = 5
print(searchInsert(nums, target))

"""

#ALGORITHMS

"""
1.Initialize two pointers, left and right, pointing to the start and end of the array respectively.
2Iterate while left <= right:
a. Calculate the middle index as mid = (left + right) // 2.
b. If the middle element is equal to the target, return mid as the index.
c. If the middle element is less than the target, update left = mid + 1 to search in the right half.
d. If the middle element is greater than the target, update right = mid - 1 to search in the left half.
3.If the target is not found during the binary search, return the value of left as the index where it would be inserted.

"""

#TC=O(log(n))
#sc=O(1)


"""

💡 **Q4.** You are given a large integer represented as an integer array digits, where each digits[i] is the ith digit of the integer. The digits are ordered from most significant to least significant in left-to-right order. The large integer does not contain any leading 0's.

Increment the large integer by one and return the resulting array of digits.

**Example 1:**
Input: digits = [1,2,3]
Output: [1,2,4]

**Explanation:** The array represents the integer 123.

Incrementing by one gives 123 + 1 = 124.
Thus, the result should be [1,2,4].

"""

#SOLUTIONS

#ALGO

"""

1.To increment a large integer represented as an array of digits by one, you can follow the following steps:

2.Initialize a carry variable to 1. This variable represents the digit to be carried over to the next position during the addition process.

3.Iterate through the digits array starting from the rightmost digit (least significant digit) to the leftmost digit (most significant digit):

4.Add the carry to the current digit.
5.Calculate the sum and the new carry by dividing the digit by 10 (since we are adding 1) and taking the quotient and remainder, respectively.
6.Update the current digit with the remainder (the new digit after adding 1).
7.Update the carry with the quotient (the carry to be added to the next digit).
8.After the loop, check if the carry is greater than 0. If it is, it means there is a carry to be added to a new most significant digit. In this case, insert the carry at the beginning of the digits array.

Return the modified digits array.

"""

#CODE

"""
def incrementDigits(digits):
    carry = 1
    for i in range(len(digits) - 1, -1, -1):
        digit = digits[i]
        digit += carry
        carry = digit // 10
        digits[i] = digit % 10

    if carry > 0:
        digits.insert(0, carry)

    return digits


digits = [1, 2, 3]
result = incrementDigits(digits)
print(result)

"""

#TC:O(N)
#SC:O(1)


"""

💡 **Q5.** You are given two integer arrays nums1 and nums2, sorted in non-decreasing order, and two integers m and n, representing the number of elements in nums1 and nums2 respectively.

Merge nums1 and nums2 into a single array sorted in non-decreasing order.

The final sorted array should not be returned by the function, but instead be stored inside the array nums1. To accommodate this, nums1 has a length of m + n, where the first m elements denote the elements that should be merged, and the last n elements are set to 0 and should be ignored. nums2 has a length of n.

**Example 1:**
Input: nums1 = [1,2,3,0,0,0], m = 3, nums2 = [2,5,6], n = 3
Output: [1,2,2,3,5,6]

**Explanation:** The arrays we are merging are [1,2,3] and [2,5,6].
The result of the merge is [1,2,2,3,5,6] with the underlined elements coming from nums1.



"""

#ALGO

"""
1.Initialize three pointers:

p1 - pointing to the last non-zero element in nums1 (index m - 1).
p2 - pointing to the last element in nums2 (index n - 1).
p - pointing to the last element in the resulting merged array (index m + n - 1).
While both p1 and p2 are greater than or equal to 0, do the following:

2.If nums1[p1] is greater than nums2[p2], set nums1[p] to nums1[p1], and decrement p1 by 1.
3.Otherwise, set nums1[p] to nums2[p2], and decrement p2 by 1.
Decrement p by 1.
4.After the above loop, there might be remaining elements in nums2. Copy these remaining elements from nums2 to nums1.

"""

#CODE

"""
def merge(nums1, m, nums2, n):
    p1 = m - 1
    p2 = n - 1
    p = m + n - 1

    while p1 >= 0 and p2 >= 0:
        if nums1[p1] > nums2[p2]:
            nums1[p] = nums1[p1]
            p1 -= 1
        else:
            nums1[p] = nums2[p2]
            p2 -= 1
        p -= 1

    # Copy remaining elements from nums2 to nums1
    nums1[:p2 + 1] = nums2[:p2 + 1]

# Example usage
nums1 = [1, 2, 3, 0, 0, 0]
m = 3
nums2 = [2, 5, 6]
n = 3

merge(nums1, m, nums2, n)
print(nums1)


"""

#TC:O(m + n)
#SC:O(1) 


"""


💡 **Q6.** Given an integer array nums, return true if any value appears at least twice in the array, and return false if every element is distinct.

**Example 1:**
Input: nums = [1,2,3,1]

Output: true




"""

#ALGO

"""
1.Initialize an empty set or hash set called seen to keep track of the elements we have encountered so far.
2.Iterate through each element num in the input array nums.
3.Check if num is already present in the seen set.
4.If it is present, return True as we have found a duplicate element.
5.If it is not present, add num to the seen set.
6.If we finish iterating through the entire array without finding any duplicates, return False as all elements are distinct.

"""

#CODE

"""
def containsDuplicate(nums):
    seen = set()
    for num in nums:
        if num in seen:
            return True
        seen.add(num)
    return False

# Testing the example
nums = [1, 2, 3, 1]
print(containsDuplicate(nums))

"""

#TC: O(n)
#SC: O(n)


"""

💡 **Q7.** Given an integer array nums, move all 0's to the end of it while maintaining the relative order of the nonzero elements.

Note that you must do this in-place without making a copy of the array.

**Example 1:**
Input: nums = [0,1,0,3,12]
Output: [1,3,12,0,0]


"""

#ALGO

"""
1.Initialize two pointers, left and right, to 0.
2.Iterate through the array using the right pointer:
3.If the element at nums[right] is nonzero:
4.Swap nums[left] with nums[right].
5.Increment left by 1.
6.After the iteration, all nonzero elements will be moved to the left side of the array, and the left pointer will be pointing to the next position that should be filled with a nonzero element.
7.Iterate through the remaining positions from left to the end of the array and set their values to 0, effectively moving all the zeros to the end.
8.Return the modified array.

"""

#CODE


"""
def move_zeros(nums):
    # Initialize two pointers
    left = 0  # points to the current position to be filled with a nonzero element
    right = 0  # points to the current element being checked

    # Iterate through the array
    while right < len(nums):
        # If the current element is nonzero, swap it with the element at the left pointer
        if nums[right] != 0:
            nums[left], nums[right] = nums[right], nums[left]
            left += 1

        right += 1

    return nums


nums = [0, 1, 0, 3, 12]
result = move_zeros(nums)
print(result)

"""

#TC:O(N)
#SC:O(1)


"""

💡 **Q8.** You have a set of integers s, which originally contains all the numbers from 1 to n. Unfortunately, due to some error, one of the numbers in s got duplicated to another number in the set, which results in repetition of one number and loss of another number.

You are given an integer array nums representing the data status of this set after the error.

Find the number that occurs twice and the number that is missing and return them in the form of an array.

**Example 1:**
Input: nums = [1,2,2,4]
Output: [2,3]


"""

#SOLUTIONS

#ALGO

"""
1.Create an empty hash set called numSet.
2.Initialize two variables, duplicate and missing, both set to 0.
3.Iterate through each number, num, in the given array nums.
4.If num is already present in numSet, set duplicate to num.
Add num to numSet.
5.Iterate from 1 to the length of nums + 1 (inclusive) using the variable i.
If i is not found in numSet, set missing to i.
Return an array [duplicate, missing].

"""

#CODE

def findErrorNums(nums):
    numSet = set()
    duplicate = missing = 0

    for num in nums:
        if num in numSet:
            duplicate = num
        numSet.add(num)

    for i in range(1, len(nums) + 1):
        if i not in numSet:
            missing = i

    return [duplicate, missing]


#TC:O(N)
#SC:O(N)