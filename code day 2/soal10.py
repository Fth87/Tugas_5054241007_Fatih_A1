# Write a program to control a bread machine

# Fungsi untuk menampilkan instruksi berdasarkan tipe roti
def display_instructions(bread_type, loaf_size, manual_baking):
    print("Mesin roti dimulai...")
    
    if bread_type == 'W':
        print("\nMemilih jenis roti: White Bread")
        print("1. Menguleni (Kneading): 15 menit")
        print("2. Pengistirahatan (Resting): 5 menit")
        print("3. Menguleni kedua (Kneading 2): 18 menit")
        print("4. Fermentasi pertama (First rising): 60 menit")
        print("5. Pembentukan loaf (Loaf shaping): 2 detik")
        baking_time = 35  # Waktu baking untuk White Bread
        
    elif bread_type == 'S':
        print("\nMemilih jenis roti: Sweet Bread")
        print("1. Menguleni (Kneading): 20 menit")
        print("2. Pengistirahatan (Resting): 5 menit")
        print("3. Menguleni kedua (Kneading 2): 33 menit")
        print("4. Fermentasi pertama (First rising): 60 menit")
        print("5. Pembentukan loaf (Loaf shaping): 2 detik")
        baking_time = 45  # Waktu baking untuk Sweet Bread
    
    # If the loaf size is double, increase the baking time by 50%.
    if loaf_size == 'Y':
        baking_time *= 1.5

    #  If baking is manual, stop after the loaf-shaping cycle and instruct the user to remove the dough for manual baking
    if manual_baking == 'Y':
        print("Pilih manual baking: Silakan keluarkan adonan untuk dipanggang manual.")
    else:
        print(f"6. Baking: {int(baking_time)} menit")
    
# Meminta input dari pengguna
def main():
    bread_type = input("Masukkan jenis roti (W untuk White, S untuk Sweet): ").upper()
    loaf_size = input("Apakah ukuran loaf double? (Y untuk Ya, N untuk Tidak): ").upper() 
    manual_baking = input("Apakah akan baking secara manual? (Y untuk Ya, N untuk Tidak): ").upper() 

    # Menampilkan instruksi dan menghitung waktu baking
    display_instructions(bread_type, loaf_size, manual_baking)


# Menjalankan program
main()
