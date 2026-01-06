class Solution:
    def reverseWords(self, s: str) -> str:
        l = s.split(" ")
        arr = []
        
        for w in l:
            if w=="":
                continue
            arr.append(w)

        return " ".join(arr[::-1])
        