# sWAP cASE
def swap_case(s):
    result = ""
    for i in s:
        if i == i.lower():
            result += i.upper()
        elif i == i.upper():
            result += i.lower()
    return result