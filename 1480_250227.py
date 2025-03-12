# 最富有客户的资产总量
class Solution(object):
    def runningSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        '''ans=[]
        sum=0
        for i in nums:
          sum+=i
          ans.append(sum)
        return ans
        '''
        a=0
        ans=[a:=i+a for i in nums]