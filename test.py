# source = ["/*Test program */", "int main()", "{ ", "  // variable declaration ", "int a, b, c;", "/* This is a test", "   multiline  ", "   comment for ", "   testing */", "a = b + c;", "}"]
source = ["a/*comment", "line", "more_comment*/b"]

n = len(source)
code = []
for i in range(n):
    source[i] = source[i].split("//")[0]
block_opened = False

