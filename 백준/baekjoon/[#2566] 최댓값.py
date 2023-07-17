matrix = [list(map(int, input().split())) for _ in range(9)]
max_value = 0
row_index, col_index = 0,0
for row in range(9):
    for col in range(9):
        if matrix[row][col] >= max_value:
            row_index = row +1
            col_index = col +1
            max_value = matrix[row][col]

print(max_value)
print(row_index, col_index)
        
