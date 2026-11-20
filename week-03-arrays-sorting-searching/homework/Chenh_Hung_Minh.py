# ==== Problem 1: Weekly Court Pass ====
# Time: O(N)
def min_passes(visits):
    days = {"Mon": 2, "Tue": 3, "Wed": 4, "Thu": 5, "Fri": 6, "Sat": 7, "Sun": 8}
    passes = 0
    last_day = 9
    for visit in visits:
        if last_day >= days[visit]:
            passes += 1
        last_day = days[visit]
    return passes

print(min_passes(["Mon", "Wed", "Sun"]))
print(min_passes(["Fri", "Tue", "Thu"]))
print(min_passes(["Wed", "Wed"]))
print(min_passes(["Sat", "Sun", "Mon", "Sun", "Sat"]))



# ==== Problem 2: Sort the People ====
# Time: O(n^2)
def sortPeople(names: list[str], heights: list[int]) -> list[str]:
    for i in range(1, len(names)):
        key_height = heights[i]
        key_name = names[i]
        j = i - 1
        while key_height > heights[j] and j >= 0:
            names[j+1] = names[j]
            heights[j+1] = heights[j]
            j -= 1
        heights[j+1] = key_height
        names[j+1] = key_name
    return names




# ==== Problem 3: Find Target Indices After Sorting Array ====
# Time: O(n)
def targetIndices(nums: list[int], target: int) -> list[int]:
    smallers, counter = 0, 0
    for num in nums:
        if num < target:
            smallers += 1
        elif num == target:
            counter += 1
    return [i+smallers for i in range(counter)]



# ==== Problem 4: Search a 2D Matrix ====
# Time: O(m.n)
def searchMatrix(matrix: list[list[int]], target: int) -> bool:
    n = len(matrix[0]) - 1
    left, right = 0, len(matrix) - 1
    while left <= right:
        mid = (left + right) // 2
        if matrix[mid][0] <= target and matrix[mid][n] >= target:
            l, r = 0, n
            while l <= r:
                m = (l + r) // 2
                if matrix[mid][m] == target:
                    return True
                elif matrix[mid][m] > target:
                    r = m - 1
                elif matrix[mid][m] < target:
                    l = m + 1
            return False
        elif matrix[mid][0] > target:
            right = mid - 1
        elif matrix[mid][n] < target:
            left = mid + 1
    return False