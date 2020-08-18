numerator, denominator = map(int, input().split())

while numerator != 0:
    div_mod = divmod(numerator, denominator)
    print(div_mod[0], div_mod[1], "/", denominator)
    numerator, denominator = map(int, input().split())
