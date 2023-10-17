#Максим Нещерет КІ-1

massive = [ 
    [8, 24, 13,], 
    [1, 10, 6,],
    [7, 12, 9,],
]
sums_and_rows = [(sum(row), row) for row in massive]

sort_sum_rows = sorted(sums_and_rows, key=lambda x: x[0])

sorted_massive = [row for _, row in sort_sum_rows]

print("Суми рядків по зростанню:")
for row in sorted_massive: 
    print(sum(row))

print("\nРядки по зростанню:")
for row in sorted_massive: 
    print(row)