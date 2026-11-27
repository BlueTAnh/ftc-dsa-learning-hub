# Problem 1: Squares of a Sorted Array
# Time: O(n)

class Solution:
    def sortedSquares(self, nums: list[int]) -> list[int]:
        n = len(nums)
        result = [0] * n
        left = 0
        right = n - 1
        pos = n - 1
        while left <= right:
            left_sq = nums[left] ** 2
            right_sq = nums[right] ** 2

            if left_sq > right_sq:
                result[pos] = left_sq
                left += 1
            else:
                result[pos] = right_sq
                right -= 1
            pos -= 1

        return result

# Problem 2: Sort Array By Parity
# Time: O(n)

class Solution:
    def sortArrayByParity(self, nums: list[int]) -> list[int]:
        left = 0
        right = len(nums) - 1

        while left < right:
            if nums[left] % 2 != 0:
                nums[left], nums[right] = nums[right], nums[left]
                right -= 1
            else:
                left += 1
        return nums

# Problem 3: Find Pivot Index 
# Time: O(n)

class Solution:
    def pivotIndex(self, nums: list[int]) -> int:
        total = sum(nums)
        left_total = 0

        for i in range(len(nums)):
            right_total = total - left_total - nums[i]

            if left_total == right_total:
                return i

            left_total += nums[i]

        
        return -1

# Problem 4: Maximum Number of Vowels in a Substring of Given Length
# Time: O(n)

class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        vowel = "aeiou"
        count = 0

        for i in range(k):
            if s[i] in vowel:
                count += 1

        real_count = count

        for j in range(k, len(s)):
            if s[j - k] in vowel:
                count -= 1
            
            if s[j] in vowel:
                count += 1

            real_count = max(real_count, count)
        return real_count