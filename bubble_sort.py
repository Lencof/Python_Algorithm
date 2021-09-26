# __Author__ __Lencof__
# bubble_sort.py

def sorted(nums):
    swapped = True
    while swapped:
        swapped = False
        for i in range(len(nums) - 1):
            if nums[i] > nums[i + 1]:
               nums[i], nums[i + 1] = nums[i + 1], nums[i]
               swapped = True

sort_numbers = [9, 8, 7, 6, 5, 4, 3, 2, 1]
sorted(sort_numbers)
print(sort_numbers)

# [1, 2, 3, 4, 5, 6, 7, 8, 9]
