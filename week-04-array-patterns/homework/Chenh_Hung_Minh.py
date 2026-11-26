# Problem 1: Squares of a Sorted Array
# Time: O(n)
def sortedSquares(nums: list[int]) -> list[int]:
        res = []
        l, r = 0, len(nums)-1
        while l <= r:
            left_num = nums[l]**2
            right_num = nums[r]**2
            if left_num <= right_num:
                res.append(right_num)
                r -= 1
            else:
                res.append(left_num)
                l += 1
        return res[::-1]


# Problem 2: Sort Array By Parity
# Time: O(n)
def sortArrayByParity(nums: list[int]) -> list[int]:
        i = 0
        j = len(nums) - 1
        res = [0] * len(nums)
        for num in nums:
            if num % 2 == 0:
                res[i] = num
                i += 1
            else:
                res[j] = num
                j -= 1
        return res

# Problem 3: Find Pivot Index 
# Time: O(n)
def pivotIndex(nums: list[int]) -> int:
        len_nums = len(nums)
        prefix_sum = [0] * (len_nums+1)
        for bi in range(len_nums):
            prefix_sum[bi+1] = prefix_sum[bi] + nums[bi]
        
        for duy in range(len_nums):
            if prefix_sum[duy] == (prefix_sum[-1] - prefix_sum[duy+1]):
                return duy
        return -1

# Problem 4: Maximum Number of Vowels in a Substring of Given Length
# Time: O(n)
def maxVowels(s: str, k: int) -> int:
    vowels = {'a', 'e', 'i', 'o', 'u'}

    current = 0
    for i in range(k):
        if s[i] in vowels:
            current += 1

    maximum = current
    for i in range(k, len(s)):
        if s[i] in vowels:
            current += 1
        if s[i-k] in vowels:
            current -= 1
        maximum = max(current, maximum)
    
    return maximum