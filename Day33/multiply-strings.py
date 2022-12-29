class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        n1 = 0
        n2 = 0
        nums={'0':0,'1':1, '2':2, '3':3, '4':4, '5':5, '6':6, '7':7, '8':8, '9':9}
        for i in num1:
            n1 = 10 * n1 + nums[i]
        for i in num2:
            n2 = 10 * n2 + nums[i]

        result = n1*n2
        return str(result)
    # def multiply(self, num1: str, num2: str) -> str:
    #     n1 = len(num1)
    #     n2 = len(num2)

    #     toBeAdded = []
    #     # multiply
    #     for i in range(n1-1,-1,-1):
    #         res = "0" * (n1-i-1) 
    #         carry = ""
    #         for j in range(n2-1,-1,-1):
    #             num = str(int(num1[i]) * int(num2[j]))
    #             if carry != "":
    #                 num = str(int(num) + int(carry))
    #             if len(num) == 2:
    #                 carry = num[0]
    #                 num = num[1]
    #             else:
    #                 carry = ""
    #             res = num + res
    #         res = carry + res
    #         print(res)
    #         toBeAdded.append(res)
    #     # add
    #     toBeAdded.sort(key=len)

    #     a = len(toBeAdded[-1])

    #     carry = 0
    #     result = ""
    #     for i in range(a-1,-1,-1):
    #         res = carry
    #         for j in range(len(toBeAdded)):
    #             if len(toBeAdded[j]) > i:
    #                 res += int(toBeAdded[j][i])
    #         res = str(res)
    #         if len(res) > 1:
    #             carry = int(res[0])
    #             res = res[1]
    #         else:
    #             carry = 0
    #         result = res + result

    #     if carry:
    #         result = str(carry) + result
    #     return str(int(num1) * int(num2))






