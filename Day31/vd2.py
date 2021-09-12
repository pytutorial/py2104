#Cho 1 day so, tim so chan dau tien
lst = [ 3, 2, 1, 4, 5, 6]
n = len

for x in lst:
    if x%2 == 0:
        print(x)
        break

# Tinh binh phuong cua cac phan tu trong day
lst2 = []
for x in lst:
    lst2.append(x*x)

lst2 = [x*x for x in lst]