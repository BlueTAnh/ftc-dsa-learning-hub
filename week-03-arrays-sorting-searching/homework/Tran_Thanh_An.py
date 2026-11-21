# ===== PROBLEM 1: Weekly Court Pass =====
# Time: O(n)
def min_passes(visits):
    days = {
        "Mon": 1, 
        "Tue": 2, 
        "Wed": 3,
        "Thu": 4, 
        "Fri": 5, 
        "Sat": 6, 
        "Sun": 7
    }

    if len(visits) == 0:
        return 0

    passCount = 1
    for i in range(len(visits) - 1):
        if days[visits[i]] >= days[visits[i+1]]:
            passCount += 1

    return passCount

print(min_passes(["Mon", "Wed", "Sun"]))
print(min_passes(["Fri", "Tue", "Thu"]))
print(min_passes(["Wed", "Wed"]))
print(min_passes(["Sat", "Sun", "Mon", "Sun", "Sat"]))

# ===== PROBLEM 2: Sort the People (LC2418) =====
# Time: O(N^2)

class Solution:
    def sortPeople(self, names: list[str], heights: list[int]) -> list[str]:
        n = len(names)

        for i in range(n - 1):
            swapped = False

            for j in range(n - i - 1):
                if heights[j] < heights[j+1]:
                    swapped = True
                    names[j], names[j+1] = names[j+1], names[j]
                    heights[j], heights[j+1] = heights[j+1], heights[j]

            if swapped == False:
                break

        return names

# ===== PROBLEM 3: Find target indices after sorting array (LC2089) =====
# Time: O(N^2)

class Solution:
    def targetIndices(self, nums: list[int], target: int) -> list[int]:
        n = len(nums)

        for i in range(n - 1):
            max_idx = 0

            for j in range(1, n - i):
                if nums[j] > nums[max_idx]:
                    max_idx = j

            nums[n - i - 1], nums[max_idx] = nums[max_idx], nums[n - i - 1]

        indices = []
        for i in range(n):
            if nums[i] == target:
                indices.append(i)

        return indices

# ===== PROBLEM 4: Search a 2D Matrix =====
# Time: O(LOG(m*n))

class Solution:
    def searchMatrix(self, matrix: list[list[int]], target: int) -> bool:
        m = len(matrix)
        n = len(matrix[0])
        
        lo = 0
        hi = m * n - 1

        while lo <= hi:
            mid = (lo + hi) // 2

            row = mid // n
            col = mid % n

            if target < matrix[row][col]:
                hi = mid - 1
            elif target > matrix[row][col]:
                lo = mid + 1
            else:
                return True
        
        return False
