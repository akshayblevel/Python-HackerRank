# Complete the average function

def average(array):
    s = set(array)
    avg = sum(s)/len(s)
    return avg


if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().split()))
    result = average(arr)
    print(result)

'''
Sample Input                                  
10                                          
161 182 161 154 176 170 167 171 170 174  

Sample Output
169.375
'''