import mysql.connector


def conectar():
    try:
        
        conexao = mysql.connector.connect(
            host='localhost',        
            user='root',              
            password='sua_senha',     
            database='rh_empresa'     
        )

        print("✅ Conexão com o banco estabelecida com sucesso!")
        return conexao

    except mysql.connector.Error as erro:
        print("❌ Ocorreu um erro ao tentar conectar ao banco de dados.")
        print(f"Detalhes do erro: {erro}")
        return None
