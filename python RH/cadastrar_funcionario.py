from conexao import conectar

def cadastrar_funcionario():
    print("\n📋 Cadastro de Funcionário")

    # Coleta de dados via terminal
    nome = input("Nome completo: ")
    cpf = input("CPF (formato 000.000.000-00): ")
    email = input("E-mail: ")
    telefone = input("Telefone: ")
    endereco = input("Endereço: ")
    data_admissao = input("Data de admissão (YYYY-MM-DD): ")
    cargo_id = input("ID do cargo: ")

    # Conecta ao banco
    conexao = conectar()
    if conexao is None:
        print("❌ Não foi possível conectar ao banco.")
        return

    try:
        cursor = conexao.cursor()

        # Comando SQL para inserir funcionário
        sql = """
            INSERT INTO funcionarios (nome, cpf, email, telefone, endereco, data_admissao, cargo_id)
            VALUES (%s, %s, %s, %s, %s, %s, %s)
        """
        valores = (nome, cpf, email, telefone, endereco, data_admissao, cargo_id)

        cursor.execute(sql, valores)
        conexao.commit()
        print("✅ Funcionário cadastrado com sucesso!")

    except Exception as erro:
        print("❌ Erro ao cadastrar funcionário:")
        print(erro)

    finally:
        cursor.close()
        conexao.close()
