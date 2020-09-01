cases = int(input())

for test in range(cases):
    city_count = int(input())
    cities = []

    for city_index in range(city_count):
        city = input()
        if city not in cities:
            cities.append(city)

    print(len(cities))
