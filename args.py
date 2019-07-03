def tambah(a, b):
    result = a + b
    print(result)


tambah(3, 5)

print('--------------------------------')


def args_tambah(*args):
    print(sum(args))


list_angka = [7, 8, 9, 10]
args_tambah(*list_angka)
