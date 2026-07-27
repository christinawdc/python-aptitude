class Solution:
    def romanToInt(self, s: str) -> int:
        n,i=0,0
        while i<len(s):
            if s[i]=="M":
                n+=1000
                i+=1
            elif s[i:i+2]=="CM":
                n+=900
                i+=2
            elif s[i]=="D":
                n+=500
                i+=1
            elif s[i:i+2]=="CD":
                n+=400
                i+=2
            elif s[i]=="C":
                n+=100
                i+=1
            elif s[i:i+2]=="XC":
                n+=90
                i+=2
            elif s[i]=="L":
                n+=50
                i+=1
            elif s[i:i+2]=="XL":
                n+=40
                i+=2
            elif s[i]=="X":
                n+=10
                i+=1
            elif s[i:i+2]=="IX":
                n+=9
                i+=2
            elif s[i]=="V":
                n+=5
                i+=1
            elif s[i:i+2]=="IV":
                n+=4
                i+=2
            elif s[i]=="I":
                n+=1
                i+=1
        return n
