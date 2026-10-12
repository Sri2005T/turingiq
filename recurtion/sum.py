def total(nums,ind):
    if ind==len(nums):
        return 0
    return nums[ind]+total(nums,ind+1)
print(total([1,2,3,4,5],0))