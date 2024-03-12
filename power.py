# You are given three integers: a, b, and m. Print two lines.
# On the first line, print the result of pow(a,b). On the second line, print the result of pow(a,b,m).

a = int(input())
b = int(input())
m = int(input())

print(pow(a, b))
print(pow(a, b, m))

'''
INPUT
3
4
5

OUTPUT
81
1
'''