# Praktikum4

## Latihan 1

membuat program sederhana dengan input 2 buah bilangan, kemudian tentukan bilangan terbesar dari kedua bilangan tersebut menggunakan statement if.

program
```python
# input nilai variable
a = input("Bilangan ke-1 :")
b = input("Bilangan ke-2 :")

# jika bilangan ke 1 lebih besar 
if a > b :
	print("Bilangan ke-1 yang terbesar")

# jika bilangan ke 2 lebih besar
elif b > a :
	print("Bilangan ke-2 yang terbesar")

# jika bilangan ke 1 ke 2 sama besar
else:
	print("Bilangan ke-1 dan ke-2 sama besarnya")
```

![1](https://user-images.githubusercontent.com/123666514/215334712-e9edc63f-0f09-4b52-bd55-f05894bc6244.PNG)

## Latihan 2

Membuat program untuk mengurutkan data berdasarkan input sejumlah data dengan tampilkan hasilnya secara berurutan mulai dari data terkecil.

program
```python
#menampilkan karakter
print("Perogram mengurutkan data")
# input nilai variable
a = input("Bilangan ke-1 : ")
b = input("Bilangan ke-2 : ")
c = input("Bilangan ke-3 : ")

if a<b and a<c:
    if b<c:
            print("Urutan bilangan:", a, b, c)
    else:
            print("Urutan bilangan:", a, c, b)
elif b<a and b<c:
    if a<c:
            print("Urutan bilangan:", b, a, c)
    else:
            print("Urutan bilangan:", b, c, a)
else:
    if a<b:
            print("Urutan bilangan:", c, a, b)
    else:
            print("Urutan bilangan:", c, b, a)
```

![2](https://user-images.githubusercontent.com/123666514/215335096-3dcff943-1012-4f5c-8704-c898c389cb2d.PNG)

## Latihan 3

Membuat program dengan perulangan bertingkat (nested) for.

program
```python
# melakukan pengulangan 0-9
for i in range(0,10):
    # melakukan pengulangan 0-9
    for j in range(0,10):
        # menampilkan hasil dari i+j dengan rata kiri di posisi 3
        print('{0:<3}'.format(i+j), end=' ')
    # menampilkan garis ganti/membuat garis baru
    print()
 ```

![3](https://user-images.githubusercontent.com/123666514/215335283-7d93f466-9ebb-44f0-a3d3-a41703710cf5.PNG)

## Latihan 4
*Tampilkan n bilangan acak yang lebih kecil dari 0.5.
*nilai n diisi pada saat runtime
*anda bisa menggunakan kombinasi while dan for untuk menyelesaikannya

program
```python
# mengimport uniform dari library random
from random import uniform

# input nilai variable n
n = int(input("masukkan jumlah n : "))
 
# mengenerate sebanyak variable n
for i in range(n):
    # membuat variable j bernilai acak dari 0 sampai 0,5
    j = uniform(0,0.5)
    # menampilkan variabel j dengan 17 angka max di balakang koma
    print(round(j,17))
 ```
 
![4](https://user-images.githubusercontent.com/123666514/215335646-166e871b-2316-402b-afe3-c588dcf0db66.PNG)
