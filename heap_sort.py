# __Author__ __Lencof__
# heap_sort.py

def heapify(nums, heap_size, root_index):
    largets = root_index
    left_child = (2 * root_index) + 1
    right_child = (2 * root_index) + 2

    if left_child < heap_size and nums[left_child] > nums[largets]:
        largets = left_child
    
    if largets != root_index:
        nums[root_index], nums[largets] = nums[largets], nums[root_index]
        heapify(nums, heap_size, largets)

def heap_sort(nums):
    n = len(nums)
    for i in range(n, -1, -1):
        heapify(nums, n, i)

    for i in range(n -1, 0, -1):
        nums[i], nums[0] = nums[0], nums[i]
        heapify(nums, i, 0)

random_list_of_nums = [35, 12, 34, 56]
heap_sort(random_list_of_nums)
print(random_list_of_nums)

# [12, 34, 35, 56]
