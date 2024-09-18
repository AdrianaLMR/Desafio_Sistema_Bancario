# Definição dos menus
menu_principal = """
[d] Depositar 
[s] Sacar 
[e] Extrato
[b] Bloquear Conta
[m] Empréstimo 
[q] Sair

=> """

menu_bloqueio_conta = """
Escolha a opção:
[1] Bloquear conta
[2] Desbloquear conta 
[3] Voltar ao menu principal
"""

menu_emprestimo = """
Escolha a opção de empréstimo:
[1] Solicitar empréstimo (limite R$ 500)
[2] Pagar empréstimo
[3] Voltar ao menu principal
"""

menu_parcelas_emprestimo = """
Escolha o número de parcelas:
[1] A vista (sem juros)
[2] 2 parcelas (2% de juros)
[3] 3 parcelas (2% + juros por atraso)
[4] Voltar ao menu anterior
"""

menu_pagamentos_parcelas = """
Escolha o número de parcelas a serem pagas:
[1] Pagar 1 parcela
[2] Pagar 2 parcelas
[3] Pagar 3 parcelas
[4] Voltar ao menu anterior
"""

# Variáveis iniciais
saldo = 0
limite = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3
conta_bloqueada = False
senha_desbloqueio = None
emprestimo_solicitado = False
valor_emprestimo = 0
parcelas = 0
parcelas_pagas = 0
sair_programa = False  # Variável de controle para sair do programa

# Função para exibir o extrato
def exibir_extrato():
    print("\n================ EXTRATO ================")
    print("Não foram realizadas movimentações." if not extrato else extrato)
    if emprestimo_solicitado:
        print(f"Empréstimo solicitado: R$ {valor_emprestimo:.2f}")
        print(f"Parcelas pagas: {parcelas_pagas} de {parcelas}")
    print(f"\nSaldo: R$ {saldo:.2f}")
    print("==========================================")

while not sair_programa:
    if conta_bloqueada:
        menu_atual = menu_bloqueio_conta
    else:
        menu_atual = menu_principal

    while True:
        opcao = input(menu_atual)

        if menu_atual == menu_principal:
            if opcao == "d":
                if conta_bloqueada:
                    print("Operação falhou! A conta está bloqueada.")
                else:
                    valor = float(input("Informe o valor do depósito: "))
                    if valor > 0:
                        saldo += valor
                        extrato += f"Depósito: R$ {valor:.2f}\n"
                    else:
                        print("Operação falhou! O valor informado é inválido.")
            
            elif opcao == "s":
                if conta_bloqueada:
                    print("Operação falhou! A conta está bloqueada.")
                else:
                    valor = float(input("Informe o valor do saque: "))
                    excedeu_saldo = valor > saldo
                    excedeu_limite = valor > limite
                    excedeu_saques = numero_saques >= LIMITE_SAQUES

                    if excedeu_saldo:
                        print("Operação falhou! Você não tem saldo suficiente.")
                    elif excedeu_limite:
                        print("Operação falhou! O valor do saque excede o limite.")
                    elif excedeu_saques:
                        print("Operação falhou! Número máximo de saques excedido.")
                    elif valor > 0:
                        saldo -= valor
                        extrato += f"Saque: R$ {valor:.2f}\n"
                        numero_saques += 1
                    else:
                        print("Operação falhou! O valor informado é inválido.")

            elif opcao == "e":
                exibir_extrato()

            elif opcao == "b":
                while True:
                    escolha_bloqueio = input(menu_bloqueio_conta)

                    if escolha_bloqueio == "1":
                        if conta_bloqueada:
                            print("A conta já está bloqueada.")
                        else:
                            senha_desbloqueio = input("Crie uma senha de desbloqueio: ")
                            conta_bloqueada = True
                            print("Conta bloqueada com sucesso.")
                            break
                    elif escolha_bloqueio == "2":
                        if conta_bloqueada:
                            senha = input("Insira a senha de desbloqueio: ")
                            if senha == senha_desbloqueio:
                                conta_bloqueada = False
                                print("Conta desbloqueada com sucesso.")
                            else:
                                print("Senha incorreta. Não foi possível desbloquear a conta.")
                            break
                        else:
                            print("A conta já está desbloqueada.")
                            break
                    elif escolha_bloqueio == "3":
                        break
                    else:
                        print("Opção inválida. Tente novamente.")
                continue  # Volta para o menu principal

            elif opcao == "m":
                if conta_bloqueada:
                    print("Operação falhou! A conta está bloqueada.")
                else:
                    while True:
                        escolha_emprestimo = input(menu_emprestimo)

                        if escolha_emprestimo == "1":
                            if emprestimo_solicitado:
                                print("Você já tem um empréstimo ativo.")
                            else:
                                valor_emprestimo = float(input("Informe o valor do empréstimo (limite de R$ 500): "))
                                if valor_emprestimo <= 500:
                                    while True:
                                        parcelas_opcao = input(menu_parcelas_emprestimo)
                                        if parcelas_opcao == "1":
                                            parcelas = 1
                                            break
                                        elif parcelas_opcao == "2":
                                            parcelas = 2
                                            break
                                        elif parcelas_opcao == "3":
                                            parcelas = 3
                                            break
                                        elif parcelas_opcao == "4":
                                            break
                                        else:
                                            print("Opção inválida. Tente novamente.")
                                    if parcelas > 0:
                                        emprestimo_solicitado = True
                                        parcelas_pagas = 0  # Reset parcelas pagas ao solicitar um novo empréstimo
                                        print("Empréstimo solicitado com sucesso.")
                                    else:
                                        print("Número de parcelas não selecionado corretamente.")
                                else:
                                    print("Valor do empréstimo excede o limite.")
                        elif escolha_emprestimo == "2":
                            if not emprestimo_solicitado:
                                print("Não há empréstimos pendentes.")
                            else:
                                while True:
                                    escolha_pagamento = input(menu_pagamentos_parcelas)
                                    if escolha_pagamento == "1":
                                        parcelas_a_pagar = 1
                                    elif escolha_pagamento == "2":
                                        parcelas_a_pagar = 2
                                    elif escolha_pagamento == "3":
                                        parcelas_a_pagar = 3
                                    elif escolha_pagamento == "4":
                                        break  # Voltar ao menu anterior
                                    else:
                                        print("Opção inválida. Tente novamente.")
                                        continue

                                    print(f"Saldo atual: R$ {saldo:.2f}")  # Exibe o saldo antes do pagamento

                                    if parcelas_pagas + parcelas_a_pagar <= parcelas:
                                        valor_parcela = valor_emprestimo / parcelas
                                        saldo -= valor_parcela * parcelas_a_pagar
                                        parcelas_pagas += parcelas_a_pagar
                                        if parcelas_pagas >= parcelas:
                                            emprestimo_solicitado = False
                                            valor_emprestimo = 0
                                            parcelas = 0
                                            print("Empréstimo pago integralmente.")
                                        else:
                                            print(f"{parcelas_a_pagar} parcelas pagas. Restam {parcelas - parcelas_pagas}.")
                                        break
                                    else:
                                        print("Número de parcelas a pagar excede o total de parcelas restantes.")
                        elif escolha_emprestimo == "3":
                            break  # Voltar ao menu principal
                        else:
                            print("Opção inválida. Tente novamente.")
                continue  # Volta para o menu principal

            elif opcao == "q":
                print("Saindo do sistema. Até logo!")
                sair_programa = True
                break

            else:
                print("Operação inválida, por favor selecione novamente a operação desejada.")
                continue
