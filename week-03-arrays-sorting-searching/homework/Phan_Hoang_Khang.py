# Problem 1: Weekly Court Pass
# Time: O(N)
def min_passes(visits):
    min_pass = 1
    day = {
        "Mon": 1,
        "Tue": 2,
        "Wed": 3,
        "Thu": 4,
        "Fri": 5,
        "Sat": 6,
        "Sun": 7
    }

    for i in range(1, len(visits)):
        if day[visits[i]] <= day[visits[i - 1]]:
            min_pass+=1

    return min_pass

visits = ["Sat", "Sun", "Mon", "Sun", "Sat"] 
print(min_passes(visits))

# Problem 2: Sort the People
# Time: O(N^2)
class Solution:
    def sortPeople(self, names: list[str], heights: list[int]) -> list[str]:
        n = len(heights)

        for i in range(n):
            for j in range(n - 1 - i):
                if heights[j] < heights[j + 1]:
                    heights[j], heights[j + 1] = heights[j + 1], heights[j]
                    names[j], names[j + 1] = names[j + 1], names[j]

        return names

# Problem 3: Find Target Indices After Sorting Array
# Time: O(N^2)
class Solution:
    def targetIndices(self, nums: list[int], target: int) -> list[int]:
        n = len(nums)
        arr = []

        for i in range(n):
            for j in range(n - 1 - i):
                if nums[j] > nums[j + 1]:
                    nums[j], nums[j + 1] = nums[j + 1], nums[j]

        for i in range(n):
            if nums[i] == target:
                arr.append(i)

        return arr

# Problem 4: Search a 2D Matrix
# Time: O(mlog(n))
# Where m is the length of row, and n is the length of column
class Solution:
    def searchMatrix(self, matrix: list[list[int]], target: int) -> bool:
        for row in matrix:
            low = 0
            high = len(row) - 1

            while low <= high:
                mid = (low + high) // 2

                if target < row[mid]:
                    high = mid - 1
                elif target > row[mid]:
                    low = mid + 1
                else:
                    return True

        return False