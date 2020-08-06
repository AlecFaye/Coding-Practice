import math

input_articles_factor = input().split()

articles = float(input_articles_factor[0])
impact_factor = float(input_articles_factor[1])

citations = articles * impact_factor

while math.ceil(citations / articles) >= impact_factor:
    citations -= 1

print(int(citations + 1))
