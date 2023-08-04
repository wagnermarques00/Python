balance = 2000.0
withdraw = float(input("Enter the withdrawal amount: "))

# If
if balance >= withdraw:
    print("Cashout done!")

if balance <= withdraw:
    print("Insufficient balance!")

# Else
if balance >= withdraw:
    print("Cashout done!")

else:
    print("Insufficient balance!")


# Else if
option = int(input("Enter an option: \n[1] Withdraw \n[2] Extract "))
if option == 1:
    print("Withdrawal option")
elif option == 2:
    print("Extract option")
else:
    print("Invalid option")


# Ternary
status = "Success" if balance >= withdraw else "Failed"
print(f"{status} to perform withdrawal")
