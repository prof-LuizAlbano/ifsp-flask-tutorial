DROP TABLE IF EXISTS contatos;

CREATE TABLE contatos (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  nome VARCHAR(50) NOT NULL,
  telefone VARCHAR(20),
  data_nascimento DATE,
  email VARCHAR(100),
  data_cadastro TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP
);