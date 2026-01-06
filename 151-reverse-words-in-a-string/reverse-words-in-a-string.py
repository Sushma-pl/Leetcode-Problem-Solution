class Solution:
    def reverseWords(self, s: str) -> str:
        temp = ""
        w = ""
        for ch in s[::-1]:
            if ch==" ":
                if w!= "":
                    temp += (" " if len(temp)>0 else "") + w
                w=""
            else:
                w= ch + w

        if len(w)>0:
            temp += (" " if len(temp)>1 else "") + w

        # l = s.split(" ")
        # arr = []
        
        # for w in l:
        #     if w=="":
        #         continue
        #     arr.append(w)

        return temp
        