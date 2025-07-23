from typing import List


def merge(left, right):
    result = []

    i = 0
    j = 0

    while i < len(left) and j < len(right):
        left_el = left[i]
        right_el = right[j]

        if left_el <= right_el:
            result.append(left_el)
            i += 1
        else:
            result.append(right_el)
            j += 1

    result.extend(left[i:])
    result.extend(right[j:])

    return result

def merge_sort(nums):
    if len(nums) <= 1:
        return nums

    center = len(nums) // 2

    left = nums[:center]
    right = nums[center:]

    sorted_left = merge_sort(left)
    sorted_right = merge_sort(right)

    return merge(sorted_left, sorted_right)

class Solution:

    def sortArray(self, nums: List[int]) -> List[int]:
        return merge_sort(nums)
