class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
      stack=[]
      for i in asteroids:
        while i<0 and stack and stack[-1]>0:
          top=stack.pop()
          if top>-i:
            i=top
          elif top<-i:
            continue
          else:
            i=0
        if i!=0:
          stack.append(i)
      return stack    
      