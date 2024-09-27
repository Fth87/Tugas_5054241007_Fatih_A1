#mencari karakter yang berdekatan ada berapa lalu dicari kerugiannya


huruf = list(input())

hurufDobel = ""
totalhurufDobel = 0

i = 0
while i < len(huruf) - 1:
    if huruf[i] == huruf[i + 1]:
        hurufDobel += huruf[i]
        totalhurufDobel += 1
        huruf = huruf[:i] + huruf[i+2:]
    else:
        i += 1


if(totalhurufDobel == 0):
    print(f"Di gudang tersisa {len(huruf)} batu \nwah, Jotaro Joemama tidak jadi dipecat")
else:
    rugi = 0 
    for i in range(len(hurufDobel)):
        rugi += ord(hurufDobel[i])*1000*2
    
    print(f'Di gudang tersisa {len(huruf)} \nTotal kerugian : {rugi} Dollar Imbu')


print(totalhurufDobel, huruf, hurufDobel )


