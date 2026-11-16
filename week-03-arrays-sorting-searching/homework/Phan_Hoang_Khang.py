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




