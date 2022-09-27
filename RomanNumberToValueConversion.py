class Solution:
    def romanToInt(self, s: str) -> int:
        ans=0
        temp=0
        d={"I":1, "V":5, "X":10, "L":50, "C":100, "D": 500, "M":1000}
        for i in range(len(s)):
            if i+1<len(s) and d[s[i]] < d[s[i+1]]:
                    temp+=d[s[i]]
            else:
                ans+=(d[s[i]]-temp)
                temp=0
        return ans
