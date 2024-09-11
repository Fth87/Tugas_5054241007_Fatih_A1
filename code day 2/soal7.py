#menghitung hari pada inputan hari bulan tahun

day = int(input("Masukkan hari (1-31): "))
month = input("Masukkan bulan (Januari-Desember): ").capitalize() 
year = int(input("Masukkan tahun: "))

# Daftar bulan dan jumlah hari di setiap bulan untuk tahun biasa
months = ["Januari", "Februari", "Maret", "April", "Mei", "Juni", "Juli", "Agustus", "September", "Oktober", "November", "Desember"]
days_in_month = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

# Menentukan apakah tahun kabisat
if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
    leap_year = True
else:
    leap_year = False

# Jika tahun kabisat, ubah Februari menjadi 29 hari
if leap_year:
    days_in_month[1] = 29

# Validasi input bulan
if month not in months:
    print("Nama bulan tidak valid.")
else:
    # Menghitung nomor bulan dari daftar "months"
    month_index = months.index(month)
    
    # Menghitung nomor hari dalam setahun
    day_number = sum(days_in_month[:month_index]) + day

    print(f"Nomor hari untuk tanggal {day} {month} {year} adalah: {day_number}")
