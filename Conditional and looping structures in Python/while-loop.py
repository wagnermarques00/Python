# While

option = 1
while option != 0:
    option = int(input("[1] Withdraw \n[2] Extract \n[0] Quit\n"))
    if option == 1:
        print("Withdraw option")
    elif option == 2:
        print("Extract option")
else:
    print("Program finished")
