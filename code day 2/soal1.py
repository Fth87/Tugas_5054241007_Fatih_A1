#Program untuk kasir( menghitung total harga setelah diskon untuk pelajar dan juga pajak)

totalpurchase = float(input("Enter the total purchase : "))
student = input("Are you a student? (y/n) : ")

if(student == "y"):
    discount = totalpurchase * 20/100
elif(student == "n"):
    discount = 0

discountpurchase = totalpurchase - discount
tax = discountpurchase * 5/100
finalpurchase = discountpurchase + tax 

print(f"Total purchase           : ${totalpurchase}")
if(student == "y"):
    print(f"Student’s discount (20%) : ${discountpurchase:.2f}")
print(f"Sales tax(5%)            : ${tax:.2f}")
print(f"Total                    : ${finalpurchase:.2f}")