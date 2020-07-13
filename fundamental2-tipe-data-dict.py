"""
tipe data dictionary sekedar menghubungkan antara KEY dan VALUE
kvp = Key Value Pair
dictionary = kamus
"""

kamus_ind_eng = {'anak': 'son', 'istri': 'wife', 'ayah': 'father', 'ibu': 'mother'}

print(kamus_ind_eng)
print(kamus_ind_eng['ayah'])
print(kamus_ind_eng['ibu'])

print('\ndata ini di kirimkan oleh server gojek, untuk memberikan info driver di sekitar pemakai aplikasi')
data_dari_server_gojek = {
    'tanggal': '2020-06-10',
    'driver_list': [
        {'nama': 'eko', 'jarak': 10},
        {'nama': 'dwi', 'jarak': 30},
        {'nama': 'tri', 'jarak': 100},
        {'nama': 'catur', 'jarak': 1000}
    ]
}
print(data_dari_server_gojek)
print(f"\ndriver disekitar sini{data_dari_server_gojek['driver_list']}")
print(f"driver #1 {data_dari_server_gojek['driver_list'][0]}")
print(f"driver #4 {data_dari_server_gojek['driver_list'][3]}")
print(f"driver terdekat berjarak {data_dari_server_gojek['driver_list'][0]['jarak']} meter")
