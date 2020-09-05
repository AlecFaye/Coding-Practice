cases = int(input())

for test in range(cases):
    rope_count = int(input())

    if rope_count <= 1:
        throw_away = input()
        print("Case #" + str(test + 1) + ": 0")
    else:
        ropes = input().split()
        red_ropes = []
        blue_ropes = []

        for current_rope in ropes:
            if current_rope[-1] == "R":
                red_ropes.append(int(current_rope[:len(current_rope) - 1]))
            else:
                blue_ropes.append(int(current_rope[:len(current_rope) - 1]))

        red_ropes.sort()
        blue_ropes.sort()

        red_ropes.reverse()
        blue_ropes.reverse()

        loop_length = 0
        ropes_used = 0

        if len(red_ropes) > len(blue_ropes):
            for index in range(len(blue_ropes)):
                loop_length += red_ropes[index]
                loop_length += blue_ropes[index]
                ropes_used += 2
        else:
            for index in range(len(red_ropes)):
                loop_length += red_ropes[index]
                loop_length += blue_ropes[index]
                ropes_used += 2

        print("Case #" + str(test + 1) + ": " + str(loop_length - ropes_used))
