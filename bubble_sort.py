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

sort_numbers = [3, 5, 7, 8, 1]
sorted(sort_numbers)
print(sort_numbers)

# [1, 3, 5, 7, 8]
