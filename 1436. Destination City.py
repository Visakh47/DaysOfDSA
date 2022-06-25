class Solution(object):
    def destCity(self, paths):
        """
        :type paths: List[List[str]]
        :rtype: str
        """
        '''
        paths[i] gives the different paths taken, i.e: edges
        paths[i][0] -> gives the src city
        paths[i][1] -> gives the destination city.
        '''
        src = []
        desn = []
        
        for path in paths:
            src.append(path[0])
            desn.append(path[1])

        
        curnode = desn[0]
        for i in range(1,len(paths)):
            if(curnode in src):
                curnode = desn[src.index(curnode)]
        
        return curnode