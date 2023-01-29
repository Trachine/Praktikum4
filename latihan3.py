# melakukan pengulangan 0-9
for i in range(0,10):
    # melakukan pengulangan 0-9
    for j in range(0,10):
        # menampilkan hasil dari i+j dengan rata kiri di posisi 3
        print('{0:<3}'.format(i+j), end=' ')
    # menampilkan garis ganti/membuat garis baru
    print()