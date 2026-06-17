class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        length=len(temperatures)
        answer=[0]*length
        stack=[]
        for i in range(length):
            while stack and (temperatures[i] > temperatures[stack[-1]]):
                x=stack.pop() #Temperature
                answer[x]=i-x #No. of days waited
            stack.append(i)
