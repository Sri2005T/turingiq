def permutations(nums):
    res=[]
    def backtrack(ind):
        if ind==len(nums):
            res.append(nums[::])

        for i in range(ind,len(nums)):
            nums[ind],nums[i]=nums[i],nums[ind]
            backtrack(ind+1)
            nums[ind],nums[i]=nums[i],nums[ind]
    backtrack(0)
    return res
print(permutations([1,2,3]))
