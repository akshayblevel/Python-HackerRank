# Output the total number of distinct country stamps on a single line.

n = int(input())
s = set()
for _ in range(n):
    name = input()
    s.add(name)

print(len(s))

'''
Sample Input
7
UK
China
USA
France
New Zealand
UK
France 

Sample Output
5
'''