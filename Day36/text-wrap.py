import textwrap

def wrap(string, max_width):
    new_string = ''
    for i in range(0,len(string),max_width):
        new_string += string[i:i+max_width] + '\n'
    return new_string

if __name__ == '__main__':
    string, max_width = input(), int(input())
    result = wrap(string, max_width)
    print(result)