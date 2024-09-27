#“Kalau kamu udah bisa baca ini, ya artinya tau lah ya harus ngapain. Untuk membedakan input, aku memiliki input code dan key, code 1 untuk encrypt dan code 2 untuk decrypt. Selanjutnya key itu yang bakal dipake buat jadi kunci shift caesarnya. Yang diproses hanya huruf saja ya! Selain huruf di print tanpa diproses

#Baris pertama adalah T, yaitu menyatakan jumlah kasus uji. Setiap kasus uji memiliki 2 baris, baris pertama berisi C yaitu code dan K yaitu key, baris kedua merupakan kalimat yang ingin di encrypt/decrypt.

#spasi gaperlu diproses

# masukkan jumlah kasus uji
T = int(input())
# loop untuk setiap kasus uji
for _ in range(T):
    #masukkan code dan key
    code,key = map(int,input().split())
    kalimat = input()
    result = ""
    for char in kalimat:
        if char.isalpha():
            if char.isupper():
                result += chr((ord(char) + key - 65) % 26 + 65) if code == 1 else chr((ord(char) - key - 65) % 26 + 65)
            else:
                result += chr((ord(char) + key - 97) % 26 + 97) if code == 1 else chr((ord(char) - key - 97) % 26 + 97)
        else:
            result += char

print(result)


