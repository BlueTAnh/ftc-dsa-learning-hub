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




