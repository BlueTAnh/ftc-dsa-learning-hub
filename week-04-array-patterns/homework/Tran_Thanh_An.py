# ===== PROBLEM 1: Squares of a Sorted Array (LC977) =====
# Time: O(n)

class Solution:
    def sortedSquares(self, nums: list[int]) -> list[int]:
        n = len(nums)
        for i in range(n):
            nums[i] = nums[i] ** 2

        sortedNums = [0] * n

        left = 0
        right = n - 1
        idx = n - 1

        while idx >= 0:
            if nums[left] <= nums[right]:
                sortedNums[idx] = nums[right]
                right -= 1
            else:
                sortedNums[idx] = nums[left]
                left += 1
            idx -= 1

        return sortedNums

# ===== PROBLEM 2: Sort Array By Parity (LC905) =====
# Time: O(n)

class Solution:
    def sortArrayByParity(self, nums: list[int]) -> list[int]:
        n = len(nums)

        sortedNums = [0] * n

        left = 0
        right = n - 1

        for i in range(n):
            if nums[i] % 2 == 0:
                sortedNums[left] = nums[i]
                left += 1
            else:
                sortedNums[right] = nums[i]
                right -= 1
        
        return sortedNums

# ===== PROBLEM 3: Find Pivot Index (LC704) =====
# Time: O(n)

class Solution:
    def pivotIndex(self, nums: list[int]) -> int:
        n = len(nums)

        leftSum = 0
        rightSum = sum(nums[1:])

        for i in range(1, n):
            if leftSum == rightSum:
                return i - 1
            leftSum += nums[i-1]
            rightSum -= nums[i]
        
        if leftSum == rightSum:
            return n - 1

        return -1

# ===== PROBLEM 4: Maximum Number of Vowels in a Substring of Given Length (LC1456) =====
# Time: O(n)

class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        n = len(s)

        vowels = "aeiou"
        count = 0

        for i in range(k):
            if s[i] in vowels:
                count += 1

        maxCount = count

        for i in range(k, n):
            if s[i] in vowels:
                count += 1
            if s[i-k] in vowels:
                count -= 1

            maxCount = max(maxCount, count)
            if maxCount == k:
                return maxCount
        
        return maxCount
