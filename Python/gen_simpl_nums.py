n = int(input("n="))
simp_lst = []
k = 0
for i in range(2, n+1):
    for j in range(2, i):
        if i % j == 0:
            k = k + 1
    if k == 0:
        simp_lst.append(i)
    else:
        k = 0
print(simp_lst)