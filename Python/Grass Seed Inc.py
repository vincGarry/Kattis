a = float(input())
b = int(input())
total =0
for x in range(b):
    c = input().split()
    d = float(c[0])
    e = float(c[1])
    total= total+(d*e*a)
print("%.7f"%total)