## Problem 1:
class Solution:
    def sortedSquares(self, nums: list[int]) -> list[int]:
        left = 0
        right = len(nums) - 1
        result = []

        while left <= right:
            if abs(nums[left]) > abs(nums[right]):
                result.append(nums[left] ** 2)
                left += 1
            else:
                result.append(nums[right] ** 2)
                right -= 1

        result.reverse()        
        return result
## Problem 2:
    def sortArrayByParity(self, nums: list[int]) -> list[int]:
        write = 0
        for i in range(len(nums)):
            if nums[i] % 2 == 0:          
                nums[write], nums[i] = nums[i], nums[write]
                write += 1                   
        return nums
## Problem 3:
    def pivotIndex(self, nums: list[int]) -> int:
        total = sum(nums)                   
        left = 0
        for i in range(len(nums)):
            right = total - left - nums[i]  
            if left == right:
                return i                   
            left += nums[i]                
        return -1