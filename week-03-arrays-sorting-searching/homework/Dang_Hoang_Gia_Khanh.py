# Problem 1: Weekly Court Pass 
# Time: O(n)   Space: O(1)
def min_passes(visits: list[str]) -> int:
    day_num = {"Mon": 0, "Tue": 1, "Wed": 2, "Thu": 3, "Fri": 4, "Sat": 5, "Sun": 6}
    passes = 1  # the first visit always needs a pass
    prev = day_num[visits[0]]
    for i in range(1, len(visits)):
        cur = day_num[visits[i]]
        if cur <= prev:  # same day or earlier day -> next week
            passes += 1
        prev = cur
    return passes


# Problem 2: Sort the People (LC 2418) 
# Time: O(n^2)   Space: O(1) extra (sorts in place)
class Solution:
    def sortPeople(self, names: list[str], heights: list[int]) -> list[str]:
        n = len(heights)
        for i in range(n - 1):
            # find the tallest person in the unsorted part heights[i..n-1]
            max_idx = i
            for j in range(i + 1, n):
                if heights[j] > heights[max_idx]:
                    max_idx = j
            # swap BOTH arrays so names[k] still belongs to heights[k]
            heights[i], heights[max_idx] = heights[max_idx], heights[i]
            names[i], names[max_idx] = names[max_idx], names[i]
        return names


# Problem 3: Find Target Indices After Sorting Array (LC 2089) 
# Time: O(n^2)   Space: O(1) extra besides the answer
    def targetIndices(self, nums: list[int], target: int) -> list[int]:
        # insertion sort, ascending
        for i in range(1, len(nums)):
            key = nums[i]
            j = i - 1
            while j >= 0 and nums[j] > key:
                nums[j + 1] = nums[j]  # shift bigger values right
                j -= 1
            nums[j + 1] = key
        # scan the sorted array, copies sit next to each other
        result: list[int] = []
        for i in range(len(nums)):
            if nums[i] == target:
                result.append(i)
            elif nums[i] > target:
                break  # past the last copy, stop early
        return result

    # Optional challenge, O(n): no sort needed.
    # Sorted, every number smaller than target comes first, then all copies
    def target_indices_counting(self, nums: list[int], target: int) -> list[int]:
        smaller = sum(1 for x in nums if x < target)
        equal = sum(1 for x in nums if x == target)
        return list(range(smaller, smaller + equal))
