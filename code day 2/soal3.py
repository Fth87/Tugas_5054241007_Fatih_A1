
# Function fun1 should prompt the user to enter “T” for true or “F” for false.
def fun1():
    input_value = input("Enter 'T' for true or 'F' for false: ")
    if input_value == 'T':
        return 1
    else:
        return 0


#Function fun2 should simply display “fun2 executed” and then return 1. 
def fun2():
    print("fun2 executed")
    return 1

#Function main should include two conditional statements: one that displays 
#“Test of && complete” if the && of function calls to fun1 and fun2 is true.
#The second conditional statement should display “Test of || complete” if 
#the || of function calls to fun1 and fun2 is true  


# Fungsi utama (main)
def main():
    # Testing AND (&&)
    print("Testing &&")
    if fun1() and fun2():
        print("Test of && complete")

    # Testing OR
    print("Testing ||")
    if fun1() or fun2():
        print("Test of || complete")

#start the program
main()