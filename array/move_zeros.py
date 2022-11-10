sample = [1,2,0,3,0,4,0]

res = []

for i in sample:
    if i == 0:
        continue
    else:
        res.append(i)
print(res)