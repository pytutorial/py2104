# Cho truoc 1 so K > 0
# Tim n nho nhat de:
#  1 + 2 + 3 + .. n > K
K = 1000
n = 0
S = 0

while S <= K:
    n += 1
    S += n

print(n, S)