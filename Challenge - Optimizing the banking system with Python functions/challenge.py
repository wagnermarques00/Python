import textwrap


def menu():
    """
    Displays the menu options and prompts the user for a choice.

    Returns:
    str: The selected menu option.
    """
    menu = """\n
    ================ MENU ================
    [d]\tDepositar
    [s]\tSacar
    [e]\tExtrato
    [nc]\tNova conta
    [lc]\tListar contas
    [nu]\tNovo usuário
    [q]\tSair
    => """
    return input(textwrap.dedent(menu))


def deposit(balance, amount, extract, /):
    """
    Deposits a given amount into the account balance.

    Parameters:
    balance (float): The current account balance.
    amount (float): The amount to be deposited.
    extract (str): The current transaction history.

    Returns:
    tuple: The updated balance and transaction history.
    """
    if amount > 0:
        balance += amount
        extract += f"Depósito:\tR$ {amount:.2f}\n"
        print("\n=== Depósito realizado com sucesso! ===")
    else:
        print("\n@@@ Operação falhou! O valor informado é inválido. @@@")

    return balance, extract


def withdraw(*, balance, amount, extract, limit, number_withdraws, limit_withdraws):
    """
    Performs a withdrawal operation from the account balance.

    Parameters:
    balance (float): The current account balance.
    amount (float): The amount to be withdrawn.
    extract (str): The current transaction history.
    limit (float): The withdrawal limit.
    number_withdraws (int): The number of withdrawals already made.
    limit_withdraws (int): The maximum number of allowed withdrawals.

    Returns:
    tuple: The updated balance and transaction history.
    """
    balance_exceeded = amount > balance
    limit_exceeded = amount > limit
    withdraw_exceeded = number_withdraws >= limit_withdraws

    if balance_exceeded:
        print("\n@@@ Operação falhou! Você não tem saldo suficiente. @@@")

    elif limit_exceeded:
        print("\n@@@ Operação falhou! O valor do saque excede o limite. @@@")

    elif withdraw_exceeded:
        print("\n@@@ Operação falhou! Número máximo de saques excedido. @@@")

    elif amount > 0:
        balance -= amount
        extract += f"Saque:\t\tR$ {amount:.2f}\n"
        number_withdraws += 1
        print("\n=== Saque realizado com sucesso! ===")

    else:
        print("\n@@@ Operação falhou! O valor informado é inválido. @@@")

    return balance, extract


def print_extract(balance, /, *, extract):
    """
    Prints the account statement including transactions and balance.

    Parameters:
    balance (float): The current account balance.
    extract (str): The transaction history.

    Returns:
    None
    """
    print("\n================ EXTRATO ================")
    print("Não foram realizadas movimentações." if not extract else extract)
    print(f"\nSaldo:\t\tR$ {balance:.2f}")
    print("==========================================")


def create_user(users):
    """
    Creates a new user and adds it to the list of users.

    Parameters:
    users (list): The list of existing users.

    Returns:
    None
    """
    cpf = input("Enter the CPF (digits only): ")
    user = filter_user(cpf, users)

    if user:
        print("\n@@@ User with this CPF already exists! @@@")
        return

    name = input("Enter the full name: ")
    birth_date = input("Enter the birth date (dd-mm-yyyy): ")
    address = input("Enter the address (street, number - neighborhood - city/state): ")

    users.append({"name": name, "birth_date": birth_date, "cpf": cpf, "address": address})

    print("=== User created successfully! ===")


def filter_user(cpf, users):
    """
    Filters users based on their CPF.

    Parameters:
    cpf (str): The CPF to be used for filtering.
    users (list): The list of users to be filtered.

    Returns:
    dict or None: The user with the matching CPF, or None if no match is found.
    """
    filtered_users = [user for user in users if user["cpf"] == cpf]
    return filtered_users[0] if filtered_users else None


def create_account(agency, account_number, users):
    """
    Creates a new account associated with a user.

    Parameters:
    agency (str): The agency number for the account.
    account_number (int): The account number.
    users (list): The list of users to search for the associated user.

    Returns:
    dict or None: A dictionary containing the account information and associated user, or None if the user is not found.
    """
    cpf = input("Enter the user's CPF: ")
    user = filter_user(cpf, users)

    if user:
        print("\n=== Account created successfully! ===")
        return {"agencia": agency, "numero_conta": account_number, "usuario": user}

    print("\n@@@ User not found, account creation process terminated! @@@")


def list_accounts(accounts):
    """
    Lists information about the accounts.

    Parameters:
    accounts (list): The list of accounts to be listed.

    Returns:
    None
    """
    for account in accounts:
        line = f"""\
            Agency:\t{account['agencia']}
            Account:\t{account['numero_conta']}
            Holder:\t{account['usuario']['nome']}
        """
        print("=" * 100)
        print(textwrap.dedent(line))


def main():
    """
    Main function to control the banking operations and menu options.

    Parameters:
    None

    Returns:
    None
    """
    WITHDRAWS_LIMIT = 3
    AGENCY = "0001"

    balance = 0
    limit = 500
    extract = ""
    withdraws_number = 0
    users = []
    accounts = []

    while True:
        option = menu()

        if option == "d":
            amount = float(input("Informe o valor do depósito: "))

            balance, extract = deposit(balance, amount, extract)

        elif option == "s":
            amount = float(input("Informe o valor do saque: "))

            balance, extract = withdraw(
                balance=balance,
                amount=amount,
                extract=extract,
                limit=limit,
                number_withdraws=withdraws_number,
                limit_withdraws=WITHDRAWS_LIMIT,
            )

        elif option == "e":
            print_extract(balance, extract=extract)

        elif option == "nu":
            create_user(users)

        elif option == "nc":
            account_number = len(accounts) + 1
            account = create_account(AGENCY, account_number, users)

            if account:
                accounts.append(account)

        elif option == "lc":
            list_accounts(accounts)

        elif option == "q":
            break

        else:
            print("Operação inválida, por favor selecione novamente a operação desejada.")


main()
