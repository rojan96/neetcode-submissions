class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        return self.getDict(s) == self.getDict(t)

    def getDict(self, s: str) -> dict:
        charDict = {}
        for char in s:
            if char in charDict:
                charDict[char] = charDict[char]+1
            else:
                charDict[char] = 1
        return charDict