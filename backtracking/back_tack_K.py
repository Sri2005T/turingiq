def combination(nums,k):
    res=[]
    curr=[]
    def backtrack(ind,total):
        if total==k:
            res.append(curr[::])
            return
        if ind==len(nums) or total>k:
            return
        curr.append(nums[ind])
        backtrack(ind,total+nums[ind])
        curr.pop()
        backtrack(ind+1,total)
    backtrack(0,0)
    return res
print(combination([2,3,5],8))