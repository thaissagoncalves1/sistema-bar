-- Categorias
CREATE TABLE categorias(
    id SERIAL PRIMARY KEY,
    nome TEXT NOT NULL UNIQUE
);

INSERT INTO categorias (nome) VALUES
('Bebidas'),
('Petiscos'),
('Pratos Individuais'),
('Pratos para Compartilhar');

-- Produtos
CREATE TABLE produtos(
    id SERIAL PRIMARY KEY,
    nome TEXT NOT NULL UNIQUE,
    preco NUMERIC(10,2) NOT NULL,
    categoria_id INTEGER REFERENCES categorias(id)
);

INSERT INTO produtos (nome, preco, categoria_id) VALUES
('Heineken 600 ml', 14.00, (SELECT id FROM categorias WHERE nome = 'Bebidas')),
('Spaten 600 ml', 13.00, (SELECT id FROM categorias WHERE nome = 'Bebidas')),
('Brahma 600 ml', 11.00, (SELECT id FROM categorias WHERE nome = 'Bebidas')),
('Antarctica 600 ml', 11.00, (SELECT id FROM categorias WHERE nome = 'Bebidas')),
('Heineken long neck', 9.00, (SELECT id FROM categorias WHERE nome = 'Bebidas')),
('Imperio gold', 7.00, (SELECT id FROM categorias WHERE nome = 'Bebidas')),
('Imperio lager', 8.00, (SELECT id FROM categorias WHERE nome = 'Bebidas')),
('Brahma cracudinha', 5.00, (SELECT id FROM categorias WHERE nome = 'Bebidas')),
('Antarctica cracudinha', 5.00, (SELECT id FROM categorias WHERE nome = 'Bebidas')),
('Heineken latão', 10.00, (SELECT id FROM categorias WHERE nome = 'Bebidas')),
('Spaten latão', 9.00, (SELECT id FROM categorias WHERE nome = 'Bebidas')),
('Brahma latão', 8.00, (SELECT id FROM categorias WHERE nome = 'Bebidas')),
('Antarctica latão', 8.00, (SELECT id FROM categorias WHERE nome = 'Bebidas')),
('Itaipava latão', 6.00, (SELECT id FROM categorias WHERE nome = 'Bebidas')),
('Imperio latão', 6.00, (SELECT id FROM categorias WHERE nome = 'Bebidas')),
('Redbull lata', 12.00, (SELECT id FROM categorias WHERE nome = 'Bebidas')),
('Coca cola lata', 5.00, (SELECT id FROM categorias WHERE nome = 'Bebidas')),
('Guaravita', 2.00, (SELECT id FROM categorias WHERE nome = 'Bebidas')),
('Coca 2L', 15.00, (SELECT id FROM categorias WHERE nome = 'Bebidas')),
('Guaraná Antarctica 2L', 12.00, (SELECT id FROM categorias WHERE nome = 'Bebidas')),
('Fanta Uva/Laranja 2L', 9.00, (SELECT id FROM categorias WHERE nome = 'Bebidas')),
('Gurjão de Frango', 35.00, (SELECT id FROM categorias WHERE nome = 'Petiscos')),
('Gurjão de Peixe', 45.00, (SELECT id FROM categorias WHERE nome = 'Petiscos')),
('Batata Frita', 15.00, (SELECT id FROM categorias WHERE nome = 'Petiscos')),
('Aipim Frito', 15.00, (SELECT id FROM categorias WHERE nome = 'Petiscos')),
('Pastel de Camarão com Catupiry (6 unidades)', 18.00, (SELECT id FROM categorias WHERE nome = 'Petiscos')),
('Pastel de Queijo (6 unidades)', 12.00, (SELECT id FROM categorias WHERE nome = 'Petiscos')),
('Pastel de Carne (6 unidades)', 15.00, (SELECT id FROM categorias WHERE nome = 'Petiscos')),
('Calabresa Acebolada', 15.00, (SELECT id FROM categorias WHERE nome = 'Petiscos')),
('Linguiça Toscana Acebolada', 15.00, (SELECT id FROM categorias WHERE nome = 'Petiscos')),
('Isca de Carne com Cebola', 30.00, (SELECT id FROM categorias WHERE nome = 'Petiscos')),
('Frango à Passarinho', 35.00, (SELECT id FROM categorias WHERE nome = 'Petiscos')),
('Bolinho de Bacalhau (6 unidades)', 30.00, (SELECT id FROM categorias WHERE nome = 'Petiscos')),
('Bolinho de Aipim com Carne Seca', 10.00, (SELECT id FROM categorias WHERE nome = 'Petiscos')),
('Torresmo', 20.00, (SELECT id FROM categorias WHERE nome = 'Petiscos')),
('Filé de Frango Grelhado (Arroz, Feijão, Batata Frita e Salada)', 22.00, (SELECT id FROM categorias WHERE nome = 'Pratos Individuais')),
('Bife Acebolado (Arroz, Feijão, Batata Frita e Salada)', 25.00, (SELECT id FROM categorias WHERE nome = 'Pratos Individuais')),
('Linguiça Toscana Grelhada (Arroz, Feijão, Vinagrete e Batata Frita)', 24.00, (SELECT id FROM categorias WHERE nome = 'Pratos Individuais')),
('Picadinho de Carne (Arroz, Feijão, Ovo Frito e Farofa)', 27.00, (SELECT id FROM categorias WHERE nome = 'Pratos Individuais')),
('Strogonoff de Frango (Arroz e Batata Palha)', 26.00, (SELECT id FROM categorias WHERE nome = 'Pratos Individuais')),
('Strogonoff de Carne (Arroz e Batata Palha)', 30.00, (SELECT id FROM categorias WHERE nome = 'Pratos Individuais')),
('Contra Filé (Arroz, Feijão, Batata Frita e Salada)', 32.00, (SELECT id FROM categorias WHERE nome = 'Pratos Individuais')),
('Filé de Tilápia (Arroz, Purê de Batata e Salada)', 32.00, (SELECT id FROM categorias WHERE nome = 'Pratos Individuais')),
('Parmegiana de Frango (Arroz e Batata Frita)', 34.00, (SELECT id FROM categorias WHERE nome = 'Pratos Individuais')),
('Parmegiana de Carne (Arroz e Batata Frita)', 38.00, (SELECT id FROM categorias WHERE nome = 'Pratos Individuais')),
('Picanha na Chapa (2 pessoas)', 89.00, (SELECT id FROM categorias WHERE nome = 'Pratos para Compartilhar')),
('Contra Filé na Chapa (2 pessoas)', 69.00, (SELECT id FROM categorias WHERE nome = 'Pratos para Compartilhar')),
('Filé de Frango à Parmegiana (2 pessoas)', 59.00, (SELECT id FROM categorias WHERE nome = 'Pratos para Compartilhar')),
('Filé Mignon à Parmegiana (2 pessoas)', 79.00, (SELECT id FROM categorias WHERE nome = 'Pratos para Compartilhar')),
('Tilápia Frita com Pirão (2 pessoas)', 69.00, (SELECT id FROM categorias WHERE nome = 'Pratos para Compartilhar')),
('Moqueca de Peixe (2 pessoas)', 89.00, (SELECT id FROM categorias WHERE nome = 'Pratos para Compartilhar')),
('Costela Suína com Batata Frita (2 pessoas)', 69.00, (SELECT id FROM categorias WHERE nome = 'Pratos para Compartilhar')),
('Churrasco Misto (2 pessoas)', 85.00, (SELECT id FROM categorias WHERE nome = 'Pratos para Compartilhar')),
('Frango à Passarinho Completo (4 pessoas)', 65.00, (SELECT id FROM categorias WHERE nome = 'Pratos para Compartilhar')),
('Feijoada Completa (2 pessoas)', 69.00, (SELECT id FROM categorias WHERE nome = 'Pratos para Compartilhar'));

-- Comandas
CREATE TABLE comandas (
    id SERIAL PRIMARY KEY,
    identificador_comanda VARCHAR(50) NOT NULL,
    status VARCHAR(20) NOT NULL DEFAULT 'aberta',
    forma_pagamento VARCHAR(20),
    criado_em TIMESTAMP DEFAULT NOW(),
    pago_em TIMESTAMP
);

-- Itens da comanda
CREATE TABLE itens_comanda(
    id SERIAL PRIMARY KEY,
    comanda_id INTEGER REFERENCES comandas(id) NOT NULL,
    produto_id INTEGER REFERENCES produtos(id) NOT NULL,
    quantidade INTEGER NOT NULL CHECK (quantidade > 0),
    preco_unitario NUMERIC(10,2) NOT NULL
);