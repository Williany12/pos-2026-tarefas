import users_wrapper as a

opcao_valida = True

while opcao_valida:

    print("1 - Listar usuários")
    print("2 - Detalhar usuário")
    print("3 - Criar usuário")
    print("4 - Atualizar usuário")
    print("5 - Deletar usuário")
    print("0 - Sair")
    print("-/"*20)
    opcao = input("Digite a opção desejada: ")

    if opcao == "0":
        break


    elif opcao == "1":

        users = a.listar_usuarios()

        if users:

            print("\n USUÁRIOS ")

            for user in users:
                print(f"{user['id']} - {user['name']}")
            print("-/"*20)
        else:
            print("Erro")
    
    elif opcao == "2":

        id = input("Digite o ID do usuário: ")
        user = a.detalhar_usuario(id)

        if user:
            print(f"ID: {user['id']}")
            print(f"Nome: {user['name']}")
            print(f"Username: {user['username']}")
            print(f"Email: {user['email']}")
            print(f"Telefone: {user['phone']}")
            print(f"Website: {user['website']}")
            print("-/"*20)
        else:
            print("Não foi possivel encontrar o usuário")
    
    elif opcao == "3":

        dados = {
            "name": input("Nome: "),
            "username": input("Username: "),
            "email": input("Email: "),
            "phone": input("Telefone: "),
            "website": input("Website: ")}
        
        user = a.criar_usuario(dados)

        if user:
            print("\nUsuário criado!")

        else:
            print("Erro ao criar!")



    elif opcao == "4":

        id = input("Digite o ID do usuário: ")

        dados = {
                "name": input(" Nome: "),
                "username": input("Username: "),
                "email": input("Email: "),
                "phone": input("Telefone: "),
                "website": input("Website: "),}
        print("-/"*20)
        user = a.editar_usuario(id,dados)

        if user:
            print("\nUsuário atualizado!")

        else:
            print("Erro ao atualizar!")
        
    elif opcao == "5":

        id = input("Digite o ID do usuário: ")

        resultado = a.deletar_usuario(id)

        if resultado:
            print("Usuário deletado!")

        else:
            print("Erro ao deletar!")



    else:
        print("opção inválida, digite um número válido!")