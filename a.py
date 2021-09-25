first_row = 1
first_column = 'A'
for i in range(3):
    for j in range(3):
        curr_row = first_row + i
        curr_col = chr(ord(first_column) + j)
        print(str(curr_row) + str(curr_col), end=' ')