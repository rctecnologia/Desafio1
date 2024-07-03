import os

menu = """
Escolha a opção desejada
[d] Depositar
[s] Sacar
[e] Extrato
[q] Sair

=>"""

extrato = ""
limite = 500
saldo = 0
numero_saques = 0
LIMITE_SAQUES = 3

while True:
    opcao = input(menu)

    if opcao == "d":
        os.system('cls')
        valor = float(input("Digite o valor a ser depositado: "))

        if valor > 0:
            saldo += valor
            extrato += f"Deposito: R$ {valor:.2f}\n"
            print(f"\n==> R$ {valor:.2f} Depositado com sucesso. Digite <ENTER> para continuar.")
            s = input()
            os.system('cls')
        else:
            print("Valor inválido.")
            s = input()
            os.system('cls')

    elif opcao == "s":
        os.system('cls')
        excedeu_saques = numero_saques >= LIMITE_SAQUES
        valor = float(input("Digite o valor a ser sacado: "))
        excedeu_saldo = valor > saldo
        excedeu_limite = valor > limite


        if excedeu_saldo:
            print("Saldo insuficiente, Digite <ENTER> para continuar.")
            s = input()
            os.system('cls')

        elif excedeu_limite:
            print("O valor solicitado excede o limite, Digite <ENTER> para continuar.")
            s = input()
            os.system('cls')

        elif excedeu_saques:
            print("Limite de Saques atingido, Digite <ENTER> para continuar.")
            s = input()
            os.system('cls')

        elif valor > 0:
            saldo -= valor
            numero_saques += 1
            extrato += f"Saque: R$ {valor:.2f}\n"
            print(f"\n==> R$ {valor:.2f} Sacado com sucesso. Digite <ENTER> para continuar.")
            s = input()
            os.system('cls')

        else:
            print("Valor informado é inválido")

    elif opcao == "e":
        os.system('cls')
        print("\n================EXTRATO================")
        print("Não foram localizadas movimentações." if not extrato else extrato)
        print(f"\nSeu Saldo é de R$ {saldo:.2f}")
        print("=========================================")
        print(f"\nDigite <ENTER> para continuar.")
        s = input()
        os.system('cls')

    elif opcao == "q":
        break

    else:
        print("Opção Inválida, Selecione uma das opções apresentadas.")
