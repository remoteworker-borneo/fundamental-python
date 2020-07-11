# tipe data skalar = tipe data sederhana
anak1 = 'eko'
anak2 = 'dwi'
anak3 = 'eko'
anak4 = 'catur'

print(anak1)
print(anak2)
print(anak3)
print(anak4)

print('\ntipe data list/daftar/array')
anak = ['eko', 'dwi', 'tri', 'catur']
print(anak)
anak.append('limo')
print(anak)

print('\nsapa anak ke-2')
print(f'hai {anak[1]}!')

print('\nsapa semua anak')
for a in anak:
    print(f'hai {a}!')

print('\nsapa semua anak: cara ribet')
for a in range(0,len(anak)):
    print(f'{a+1}. hai {anak[a]}')