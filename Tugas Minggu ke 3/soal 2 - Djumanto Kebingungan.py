arr_numbers = input("masukkan angka (pisahkan dengan spasi): ").split()

final_result = ""
for numbers in arr_numbers:
  # convert inputan ke biner
  binary_numbers = bin(int(numbers))[2:] #[2:] untuk menghilangkan '0b' di depan

  # jika panjang biner kurang dari 32, tambahkan '0' di depan
  if len(binary_numbers) < 32:
    binary_numbers = '0' * (32 - len(binary_numbers)) + binary_numbers

  # tempat menyimpan hasil karakter ASCII setelah dikonversi
  result = ""

  # bagi bilangan biner menjadi 8 bit
  for i in range(4): # 4 karena akan dibagi menjadi 4 bagian
    # biner dibagi menjadi 8 bit
    splitted_binary = binary_numbers[i*8:i*8+8]

    # konversi biner 8 bit ke desimal
    decimal = int(splitted_binary, 2)

    # konversi desimal ke karakter ASCII
    result += chr(decimal)

  # menyimpan karakter ASCII setelah dikonversi
  final_result += result

print(final_result)


# #Versi hexadecimal
# arr_numbers = input("masukkan angka (pisahkan dengan spasi): ").split()

# final_result = ""
# for numbers in arr_numbers:
#   # convert inputan ke hexadecimal
#   hex_numbers = hex(int(numbers))[2:] #[2:] untuk menghilangkan '0x' di depan
  
#   for i in range(len(str(hex_numbers)) // 2):
#     # tempat menyimpan karakter ASCII setelah dikonversi
#     decimal = int(str(hex_numbers)[i*2:i*2+2], 16)

#     # konversi desimal ke karakter ASCII
#     result = chr(decimal)

#     # menyimpan karakter ASCII setelah dikonversi
#     final_result += result

# print(final_result)

##Versi dengan numpy
# import numpy as np
# total_input = int(input("masukkan berapa jumlah inputan: "))
# arr_numbers = [0] * total_input

# for i in range(total_input):
#     numbers = int(input("masukkan angka: "))
#     arr_numbers[i] = numbers

# final_result = ""
# for numbers in arr_numbers:
#   # convert inputan ke biner
#   binary = np.binary_repr(numbers, width=32)

#   # bagi bilangan biner menjadi 8 bit
#   splitted_binary = [str(binary)[i:i+8] for i in range(0, len(str(binary)), 8)]

#   result = ""
#   for i in splitted_binary:
#     # convert bilangan biner yang sudah dibagi menjadi desimal
#     decimal = int(i, 2)

#     # convert desimal ke karakter ASCII
#     result += chr(decimal)
#   final_result += result

# print(final_result)