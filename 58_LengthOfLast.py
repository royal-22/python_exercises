"""
Given a string s consisting of words and spaces, return the length of the last word in the string.

A word is a maximal substring consisting of non-space characters only.

source: https://leetcode.com/problems/length-of-last-word/ 
:)
"""


class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        ls = s.split()
        
        return len(ls[-1])
      
class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        
        s = s[::-1]
        i = 0
        j = 0
        
        while s[j] == " ":
            j += 1
        
        while not(j == len(s) or s[j] == " "):
            i += 1
            j += 1
        return i
