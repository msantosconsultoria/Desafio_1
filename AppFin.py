class ContaBancaria:
    def __init__(self, saldo_inicial=0):
        self.saldo = saldo_inicial
        self.transacoes = []
        self.saques_hoje = 0

    def depositar(self, valor):
        if valor > 0:
            self.saldo += valor
            self.transacoes.append(f"Depósito: +R$ {valor:.2f}")
            print(f"\nDepósito de R$ {valor:.2f} realizado com sucesso!")
        else:
            print("\nO valor do depósito deve ser positivo.")

    def sacar(self, valor):
        if self.saques_hoje >= 3:
            print("\nLimite de saques diários atingido.")
            return

        if valor <= 0:
            print("\nO valor do saque deve ser positivo.")
            return

        if valor > 500:
            print("\nO valor máximo de saque por transação é R$ 500,00.")
            return

        if valor > self.saldo:
            print("\nSaldo insuficiente para realizar o saque.")
            return

        self.saldo -= valor
        self.transacoes.append(f"Saque: -R$ {valor:.2f}")
        self.saques_hoje += 1
        print(f"Saque de R$ {valor:.2f} realizado com sucesso!")

    def extrato(self):
        print("\nExtrato de transações:")
        for transacao in self.transacoes:
            print(transacao)
        print(f"Saldo atual: R$ {self.saldo:.2f}\n")

    def painel(self):
        while True:
            #print("\n##################################################")
            print("\n######## Painel de Operações Bancárias ###########")
            print("\nDigite 'd' para Depósito")
            print("Digite 's' para Saque")
            print("Digite 'e' para Exibir Extrato")
            print("Digite 'q' para Sair")
            opcao = input("\nEscolha uma operação: ").lower()
            #print("\n##################################################")

            if opcao == 'd':
                valor = float(input("\nDigite o valor a ser depositado: R$ "))
                self.depositar(valor)
            elif opcao == 's':
                valor = float(input("\nDigite o valor a ser sacado: R$ "))
                self.sacar(valor)
            elif opcao == 'e':
                self.extrato()
            elif opcao == 'q':
                print("\nObrigado por usar nosso sistema bancário.")
                #print("\n##################################################")
                break
            else:
                print("\nOpção inválida, por favor escolha novamente.")
            #print("\n##################################################")

# Exemplo de uso
conta = ContaBancaria(1000)  # Inicializando a conta com saldo inicial de 1000
conta.painel()               # Iniciando o painel de operações
