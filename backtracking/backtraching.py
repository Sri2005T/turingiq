def combination(nums):
    res=[]
    curr=[]
    def backtrack(ind):
        if ind==len(nums):
            res.append(curr[:])
            return
        curr.append(nums[ind])
        backtrack(ind+1)
        curr.pop()
        backtrack(ind+1)
    backtrack(0)
    return res
print(combination([1,2,3]))