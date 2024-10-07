p, d = input().split()
p = int(p)
d = int(d)
i = 0
if p % 2 == 0:
    while True:
        i += 1
        if (d * i) % p <= p / 2:
            break
        else:
            continue
print(d*i) 
