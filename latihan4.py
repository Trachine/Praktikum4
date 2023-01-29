from random import uniform

# input nilai variable n
n = int(input("masukkan jumlah n : "))
 
# mengenerate sebanyak variable n
for i in range(n):
    # membuat variable j bernilai acak dari 0 sampai 0,5
    j = uniform(0,0.5)
    # menampilkan variabel j dengan 17 angka max di balakang koma
    print(round(j,17))