class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        temp = 0
        for i in range(0,k):  
            temp = nums.pop()
            nums.insert(0,temp)
        
        return temp
        