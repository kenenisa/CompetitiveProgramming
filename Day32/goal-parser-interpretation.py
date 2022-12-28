class Solution:
    def interpret(self, command: str) -> str:
        i = 0
        n = len(command)
        result = ''
        while i < n:
            if command[i] == "G":
                result += "G"
            elif command[i] == "(":
                if command[i + 1] == ")":
                    result += "o"
                    i += 1
                else:
                    result += "al"
                    i+=2
            i+=1
        return result