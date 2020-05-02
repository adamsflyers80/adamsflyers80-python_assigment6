asal_sayılar = []
for i in range(1,100):
    for b in range(2,i):
        if (i%b==0):
            break
        else:
            asal_sayılar.append(i)
print(asal_sayılar)
