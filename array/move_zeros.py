sample = [1,2,0,3,0,4,0]

res = []
count = 0
for i in sample:
    if i == 0:
        count = count + 1
        continue
    else:
        res.append(i)
res = res + [0] * count
print(res)