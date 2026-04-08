class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        freqMap = {}

        for n in nums:
            freqMap[n] = freqMap.get(n,0) +1
        

        buckets = [[] for _ in range(len(nums)+1)]
        print(freqMap.items())
        for num,f in freqMap.items():
            
            buckets[f].append(num)
        print(buckets)
        

        res = []
        for f in range(len(buckets)-1,0,-1):
            for num in buckets[f]: # nothing to append if empty bucket
                res.append(num)
                if(len(res)) == k:
                    return res