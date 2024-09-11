#calculate the charges to be paid by the subscriber


# Meminta input dari pengguna
data_usage = float(input("Enter the amount of data used (in GBs): "))


# Logika untuk menentukan biaya berdasarkan penggunaan data
if data_usage < 0:
        print("Bad data. Data usage cannot be negative.")
elif 0.0 <= data_usage <= 1.0:
    print(f"The charge for {data_usage} GB of data usage is: 250")
elif 1.0 < data_usage <= 2.0:
    print(f"The charge for {data_usage} GB of data usage is: 500")
elif 2.0 < data_usage <= 5.0:
    print(f"The charge for {data_usage} GB of data usage is: 1000")
elif 5.0 < data_usage <= 10.0:
    print(f"The charge for {data_usage} GB of data usage is: 1500")
elif data_usage > 10.0:
    print(f"The charge for {data_usage} GB of data usage is: 2000")
else:
    print("Bad data.")

