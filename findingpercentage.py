
'''
The average of the marks obtained by the particular student correct to 2 decimal places.

INPUT

3
Krishna 67 68 69
Arjun 70 98 63
Malika 52 56 60
Malika

OUTPUT
56.00
'''


if __name__ == '__main__':
    n = int(input())
    student_marks = {}
    for _ in range(n):
        name, *line = input().split()
        scores = list(map(float, line))
        student_marks[name] = scores
    query_name = input()

    result = sum(student_marks[query_name])/len(student_marks[query_name])
    print("%.2f" % result)
