# Validação básica de CPF (formato e tamanho)
def validar_cpf(cpf):
    return len(cpf) == 14 and cpf.count('.') == 2 and cpf.count('-') == 1

# Formata telefone para padrão brasileiro
def formatar_telefone(telefone):
    telefone = telefone.replace(" ", "").replace("-", "").replace("(", "").replace(")", "")
    if len(telefone) == 11:
        return f"({telefone[:2]}){telefone[2:7]}-{telefone[7:]}"
    return telefone

# Confirmação simples antes de ações críticas
def confirmar_acao(mensagem):
    resposta = input(f"{mensagem} (s/n): ").lower()
    return resposta == 's'

# Exibe uma linha separadora para o terminal
def linha():
    print("-" * 40)

from utils import validar_cpf, confirmar_acao

cpf = input("Digite o CPF: ")
if not validar_cpf(cpf):
    print("❌ CPF inválido. Use o formato 000.000.000-00")
    return

if confirmar_acao("Deseja realmente excluir este funcionário?"):
    # Executa exclusão
    pass
