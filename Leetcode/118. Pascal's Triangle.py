class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        list2=[]
        for i in range(numRows):
            list1=[1]
            if i!=0: 
                prev = list2[-1]
                for j in range(len(prev) - 1):
                    list1.append(prev[j]+prev[j+1])
                list1.append(1)
            list2.append(list1)
        return list2
