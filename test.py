# source = ["/*Test program */", "int main()", "{ ", "  // variable declaration ", "int a, b, c;", "/* This is a test", "   multiline  ", "   block for ", "   testing */", "a = b + c;", "}"]
source = ["a/*comment", "line", "more_comment*/b"]
code = []
block = False
line = ''
for s in source:
    n = len(s)
    i = 0
    while i < n: 
        if not block:
            if s[i] == '/' and i != n - 1 and s[i+1] == '/': 
                break
            elif s[i] == '/' and i != n - 1 and s[i+1] == '*':
                block = True
                i+=1
            else:
                line += s[i]
        else:
            if s[i] == '*' and i < n-1 and s[i+1] == '/':
                block = False
                i+=1
        i += 1
    if not block and len(line) > 0:
        code.append(line)
        line = ''
print(code)
# List<String> code = new ArrayList<>();
# StringBuilder sb = new StringBuilder();
# boolean block = false;
# for (String s: source) {
#     for (int i = 0; i < s.length(); i++) {
#         if (!block) {
#             if (s.charAt(i) == '/' && i != s.length()-1 && s.charAt(i+1) == '/') break;
#             else if (s.charAt(i) == '/' && i != s.length()-1 && s.charAt(i+1) == '*') {
#                 block = true;
#                 i++;
#             }
#             else sb.append(s.charAt(i));
#         } else {
#             if (s.charAt(i) == '*' && i < s.length()-1 && s.charAt(i+1) == '/') {
#                 block = false;
#                 i++;
#             }
#         }
#     }
#     if (!block && sb.length() > 0) {
#         code.add(sb.toString());
#         sb.setLength(0);
#     }
# }
# return code;