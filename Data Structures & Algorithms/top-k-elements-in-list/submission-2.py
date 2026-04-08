class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        order = {}
        res = []
        maxL =  0
        for n in (nums):
            if n not in order:
                order[n] = 1
            else:
                order[n] += 1
       
        while k > 0:
            maxL = max(order, key = order.get)
            res.append(maxL)
            order.pop(maxL)
            k -=1
        

        return res