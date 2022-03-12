class Solution:
    def areAlmostEqual(self, s1: str, s2: str) -> bool:
        count = 0
        for i, n in zip(s1, s2):
            if i !=  n:
                count += 1

        return s1 == s2 or sorted(s1) == sorted(s2) and count == 2
