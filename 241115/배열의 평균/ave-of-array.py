arr_2d = [list(map(int, input().split())) for _ in range(2)]
avg_row = []
avg_col = []
avg_total = []

for i in range(2):
    sum_row = sum(arr_2d[i])
    avg_row.append(sum_row/4)
    avg_total.append(sum_row)

    if i==1:
        continue
    else:
        for j in range(4):
            avg_col.append((arr_2d[0][j]+arr_2d[1][j])/2)

print(f"{avg_row[0]:.1f} {avg_row[1]:.1f}")
print(f"{avg_col[0]:.1f} {avg_col[1]:.1f} {avg_col[2]:.1f} {avg_col[3]:.1f}")
print(f"{((avg_total[0]+avg_total[1])/8):.1f}")