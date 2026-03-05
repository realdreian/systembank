def cadastro_usuario():
    nome = input("Digite seu nome completo: ")
    cpf = input("Digite seu CPF (APENAS NUMEROS: )")
    nasc = input("Digite sua data de nascimento: ")

    if len(cpf) != 11:
        print("CPF INVALIDO")
        return 'cpf invalido'
    else:
        conta = {
            "nome": nome,
            "cpf": cpf,
            "data de nascimento": nasc,
            "saldo": 0,
            "historico": []
}        
        return conta

def menu_opcoes():
    print("=== MENU DE OPÇÔES === \n")
    print("[1] Depositar \n")
    print("[2] Sacar \n")
    print("[3] Verificar Saldo \n")
    print("[4] Verificar Extrato \n")
    print("[5] Sair \n")

def deposito(conta):
    valor = input("Digite o valor a Deposritar: R$ ")
    if not valor.isdigit():
        print("Valor inválido! Digite apenas números inteiros")
        return
    
    valor_int = int(valor)

    if valor_int <= 0:
        print("Valor do depósito deve ser maior que R$ 0")
        return
    conta['saldo'] += valor_int

    conta['historico'].append(f"Depósito R$ {valor_int}")
    print("Depósito Realizado com Sucesso")

def verificar_saldo(conta):
    print(f"Saldo Atual R$ {conta['saldo']}")



              