class Solution:
    def findNumbers(self, nums: List[int]) -> int:
        c=0
        k=0
        for i in nums:
            num=i
            while(num>0):
                num=num//10
                c=c+1
            if(c%2==0):
                k=k+1
            c=0
        
        return k
    
    #Another Solution 1
        k=0
        for i in nums: 
            if(i>=10 and i<=99):
                k=k+1
            elif(i>=1000 and i<=9999):
                k=k+1
            elif(i>=100000 and i<=999999):
                k=k+1
        
        return k
    
    k=0
    #Another Solution 2
        for i in range(len(nums)):
            if(len(str(nums[i])) % 2 == 0):
                k=k+1
                
        return k
                
            