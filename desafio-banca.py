menu = """
[d] Depositar
[s] Sacar
[e] Extrato
[c] Crédito
[q] Sair

=> """

saldo = 0
limite = 500
extrato = ""
credito = 0  # Inicializando a variável de crédito
numero_saques = 0
LIMITE_SAQUES = 3
depositos = 0  # Contador de depósitos

while True:

    opcao = input(menu)

    if opcao == "d":
        valor = float(input("Informe o valor do depósito: "))

        if valor > 0:
            saldo += valor
            extrato += f"Depósito: R$ {valor:.2f}\n"
            credito += 1  # Aumentando o crédito a cada depósito
            depositos += 1  # Contando os depósitos

            if depositos == 10:  # Quando ocorrerem 10 depósitos
                incremento = sum(map(float, extrato.split()[2::3])) * 0.3  # Incremento de 30%
                credito += incremento  # Adicionando o incremento ao crédito
                depositos = 0  # Resetando o contador de depósitos

            else:
                incremento = sum(map(float, extrato.split()[2::3])) * 0.03  # Incremento de 3%
                credito += incremento  # Adicionando o incremento ao crédito

        else:
            print("Operação falhou! O valor informado é inválido.")

    elif opcao == "s":
        valor = float(input("Informe o valor do saque: "))

        excedeu_saldo = valor > saldo
        excedeu_limite = valor > limite
        excede_saques = numero_saques >= LIMITE_SAQUES

        if excedeu_saldo:
            print("Operação falhou! Você não tem saldo suficiente.")

        elif excedeu_limite:
            print("Operação falhou! O valor do saque excede o limite.")

        elif valor > 0:
            saldo -= valor
            extrato += f"Saque: R$ {valor:.2f}\n"
            numero_saques += 1

        else:
            print("Operação falhou! O valor informado é inválido.")

    elif opcao == "e":
        print("\n================ EXTRATO ================")
        print("Não foram realizadas movimentações." if not extrato else extrato)
        print(f"\nSaldo: R$ {saldo+credito:.2f}")
        print("=========================================")

    elif opcao == "c":
        print(f"Crédito: {credito:.2f}")  # Mostrando o crédito atual

    elif opcao == "q":
        break

    else:
        print("Operação inválida, por favor selecione novamente a operação desejada.")
