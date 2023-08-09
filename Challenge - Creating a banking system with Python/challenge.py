menu = """

[d] Depósito
[e] Extrato
[s] Saque
[q] Sair

=>"""

balance = 0
limit = 500
extract = ""
number_witdhraws = 0
LIMIT_WITDHRAWS = 3

while True:
    option = input(menu)

    if option == "d":
        amount = float(input("Informe o valor do depósito: "))

        if amount > 0:
            balance += amount
            extract += f"Depósito: R$ {amount:.2f}\n"
        else:
            print("Depósito falhou! O valor informado é inválido")
    elif option == "s":
        amount = float(input("Informe o valor do saque: "))

        exceded_balance = amount > balance
        exceded_limit = amount > limit
        exceded_withdraws = number_witdhraws >= LIMIT_WITDHRAWS

        if exceded_balance:
            print("Operação falhou! Você não tem saldo suficiente.")
        elif exceded_limit:
            print("Operação falhou! O valor do saque excede o limite")
        elif exceded_withdraws:
            print("Operação falhou! Número máximo de saques excedido.")
        elif amount > 0:
            balance -= amount
            extract += f"Saque: R$ {amount:.2f}\n"
            number_witdhraws += 1
        else:
            print("Operação falhou! O valor informado é inválido.")
    elif option == "e":
        print("\n====================EXTRATO====================")
        if not extract:
            print("Não foram realizadas movimentações.")
        else:
            print(extract)
        print(f"\nSaldo: R$ {balance:.2f}")
        print("=================================================")
    elif option == "q":
        print(">>> Programa encerrado. <<<q")
        break
    else:
        print("Operação inválida, selecione novamente a operação desejada.")
