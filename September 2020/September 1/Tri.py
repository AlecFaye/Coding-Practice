first, second, third = map(int, input().split())


def operations():
    if first + second == third:
        return str(first) + "+" + str(second) + "=" + str(third)

    if first - second == third:
        return str(first) + "-" + str(second) + "=" + str(third)

    if first * second == third:
        return str(first) + "*" + str(second) + "=" + str(third)

    if second != 0:
        if first / second == third:
            return str(first) + "/" + str(second) + "=" + str(third)

    if second + third == first:
        return str(first) + "=" + str(second) + "+" + str(third)

    if second - third == first:
        return str(first) + "=" + str(second) + "-" + str(third)

    if second * third == first:
        return str(first) + "=" + str(second) + "*" + str(third)

    if third != 0:
        if second / third == first:
            return str(first) + "=" + str(second) + "/" + str(third)


print(operations())
