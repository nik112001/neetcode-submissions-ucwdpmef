class Solution:
    def maxArea(self, heights: List[int]) -> int:
        left,right = 0, len(heights) -1
        maxA = min(heights)

        
        while left < right:
            area = (abs(left - right))*(min(heights[left],heights[right]))
            maxA = max(maxA,area)
            if heights[left] < heights[right]:
                left +=1
            else: 
                right -=1
        return maxA
            