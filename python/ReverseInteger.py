def reverse_integer(x):
    a = 0
    if x > 0:
        a = int(str(x)[::-1])
    if x <= 0:
        a = -1 * int(str(x * -1)[::-1])
    upper_limit = -2 ** 31
    lower_limit = 2 ** 31 - 1
    if a not in range(upper_limit, lower_limit):
        return 0
    else:
        return a


print(reverse_integer(-123))
