print()
print('## Nomor 1 ##')
def celcius_ke_fahrenheit (celcius):
    fahrenheit=(celcius*9/5)+32
    return fahrenheit
suhu_celcius1 = 0
suhu_celcius2 = 100
#Cetak 0 celcius ke 32 fahrenheit
suhu_fahrenheit1 = celcius_ke_fahrenheit (suhu_celcius1)
print('Suhu celcius' , suhu_celcius1, 'sama dengan', suhu_fahrenheit1)

#Cetak 100 celcius ke 212 fahrenheit
suhu_fahrenheit2 = celcius_ke_fahrenheit (suhu_celcius2)
print('Suhu celcius', suhu_celcius2, 'sama dengan', suhu_fahrenheit2)

print()
print('## Nomor 2 ##')
def genap_ganjil(bilangan):
   hitung = bilangan % 2 == 00 #Menentukan bilangan ganjil atau genap
   return hitung # Mengembalikan nilai hitung
angka = 4
hasil = genap_ganjil(angka)
print(f"Bilangan {angka} bernilai {hasil}")

angka2 = 7
hasil2 = genap_ganjil(angka2)
print(f"Bilangan {angka2} bernilai {hasil2}")

print()
print('## Nomor 3 ##')
def cek_kelulusan(nilai):
    if nilai > 60:
         return 'Lulus'
    else:
         return 'Gagal'

nilai_kamu = 95 # Mendefinisikan Nilai
status = cek_kelulusan(nilai_kamu) # Memanggil Fungsi dan Parameter
print(f"Nilai: {nilai_kamu}, Status: {status}")

nilai_kamu2 = 60 # Mendefinisikan Nilai
status2 = cek_kelulusan(nilai_kamu2) # Memanggil Fungsi dan Parameter
print(f"Nilai: {nilai_kamu2}, Status: {status2}")

print()
print('## Nomor 4 ##')
def bilangan_ganjil(number):
    for a in range(1, number, 2): # 1,3,5..19
        print(a, end=" ") # 1,3,5..19

bilangan_ganjil(20)
