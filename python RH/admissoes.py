from conexao import conectar

def registrar_movimentacao():
    print("\n Registro de Movimentação de Funcionário")

    funcionario_id = input("ID do funcionário: ")
    horario = input("Data do evento (YYYY-MM-DD): ")
    print("Tipo de movimentação:")
    print("1 - Admissão")
    print("2 - Demissão")
    print("3 - Transferência")
    tipo_opcao = input("Escolha o tipo (1/2/3): ")

    tipos = {
        "1": "Admissão",
        "2": "Demissão",
        "3": "Transferência"
    }

    tipo = tipos.get(tipo_opcao)
    if not tipo:
        print(" Tipo inválido.")
        return

    observacoes = input("Observações (opcional): ")

    conexao = conectar()
    if conexao is None:
        print(" Não foi possível conectar ao banco.")
        return

    try:
        cursor = conexao.cursor()
        sql = """
            INSERT INTO admissoes (funcionario_id, horario, tipo, observacoes)
            VALUES (%s, %s, %s, %s)
        """
        valores = (funcionario_id, horario, tipo, observacoes)
        cursor.execute(sql, valores)
        conexao.commit()
        print(f" {tipo} registrada com sucesso!")

    except Exception as erro:

from registrar_admissao import registrar_movimentacao

# Adicione ao menu:
print("3 - Registrar Admissão/Demissão/Transferência")

# E no if:
elif opcao == "3":
    registrar_movimentacao()

