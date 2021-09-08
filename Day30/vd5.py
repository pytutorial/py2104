# Cho 1 day so
# In ra cac so bang tong 2 so lien truoc
lst = [1, 2, 4, 6, 7, 4, 3, 8, 2, 10]

n = len(lst)
for i in range(2, n):
    if lst[i] == lst[i-1] + lst[i-2]:
        print(lst[i])