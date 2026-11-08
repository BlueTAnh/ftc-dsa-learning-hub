# Complexity: O(1)
def get_first(nums):
    return nums[0]

# Complexity: O(n)
def total(nums):
    result = 0
    for x in nums:
        result += x
    return result

# Complexity: O(n)
def sum_add_count(nums):
    total = 0
    for x in nums:
        total += x
    count = 0
    for x in nums:
        count += 1
    return total, count

# Complexity: O(n^2)
def print_pair(n):
    for i in range(n):
        for j in range(n):
            print(i, j)

# Complexity: O(n)
def print_with_labels(n):
    for i in range(n):
        for j in range(5):
            print(i,j)

# Complexity: O(log n)
def count_halvings(n):
    steps = 0
    while n > 1:
        n //= 2
        steps += 1
    return steps

# Complexity: O(n^2)
def print_unique_pairs(n):
    for i in range(n):
        for j in range(i, n):
            print(i, j)

# Complexity: O(n^2)
def build_reversed(n):
    result = []
    for i in range(n):
        result.insert(0, i)
    return result

# Complexity: O(n.m)
# a has n items, b has m items
def common_items(a, b):
    result = []
    for x in a:
        if x in b:
            result.append(x)
    return result

# Complexity: O(n+m)
def common_items_fast(a, b):
    b_set = set(b)
    result = []
    for x in a:
        if x in b_set:
            result.append(x)
    return result

# Complexity: O(n log n)
def print_sorted(nums):
    nums.sort()
    for x in nums:
        print(x)

# Question 12: O(log n) < O(n) < O(n logn) < O(n^2)
# Question 13: O(n logn) < O(n^2)
# Question 14: O(n^10) < O(2^n)
# Question 15: O((log n)^2) < O(√n)