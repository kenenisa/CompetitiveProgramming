class Solution:
    def complexNumberMultiply(self, num1: str, num2: str) -> str:
        num1 = num1.split("+")
        realNum1 = int(num1[0])
        imgNum1 = int(num1[1][:-1])
        num2 = num2.split("+")
        realNum2 = int(num2[0])
        imgNum2 = int(num2[1][:-1])
        realAns = (realNum1 * realNum2) - (imgNum1 * imgNum2)
        imgAns = (realNum1 * imgNum2) + (imgNum1 * realNum2)
        return '{real}+{img}i'.format(real=realAns,img=imgAns)

        