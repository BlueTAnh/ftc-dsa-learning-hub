# Problem 2: Sort Array By Parity
# Time: O(n)
class Solution:
    def sortArrayByParity(self, nums: list[int]) -> list[int]:
        left = 0
        
        for right in range(len(nums)):
            if nums[right] % 2 == 0:
                nums[left], nums[right] = nums[right], nums[left]
                left+=1

        return nums

# Problem 4: Maximum Number of Vowels in a Substring of Given Length
# Time: O(n)
class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        vowels = 'aeiou'
        max_count = 0
        count = 0
        s_list = list(s)

        for i in range(k):
            if s_list[i] in vowels:
                count+=1

            max_count = max(max_count, count)

        for i in range(k, len(s_list)):
            if s_list[i] in vowels:
                count+=1

            if s_list[i - k] in vowels:
                count-=1

            max_count = max(max_count, count)

        return max_count
