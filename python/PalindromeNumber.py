def isPalindrome(x):
    if x < 0 or (x % 10 == 0 and x != 0):
        return False
    reverted = 0
    while x > reverted:
        reverted = int(reverted * 10) + int(x % 10)
        x = int(x / 10)

    return x == reverted or x == int(reverted / 10)