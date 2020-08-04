cases = int(input())

for test in range(cases):
    bp = input().split()
    beats = int(bp[0])
    seconds = float(bp[1])

    margin = 60.0 / seconds
    BPM = margin * beats

    print(str(round(BPM - margin, 4)) + " " + str(round(BPM, 4)) + " " + str(round(BPM + margin, 4)))
