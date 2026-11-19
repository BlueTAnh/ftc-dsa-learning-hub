# Problem 1: Weekly Court Pass
# Time: O(n)

def min_passes(visits):
    week_passes = 1
    days = {
        "Mon": 1,
        "Tue": 2,
        "Wed": 3,
        "Thu": 4,
        "Fri": 5,
        "Sat": 6,
        "Sun": 7
    }

    for i in range(1, len(visits)):
        if days[visits[i - 1]] >= days[visits[i]]:
            week_passes += 1
    return week_passes
print(min_passes(["Mon", "Wed", "Sun"]))
print(min_passes(["Fri", "Tue", "Thu"]))
print(min_passes(["Wed", "Wed"]))
print(min_passes(["Sat", "Sun", "Mon", "Sun", "Sat"]))

# Problem 2: Sort the People
# Time: O(n^2)

def sortPeople(self, names: list[str], heights: list[int]) -> list[str]:
    for i in range(len(heights)):
        min_index = i
        for j in range(i + 1, len(heights)):
            if heights[j] > heights[min_index]:
                min_index = j
        names[i], names[min_index] = names[min_index], names[i]
    return names

# Problem 3: Find Target Indices After Sorting Array
# Time: O(n^2)

def targetIndices(self, nums: list[int], target: int) -> list[int]:
    for i in range(1, len(nums)):
        temp_index = i
        temp_value = nums[i]
        for j in range(i - 1, -1, -1):
            if nums[j] > temp_value:
                nums[j + 1] = nums[j]
                temp_index = j
            else:
                break
        nums[temp_index] = temp_value

    indices = []    

    for n in range(len(nums)):
        if nums[n] == target:
            indices.append(n)
    return indices

# Problem 4: Search a 2D Matrix
# Time: O(log(m * n))

class Solution:
    def searchMatrix(self, matrix: list[list[int]], target: int) -> bool:
        m = len(matrix)
        n = len(matrix[0])

        left = 0
        right = m * n - 1

        while left <= right:
            mid = (left + right) // 2
            rows = mid // n
            column = mid % n

            
            if matrix[rows][column] == target:
                return True
            
            if matrix[rows][column] < target:
                left = mid + 1
            else:
                right = mid - 1
        
        return False


