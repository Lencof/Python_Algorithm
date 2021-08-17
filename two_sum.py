# __Author__ __Lencof__
# two_sum.py

def two_sum(nums, target):
    # check that the list is not empty
    if not nums:
        return None
    else:
        for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                if nums[i] + nums[j] == target:
                    return i,j

print(two_sum([1, 7, 8, 2, 5], 12))
# (1, 4)
