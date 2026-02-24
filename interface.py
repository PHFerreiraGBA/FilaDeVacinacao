from fila import Fila
from pilha import Pilha

def adicionaPaciente(filaPacientes):
    if filaPacientes.contaItensFila() < 15:
        nome = input("\nNome da pessoa: ")
        cpf = input("CPF da pessoa: ")
        print("")
        filaPacientes.addElemento([nome, cpf])
    else:
        print("\nNão é possível adicionar pacientes agora.\nA fila está cheia. Tente novamente em outra hora.")

def imprimePacientes(filaPacientes):
    print("")

    aux = filaPacientes.primeiro
    if(aux != None):
        contadorPacientes = 1
        while(aux != None):
            print(f"\nPaciente {contadorPacientes}")
            print(f"Nome: {aux.valor[0]}\nCPF: {aux.valor[1]}\n")
            aux = aux.proximo
            contadorPacientes += 1
    else:
        print("--- Fila Vazia ---")
    
    print("")

def contaDoses(pilhaVacinas):
    aux = pilhaVacinas.primeiro
    if(aux != None):
        contadorDoses = 0
        while(aux != None):
            contadorDoses += aux.valor
            aux = aux.proximo
        return contadorDoses
    else:
        return 0

def imprimeVacinas(pilhaVacinas):
    print("")

    aux = pilhaVacinas.primeiro
    if(aux != None):
        contadorDoses = 0
        while(aux != None):
            contadorDoses += aux.valor
            aux = aux.proximo
        print(f"{contadorDoses} doses disponíveis.")
    else:
        print("--- Sem doses disponíveis ---")
    
    print("")

vacinados = []

def vacinarPessoa(pilhaVacinas, filaPacientes):
    print("Pessoa Vacinada:")
    print(f"Nome: {filaPacientes.primeiro.valor[0]}")
    print(f"CPF: {filaPacientes.primeiro.valor[1]}")

    if pilhaVacinas.ultimo.valor > 1:
        pilhaVacinas.ultimo.valor -= 1
    else:
        pilhaVacinas.removeElemento()
    
    print(f"{15-contaDoses(pilhaVacinas)}ª dose aplicada.")
    vacinados.append(filaPacientes.primeiro.valor)
    filaPacientes.removeElemento()

vacinas = Pilha()
pacientes = Fila()
sair = False

for i in range(0, 3):
    vacinas.addElemento(5)

while sair == False:
    print("Selecione uma opção digitando um dos números:")

    stringOpcoes = "\n0 - Sair do programa\n1 - Adicionar pessoa\n2 - Imprimir Pessoas da Fila\n3 - Imprimir quantas doses tem disponíveis\n4 - Vacinar uma pessoa\n5 - Exibir total de vacinados"

    opcao = input(stringOpcoes + "\n\nEscolha sua opção: ")

    if opcao == "0":
        sair = True
    elif opcao == "1":
        adicionaPaciente(pacientes)
    elif opcao == "2":
        imprimePacientes(pacientes)
    elif opcao == "3":
        imprimeVacinas(vacinas)
    elif opcao == "4":
        if pacientes.primeiro != None and vacinas.primeiro != None:
            vacinarPessoa(vacinas, pacientes)
        else:
            print("")
            if pacientes.primeiro == None:
                print("Não há pacientes para vacinar.")
            if vacinas.primeiro == None:
                print("Não há doses para aplicar.")
            print("Portanto, não podemos aplicar vacina agora.\n")
    elif opcao == "5":
        if vacinados == []:
            print("Nenhuma pessoa vacinada.")
        else:
            print(f"{len(vacinados)} pessoas vacinadas.")
    else:
        print("\nDesculpe, mas essa opção não está disponível.\nTente de novo com uma válida.\n")