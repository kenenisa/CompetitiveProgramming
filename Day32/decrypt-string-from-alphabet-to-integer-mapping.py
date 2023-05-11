import string
class Solution:
    def freqAlphabets(self, s: str) -> str:
        first = {1:'a',2:'b',3:'c',4:'d',5:'e',6:'f',7:'g',8:'h',9:'i'}
        second = {10:'j',11:'k',12:'l',13:'m',14:'n',15:'o',16:'p',17:'q',18:'r',19:'s',20:'t',21:'u',22:'v',23:'w',24:'x',25:'y',26:'z'}
        s = s.split("#")
        new_string = ""
        n = len(s)
        for i in range(n - 1):
            new_string += s[i][:-2] + second[int(s[i][-2:])]
        new_string += s[-1]
        s = ''
        for i in new_string:
            if i not in string.ascii_lowercase:
                i = first[int(i)]
            s += i
        return s