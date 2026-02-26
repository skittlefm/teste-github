import sql_funcoes as sf
import os

NOMEDB = "agenda.db"
NOMETABELA = "Clientes"
# MENU PRINCIPAL
def menuPrincipal():
    os.system("cls")
    print("1 - Inserir Novo Registro")
    print("2 - Atualizar Registro")
    print("3 - Apagar Registro")
    print("4 - Consultar Todos os Registros")
    print("5 - Consultar Registro por ID")
    print("6 - Sair")

def menuInserir():
    os.system("cls")
    print("MENU INSERIR UM NOVO REGISTRO")
    nome = input("Digite seu nome: ")
    sobrenome = input("Digite o sobrenome: ")
    email = input("Digite o email: ")

    sf.inseriDados(NOMEDB, NOMETABELA, nome, sobrenome, email)

    print("Registro Inserido com Sucesso")
    os.system("pause")

def menuAtualizar():
    os.system("cls")
    print("MENU ATUALIZAR UM REGISTRO")
    print("Digite o campo desejado ou aperte ENTER para continuar")
    nome = input("Digite seu nome: ")
    sobrenome = input("Digite o sobrenome: ")
    email = input("Digite o email: ")
    numRegistro = input("Digite o número do registro: ")

    sf.atualizarDados(NOMEDB, NOMETABELA, nome, sobrenome, email, numRegistro)

    print("Registro Atualizado com Sucesso")
    os.system("pause")

def menuApagar():
    os.system("cls")
    print("MENU APAGAR UM REGISTRO")

    numRegistro =  input("Digite o número do registro : ")

    os.system("cls")
    confirmar = input("Digite SIM para confirmar: ")

    if confirmar.lower() == "sim":
        sf.apagarDado(NOMEDB, NOMETABELA, numRegistro)
        print("Registro Apagado com Sucesso")
    else:
        print("Operação Cancelada")
    os.system("pause")

def menuSelecionarTodos():
    os.system("cls")
    print("MENU SELECIONAR TODOS OS REGISTROS")

    dados = sf.selecionarTodosDados(NOMEDB, NOMETABELA)

    print(f"{'ID':<5} | {'NOME':>20} | {'SOBRENOME':>20} | {'EMAIL':>20}")
    for dado in dados:
        print(f"{dado[0]:<5} | {dado[1]:>20} | {dado[2]:>20} | {dado[3]:>20}")

    os.system("pause")

def menuSelecionarPorId():
    os.system("cls")
    print("MENU SELECIONAR REGISTRO POR ID")

    numRegistro = input("Digite o número do registro: ")

    dados = sf.selecionarDadoPorId(NOMEDB, NOMETABELA, numRegistro)

    print(f"{'ID':<5} | {'NOME':>20} | {'SOBRENOME':>20} | {'EMAIL':>20}")
    
    for dado in dados:
        print(f"{dado[0]:<5} | {dado[1]:>20} | {dado[2]:>20} | {dado[3]:>20}")

    os.system("pause")

def main():
    
    sf.criarTabela(NOMEDB, NOMETABELA)

    opcao = 0

    while opcao != 6:

        menuPrincipal()
        opcao = int(input("Digite a opção desejada: "))

        if opcao == 1:
            menuInserir()
        elif opcao == 2:
            menuAtualizar()
        elif opcao == 3:
            menuApagar()
        elif opcao == 4:
            menuSelecionarTodos()
        elif opcao == 5:
            menuSelecionarPorId()
        elif opcao == 6:
            os.system("cls")
            print("Programa Encerrado")
        else:
            os.system("cls")
            print("Opção Inválida")
            os.system("pause")

if __name__ == "__main__":
    main()