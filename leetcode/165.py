# 165. Compare Version Numbers
# https://leetcode.com/problems/compare-version-numbers

class Solution(object):
    def compareVersion(self, version1, version2):

        a = int(version1)
        b = int(version2)
        if a > b:
            return 1
        elif a < b:
            return -1
        return 0

    def compareVersion1(self, version1, version2):

        if version1 > version2:
            return 1
        elif version1 < version2:
            return -1
        return 0


result = Solution()
print result.compareVersion1('1.0', '1.00')
