def bubble_sort(nums):
    n = len(nums)
    for i in range(n-1):
        print(i)
        for j in range(n-1-i):
            if nums[j] > nums[j+1]:
                nums[j], nums[j+1] = nums[j+1], nums[j]
        print("Pass", i+1, ":", nums)

bubble_sort([5, 2, 4, 1, 3])