class Solution:
    def maximumWealth(self, accounts: List[List[int]]) -> int:
        '''m=len(accounts)
        ans=[]
        for i in range(0,m):
          sum=0
          for j in accounts[i]:
            sum+=j
          ans.append(sum)
        max_value=max(ans)  
        
        return max_value'''
        a=0
        l=[sum(i) for i in accounts ]
        return(max(l))