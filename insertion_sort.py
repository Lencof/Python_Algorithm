# __Author__ __Lencof__
# insertion_sort.py

def insertion_sort(nums):
    for i in range(1, len(nums)):
        item_to_insert = nums[i]
        j = i - 1
        while j >= 0 and nums[j] > item_to_insert:
            nums[j + 1] = nums[j]
            j -= 1

        nums[j + 1] = item_to_insert

random_list_of_nums = [9, 23, 12, 34, 234]
insertion_sort(random_list_of_nums)
print(random_list_of_nums) 

# [9, 12, 23, 34, 234]
