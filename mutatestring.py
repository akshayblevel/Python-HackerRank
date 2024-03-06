# Read a given string, change the character at a given index and then print the modified string.

def mutate_string(string, position, character):
    str = string[:position] + character + string[position+1:]
    return str

if __name__ == '__main__':
    s = input()
    i, c = input().split()
    s_new = mutate_string(s, int(i), c)
    print(s_new)

# INPUT
# abracadabra
# 5 k

# OUTPUT
# abrackdabra
