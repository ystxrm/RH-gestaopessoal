CREATE DATABASE gestaopessoal;
USE gestaopessoal;

CREATE TABLE departamentos (
 id INT AUTO_INCREMENT PRIMARY KEY,
 nome VARCHAR(100) NOT NULL,
 descricao TEXT
);
-- Criação da tabela 'cargos' para armazenar os cargos disponíveis na empresa
CREATE TABLE cargos ( 
id INT AUTO_INCREMENT PRIMARY KEY,
nome VARCHAR(100) NOT NULL,
salario_base DECIMAL(10,2) NOT NULL,
departamento_id INT,
FOREIGN KEY (departamento_id) REFERENCES departamentos(id)
);

-- Criação da tabela 'funcionarios' para armazenar dados dos colaboradores da empresa
CREATE TABLE funcionarios (
id INT AUTO_INCREMENT PRIMARY KEY,-- Identificador único do funcionário
nome VARCHAR(100) NOT NULL,-- Nome completo do funcionário
cpf VARCHAR(14) UNIQUE NOT NULL,-- CPF com formato padrão brasileiro, deve ser único
email VARCHAR(100), 
telefone VARCHAR(20),  
endereco TEXT, 
data_admissao DATE,
cargo_id INT,
FOREIGN KEY (cargo_id) REFERENCES cargos(id)-- Chave estrangeira ligando ao cargo na tabela 'cargos'
);

-- Criação da tabela 'admissoes' para registrar eventos como admissão, demissão e transferência de funcionários
CREATE TABLE admissoes ( 
id INT AUTO_INCREMENT PRIMARY KEY, -- Identificador único para cada registro, gerado automaticamente
funcionario_id INT, -- Referência ao funcionário envolvido no evento
horario DATE NOT NULL, -- Data do evento (admissão, demissão ou transferência)
tipo ENUM('Admissão', 'Demissão', 'Transferência') NOT NULL,-- Tipo do evento, limitado a três opções
observacoes TEXT,-- Campo livre para observações adicionais sobre o evento
FOREIGN KEY (funcionario_id) REFERENCES funcionarios(id) -- Chave estrangeira que conecta ao funcionário correspondente
);

INSERT INTO departamentos (nome, descricao) 
VALUES ('TI', 'Tecnologia da informação');

INSERT INTO cargos (nome, salario_base, departamento_id)
VALUES ('Senior', '5500', '1');

INSERT INTO funcionarios (nome, cpf, email, telefone, endereco, data_admissao, cargo_id)
VALUES ('Marcos Paulo Figueredo', '000.123.421-56', 'marcos1823@gmail.com', '(61)99999-9999', 'Rua A, Brasília', '2023-01-15', 1
);

INSERT INTO admissoes (funcionario_id, horario, tipo, observacoes) 
VALUES (1, '2023-01-15', 'Admissão', 'Contratação inicial');


