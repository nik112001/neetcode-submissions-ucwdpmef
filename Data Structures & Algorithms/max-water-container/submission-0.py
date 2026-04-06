class Solution:
    def maxArea(self, heights: List[int]) -> int:
        maxP = 0
        left,right = 0, len(heights)-1
        

        while left < right:
            area = (right-left)*(min(heights[right],heights[left]))
            maxP = max(maxP,area)
            if heights[right] < heights[left]:
                right -= 1
            else:
                left +=1
        return maxP
            
