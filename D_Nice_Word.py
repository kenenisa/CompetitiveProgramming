# from collections import deque
# import string
# def run():
#     a = [x for x in input()]
#     b = [0] * 26
#     n = len(a)
#     if n < 26:
#         return -1
#     for i in range(n-25):
#         invalid = False
#         b = [0] * 26
#         for j in range(i,i+26):
#             letter_index = ord(a[j])-ord('A')
#             if a[j] != "?":
#                 b[letter_index] += 1
#             if b[letter_index]>=2:
#                 invalid = True
#                 break
#         if invalid:  
#             continue
#         for j in range(i,i+26):
#             if a[j]=='?':
#                 for k in range(26):
#                     if b[k]==0:
#                         b[k]=1
#                         a[j]=chr(k+ord('A'))
#                         break      
#         new_arr = []
#         for i in range(n):
#             if a[i] == '?':
#                 new_arr.append("A")
#             else:
#                 new_arr.append(a[i])
#         return "".join(new_arr)
#     else:
#         return -1
# print(run())

from collections import deque
import string
s = input()
n = len(s)
def run():
    if n < 26:
        return -1
    alpha = set(string.ascii_uppercase)
    segment = deque()
    for i in range(n):
        while s[i] in segment and s[i] != "?":
            segment.popleft()
        segment.append(s[i])
        if len(segment) == 26:
            unique_substring = set(segment)
            count = len(unique_substring)
            if "?" in unique_substring:
                count -= 1
                
            diff = alpha.difference(unique_substring)

            if len(diff) == 26 - count:
                new_str = []
                while segment:
                    l = segment.popleft()
                    if l == "?":
                        l = diff.pop()
                    new_str.append(l)
                replaced_s = s.replace("?","A")
                return replaced_s[:i-25] + "".join(new_str) + replaced_s[i+1:]
    return -1
    
print(run())