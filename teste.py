def cadastro_devs():
    print("Cadastro de desenvolvedores")
    nome = input("Digite seu nome: ")
    apelido = input("Digite seu apelido: ")
    ids = int(input("Digite seu ID (apenas números): "))
    ativo = False  # Alterado para booleano para simplicidade

    def ja_cadastrado():
        nonlocal nome, apelido, ids, ativo

        if nome == "Vinicius dos Santos Pereira":
            pass

        if apelido in ["Tanmo", "Vnzin", "Hood"]:
            print("Apelido já cadastrado. Por favor, escolha outro.")
            apelido = input("Digite seu apelido novamente: ")
            ativo = True

        if nome == apelido:
            print("O nome e o apelido são iguais.")
            nome = input("Digite seu nome novamente: ")
            apelido = input("Digite seu apelido novamente: ")

        if ids in [3225, 4041]:
            ativo = True
            print("ID já cadastrado!!")
            ids = int(input("Digite seu ID novamente: "))

    ja_cadastrado()
    print("__________________________________________________")
    print(nome)
    print(apelido)
    print(ids)

    print("__________________________________________________")
    print("Agora vamos confirmar que você é humano jogando este jogo.")

    def jogo():
        print("Nas alternativas corretas, coloque V; nas erradas, coloque F.")
        print("Espero que você seja humano...")
        print("__________________________________________________")
        pergunta1 = input("35 + 30 = 65? (V/F): ").upper()
        pergunta2 = input("A letra 'A' é uma vogal? (V/F): ").upper()
        ativacao = 0
        robo = 0
        verify = "nao"

        if pergunta1 == "V":
            print("Quase lá...")
            print("__________________________________________________")
            ativacao += 1
        else:
            print("Será que você é um robô...")
            print("__________________________________________________")
            robo += 1

        if pergunta2 == "V":
            print("Quase lá...")
            print("__________________________________________________")
            ativacao += 1
        else:
            print("Você errou, será que você é um robô...")
            print("__________________________________________________")
            robo += 1

        if ativacao == 2:
            print("Pronto, verificamos que você é um humano. Sua conta vai ser criada...")
            print("__________________________________________________")
            verify = "verificado"

        if robo == 2:
            print("-_- Você é um robô... se não verifique mais uma vez.")

        if verify == "verificado":
            print("__________________________________________________")
            print("Sua conta foi criada. Aproveite!")

    jogo()

cadastro_devs()
