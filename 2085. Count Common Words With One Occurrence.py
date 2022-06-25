class Solution(object):
    def countWords(self, words1, words2):
        """
        :type words1: List[str]
        :type words2: List[str]
        :rtype: int
        """
        '''
        Solution 1 is using hashmaps. 
        Let's attack the question objectively. 
        We need to find the number of strings that has been present in both arrays exactly once
        We can use the dictionary get function here, 
        it returns the value of the key(w1), and 
        if no key is present, it return '0' as value by default
        then we use items to convert dic1 into a list and 
        check if the value of each key is 1, and if key(word) is present in dic2, and
        if value of key in dic2 is also 1, we increment the counter. 
        
        '''
        c=0
        dic1 = dict()
        dic2 = dict()
        for w1 in words1:
            dic1[w1] = dic1.get(w1,0) + 1
        for w2 in words2:
            dic2[w2] = dic2.get(w2,0) + 1
            
        print(dic1.items())
        #items turns dictionary in 2d lists with (key,value)
        
        for key,value in dic1.items():
            if value==1 and key in dic2 and dic2[key] == 1:
                c+=1
        return c
            
        