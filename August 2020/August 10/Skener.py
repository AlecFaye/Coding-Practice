row_col_zoom = input().split()

row = int(row_col_zoom[0])
col = int(row_col_zoom[1])
row_zoom = int(row_col_zoom[2])
col_zoom = int(row_col_zoom[3])

article = []

for count in range(row):
    row_input = input()
    empty_row = []

    for character in row_input:
        empty_row.append(character)

    article.append(empty_row)

for current_row in article:
    for row_count in range(row_zoom):

        for character in current_row:
            for col_count in range(col_zoom):
                print(character, end="")
        print()
