class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        longest = 0

        for i in range(len(s)):
            # expand right, keeping s[i] as the target char
            temp = k
            right = i + 1
            length = 1

            while right < len(s):
                if s[right] != s[i]:
                    if temp <= 0:
                        break
                    temp -= 1
                length += 1
                right += 1

            # also spend remaining replacements going left
            left = i - 1
            while left >= 0 and temp > 0:
                if s[left] != s[i]:
                    temp -= 1
                length += 1
                left -= 1

            longest = max(longest, length)

        return longest