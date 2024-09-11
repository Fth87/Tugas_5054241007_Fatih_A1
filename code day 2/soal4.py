#Program untuk menampilkan isi tabung gas berdasarkan kata pertama warna tabung

color = input("Enter the first color of the gas : ")

# Mengubah input menjadi huruf kecil untuk memudahkan pengecekan
match color.lower():
  case 'o':
    cylinder = 'ammonia'
  case 'b':
    cylinder = 'carbon monoxide'
  case 'y':
    cylinder = 'hydrogen'
  case 'g':
    cylinder = 'oxygen'
  case _:
    cylinder = 'unknown'

print(f"contents of a compressed-gas cylinder  : {cylinder}")
