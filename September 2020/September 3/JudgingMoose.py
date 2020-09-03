left, right = map(int, input().split())

if left == 0 and right == 0:
    print("Not a moose")
elif left > right:
    print("Odd", left * 2)
elif right > left:
    print("Odd", right * 2)
else:
    print("Even", left + right)
