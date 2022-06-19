# First check if array can be split equally with n
# If Not, Return The Number
# Iterate through the array with n, 
# ex: If n=3, you add the 1st element[i=0] & 4th element[i=3]
# Keep adding elements to the array
class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:
        if(n*2!=len(nums)):
            return nums
        res=[]
        for i in range(n):
            res.append(nums[i])
            res.append(nums[i+n])
        
        return res