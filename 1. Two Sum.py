class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        '''
        Solution 1:
        initialize a new dictionary
        get the difference with the length and the number
        once you get difference, check if that difference value is present in the 
        dictionary, if not, map each of the number to the index value.
        
        ex: {2,7,11,15}
        target = 9
        for 2, diff = 7, dict = {}
        no 7 found in dict
        map 2 to position 0
        for 7, diff = 2, dict = {2:0}
        2 found in dic, mapped to 0, 
        return posn of 7, along with 0.
        
        '''
        
        
        dc = {}
        for i in range(0,len(nums)):
            diff = length - nums[i]
            if dc.get(diff) != None :
                return [i,dc[diff]]
            else:
                dc[nums[i]] = i
        
      
        