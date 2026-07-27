class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        common=''
        for i in range(len(strs[0])):
            common+=strs[0][i]
            for word in strs:
                if not word.startswith(common):
                    common=common[:-1] #remove last letter
                    break
        return(common)
