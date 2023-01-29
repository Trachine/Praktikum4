# menampilkan karakter
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
