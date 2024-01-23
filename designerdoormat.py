
arr = map(int, input().split())
lst = list(arr)
n = lst[0]
m = lst[1]

def print_dash(occurrence,is_end):
    if is_end:
        print(f'{occurrence * "-"}', end="")
    else:
        print(f'{occurrence * "-"}')


def print_pattern(occurrence):
    print(f'{occurrence * ".|."}', end="")


def print_string(str):
    print(f'{str}', end="")


counter = 3
increment = 1
for i in range(0, n):
    mid = n // 2
    if i < mid:
        dash = (m - counter*increment) // 2
        print_dash(dash, True)
        print_pattern(increment)
        print_dash(dash, False)
        increment += 2
    elif i == mid:
        print_dash((m - 7)//2, True)
        print_string("WELCOME")
        print_dash((m - 7)//2, False)
    else:
        increment -= 2
        dash = (m - counter * increment) // 2
        print_dash(dash, True)
        print_pattern(increment)
        print_dash(dash, False)
