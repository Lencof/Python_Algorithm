# __Author__ __Lencof__
# fibonacci_sort.py

f1 = f2 = 1
n = 10

print(f1, end=' ')
print(f2, end=' ')

for i in range(2, n):
    f1, f2 = f2, f1 + f2
    print(f2, end=' ')
    
# 1 1 2 3 5 8 13 21 34 55
# nominal numbers
