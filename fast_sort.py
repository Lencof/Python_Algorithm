# __Author__ __Lencof__
# fast_sort.py

def parition(nums, low, high):
    pivot = nums[(low + high) // 2]
    i = low - 1
    j = high + 1
    while True:
        i += 1
        while nums[i] < pivot:
            i += 1

        j -= 1
        while nums[j] > pivot:
            j -= 1

        if i >= j:
            return j

        nums[i], nums[j] = nums[j], nums[i]

def quick_sort(nums):
    def _quick_sort(items, low, high):
        if low < high:
            split_index = parition(items, low, high)
            _quick_sort(items, low, split_index)
            _quick_sort(items, split_index + 1, high)

    _quick_sort(nums, 0, len(nums) -1)

random_list_of_nums = [22, 4, 5, 7, 2, 93]
quick_sort(random_list_of_nums)
print(random_list_of_nums)

# [2, 4, 5, 7, 22, 93]