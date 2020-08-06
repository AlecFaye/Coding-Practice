cases = int(input())

for test in range(cases):
    fox_noises = []
    fox_sounds = ""

    forest_noises = input().split()
    animal_noises = []

    current_noise = input()

    while current_noise != "what does the fox say?":
        noise_array = current_noise.split()
        animal_noises.append(noise_array[2])
        current_noise = input()

    for noise in forest_noises:
        if noise not in animal_noises:
            fox_noises.append(noise)

    for index in range(len(fox_noises)):
        if index != len(fox_noises) - 1:
            fox_sounds += fox_noises[index] + " "
        else:
            fox_sounds += fox_noises[index]

    print(fox_sounds)
