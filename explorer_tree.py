lst = []

for item in lst:
    p = PC
    for x in item.split('/'):
        p = p.setdefault(x, {})

print(PC)
