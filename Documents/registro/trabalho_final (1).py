#Trabalho final de algoritmos
#Alunos: Arthur Daniel Pereira da Silva, Filipe Braga de Menezes.
#O código tem 4 funções principais, novos registros, menu, excluir um registro e executar o sistema, sendo esse(executar_sistema) um loop
lista_de_carros = []
total_de_registro = 0 
limite_registros = 2
print("Sistemas de registro de automóveis")
print("É possível adicionar as seguintes categorias na lista\n Modelo do carro, Marca do carro e Ano do carro")
print('-' * 50)

# Função para inserir um novo registro
def novoregistro():
    modelo = str(input("Qual o modelo do carro?: "))
    marca = str(input("Qual a marca do carro?: "))
    cor = str(input("Qual a cor do carro?: "))
    ano = int(input("Qual o ano do carro?: "))
    motor = str(input("Qual o tipo de motor (1.0, 1.5, 2.0, etc.)?: "))
    quilometragem = str(input("Qual a quilometragem?: "))
    chaves = {"modelo": modelo, "marca": marca, "ano": ano, "motor": motor, "quilometragem": quilometragem, "cor": cor}
    lista_de_carros.append(chaves)
    print("Carro registrado com sucesso!")

# Função para excluir um registro
def excluir_registro():
    global total_de_registro
    if not lista_de_carros:
        print("Não há carros para excluir.")
        return
    
    for i, carro in enumerate(lista_de_carros):
        print(f'Registro {i+1}: Modelo: {carro["modelo"]}, Marca: {carro["marca"]}, Ano: {carro["ano"]}, Motor: {carro["motor"]}, Quilometragem: {carro["quilometragem"]}, cor: {carro["cor"]}')
    
    indice = int(input("Digite o número do registro que deseja excluir: ")) - 1
    if 0 <= indice < len(lista_de_carros):
        del lista_de_carros[indice]
        total_de_registro = total_de_registro - 1
        print("Registro excluído com sucesso!")
    else:
        print("Índice inválido. Nenhum registro foi excluído.")

# Função para exibir o menu
def menu():
    print("Menu inicial")
    print("1- Inserir novo carro")
    print("2- Imprimir todos os carros existentes")
    print("3- Imprimir um trecho dos carros registrados")
    print("4- Busque um carro")
    print("5- Busque um carro por modelo")
    print("6- Busque um carro pelo ano")
    print("7- Busque um carro pela cor")
    print("8- Excluir um carro")
    print("9- Sair")

# Loop principal
def executar_sistema():
    global total_de_registro
    decisao = 0  # Variável de controle para continuar o loop
    
    while decisao != 9:  # O sistema continua até o usuário escolher a opção de sair
        menu()
        decisao = int(input("Selecione uma opção do menu: "))
        
        # Inserir novo registro
        if decisao == 1:
            if total_de_registro < limite_registros:
                novoregistro()
                total_de_registro += 1
                print(f'Total de registros: {total_de_registro}')
                
                # Verifica se o usuário deseja adicionar mais um registro
                while total_de_registro < limite_registros:
                    novo_registro = input("Você deseja inserir mais um registro? Digite S para sim e N para não (S/N) ").strip().upper()
                    if novo_registro == 'S':
                        novoregistro()
                        total_de_registro += 1
                        print(f'Total de registros: {total_de_registro}')
                    elif novo_registro == 'N':
                        break
                    else:
                        print("Resposta inválida. Digite S para Sim ou N para Não.")
            else:
                print("Limite de registro de carros atingido, exclua um carro antes de adicionar um novo.")
          # Imprimir todos os registros
        elif decisao == 2:
            if lista_de_carros:
                for i, carro in enumerate(lista_de_carros):
                    print(f'Registro {i+1}: Modelo: {carro["modelo"]}, Marca: {carro["marca"]}, Ano: {carro["ano"]}, Motor {carro["motor"]}, Kilometragem: {carro["quilometragem"]}, cor: {carro["cor"]}')
            else:
                print("Não há registros para exibir.")

        # Imprimir um trecho dos registros
        elif decisao == 3:
            inicio = int(input("Qual o índice inicial? ")) - 1
            final = int(input("Qual o índice final? "))
            if 0 <= inicio < final <= len(lista_de_carros):
                for i in range(inicio, final):
                    carro = lista_de_carros[i]
                    print(f'Registro {i+1}: Modelo: {carro["modelo"]}, Marca: {carro["marca"]}, Ano: {carro["ano"]}, Motor: {carro["motor"]}, Kilometragem: {carro["quilometragem"]}, cor: {carro["cor"]}')
                    print("-" * 20)
            else:
                print("Índices inválidos.")
        
        # Buscar um registro por modelo
        elif decisao == 4:
            modelo_busca = input("Digite o modelo do carro que deseja buscar: ").strip().lower()
            encontrados = []
            for carro in lista_de_carros:
                if carro["modelo"].lower() == modelo_busca:
                    encontrados.append(carro)
            
            if encontrados:
                for i, carro in enumerate(encontrados):
                    print(f'Modelo: {carro["modelo"]}, Marca: {carro["marca"]}, Ano: {carro["ano"]}, Motor:{carro["motor"]}, Kilometragem: {carro["quilometragem"]}, cor: {carro["cor"]}')
            else:
                print("Nenhum carro encontrado com esse modelo.")
        elif decisao == 5:
            marca_busca = input("Digite a marca do carro que deseja buscar: ").strip().lower()
            carros_encontrados = []
            for carro in lista_de_carros:
                if carro["marca"].lower() == marca_busca:
                    carros_encontrados.append(carro)
            
            if carros_encontrados:
                print(f"\nCarros da marca '{marca_busca.capitalize()}':")
                for i, carro in enumerate(carros_encontrados):
                    print(f'{i+1}: Modelo: {carro["modelo"]}, Ano: {carro["ano"]}, Motor:{carro["motor"]}, Kilometragem: {carro["quilometragem"]}, cor: {carro["cor"]}')
            else:
                print(f"Nenhum carro encontrado da marca '{marca_busca}'.")
        elif decisao == 6:
            ano_busca = int(input("Digite o ano do carro que você deseja buscar: "))
            carros_achados = []
            for carro in lista_de_carros:
                if carro["ano"]==ano_busca:
                    carros_achados.append(carro)
            if carros_achados: 
                print(f"\nCarros da ano '{ano_busca}':")
                for i, carro in enumerate(carros_achados):
                    print(f'{i+1}: Modelo: {carro["modelo"]}, Ano: {carro["ano"]}, Motor:{carro["motor"]}, Kilometragem: {carro["quilometragem"]}, cor: {carro["cor"]}')
            else:
                print("Nenhum carro encontrado desse ano.")
        elif decisao == 7:
            cor_busca = input("Digite a cor do carro que deseja buscar: ").strip().lower()
            carros_achaduskk = []
            for carro in lista_de_carros:
                if carro["cor"].lower()==cor_busca:
                    carros_achaduskk.append(carro)
            if carros_achaduskk:
                print(f"\nCarros da cor '{cor_busca.capitalize()}':")
                for i, carro in enumerate(carros_achaduskk):
                    print(f'{i+1}: Modelo: {carro["modelo"]}, Ano: {carro["ano"]}, Motor:{carro["motor"]}, Kilometragem: {carro["quilometragem"]}, cor: {carro["cor"]}')
            else:
                print("Nenhum carro foi encontrado com essa cor")
        
        #Excluir um carro
        elif decisao == 8:
            excluir_registro()

        elif decisao == 9:
            print("Encerrando o programa...")
            break
        
        else:
            print("Opção inválida, tente novamente.")

# Executa o sistema de cadastro
executar_sistema()