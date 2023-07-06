"""
x = 0
print(f"x = {x}")
while x < 5:
    print(f"X is at {x}")
    x = x + 1
print(f"x = {x}")
 """


def print_range(start, end):
    n = start
    while n <= end:
        print(n)
        n += 1

print_range(1, 5)
def multiplication_table(number):
    multiplier = 1
    while multiplier <= 5:
        result = number * multiplier
        if result > 25:
            break
        print(f"{number} x {multiplier} = {result}")
        multiplier += 1


multiplication_table(3)