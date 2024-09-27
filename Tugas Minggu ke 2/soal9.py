
#Write a program that prompts the user to enter the number of weekday minutes, night minutes, and weekend minutes used, and calculates the monthly bill and average cost of a minute before taxes.

weekday_minutes = int(input("Enter the number of weekday minutes: "))
night_minutes = int(input("enter night minutes: "))
weekend_minutes = int(input("Enter weekend minutes used: "))

# Konstanta tarif dan pajak
flat_rate = 39.99 
additional_rate_per_minute = 0.40  
tax_rate = 5.25/100  
included_weekday_minutes = 600

# Menghitung total biaya sebelum pajak
pretax_bill = flat_rate

# Menentukan biaya tambahan jika penggunaan melebihi 600 menit di hari kerja
if weekday_minutes > included_weekday_minutes:
    extra_minutes = weekday_minutes - included_weekday_minutes
    pretax_bill += extra_minutes * additional_rate_per_minute

# Menghitung pajak
taxes = pretax_bill * tax_rate

# Menghitung total tagihan setelah pajak
total_bill = pretax_bill + taxes

# Menghitung biaya rata-rata per menit (menggunakan semua jenis menit)
total_minutes_used = weekday_minutes + night_minutes + weekend_minutes
average_minute_cost = pretax_bill / total_minutes_used

# Menampilkan hasil
print(f"Tagihan sebelum pajak: ${pretax_bill:.2f}")
print(f"Biaya rata-rata per menit: ${average_minute_cost:.2f}")
print(f"Pajak: ${taxes:.2f}")
print(f"Total tagihan: ${total_bill:.2f}")
