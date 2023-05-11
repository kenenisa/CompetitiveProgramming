# 38ms 73.55% runtime - 68.79% memory
class Solution:
    def numberToWords(self, num: int) -> str:
        if num == 0:
            return 'Zero'
        df = {
        1: "One",
        2: "Two",
        3: "Three",
        4: "Four",
        5: "Five",
        6: "Six",
        7: "Seven",
        8: "Eight",
        9: "Nine",
        10: "Ten",
        11: "Eleven",
        12: "Twelve",
        13: "Thirteen",
        14: "Fourteen",
        15: "Fifteen",
        16: "Sixteen",
        17: "Seventeen",
        18: "Eighteen",
        19: "Nineteen",
        20: "Twenty",
        30: "Thirty",
        40: "Forty",
        50: "Fifty",
        60: "Sixty",
        70: "Seventy",
        80: "Eighty",
        90: "Ninety",
        100: "Hundred",
        1000: "Thousand",
        1000000: "Million",
        1000000000: "Billion"}

        s = str(num)
        n = len(s)
        def hundred(number):
            return df[number//100] + ' ' + df[100]
        def moreThanThousand(number,di):
            if number >= di * 100:
                    return hundred(number//di) + ' ' + df[di]
            return df[number//di] + ' ' + df[di]
        def words(number):
            if number > 0:
                if number < 100:
                    return df[number]
                elif number < 1000:
                    return hundred(number)
                elif number < 1000000:
                    return moreThanThousand(number,1000)
                elif number < 1000000000:
                    return moreThanThousand(number,1000000)
                return moreThanThousand(number,1000000000)
            return ''
        result = ''
        for j in range(n//3 + n%3):
            ss = s[-3:]
            ssn = len(ss)
            if ssn:
                ssi = int(ss)
                if j > 0 and ssi:
                    result = df[1000**j] + ' ' + result
                if(ssi > 20):
                    ten = int(ss[-2:])
                    if ten < 20 and ten >= 10:
                        result = df[ten] + ' ' + result
                        result = words(int(ss[0]) * 100) + ' ' + result
                    else:
                        for i in range(1,ssn + 1):
                            number = int(ss[ssn-i]) * (10**(i-1))
                            if number == 10:
                                result = df[int(ss[-2:])] + ' ' + result
                                break
                            if number:
                                result = words(number) + ' ' + result
                else:
                    if ssi:
                        result = df[ssi] + ' ' + result
            s = s[:-3]

        return result.strip()
