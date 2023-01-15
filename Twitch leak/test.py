L = [(1,2), (8,9)]

sum_x = 0
sum_y = 0

for x,y in L:
    sum_x += x
    sum_y += y

print(sum_x / len(L), sum_y / len(L))