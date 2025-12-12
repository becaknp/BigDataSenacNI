CREATE DATABASE sales_online; -- criar a tabela
use sales_online; -- marcar a tabela
-- Criação do banco de dados
-- 1. Fornecedores (tabela independente)
CREATE TABLE Fornecedores (
    Supplier_ID INT PRIMARY KEY,
    Supplier_Name VARCHAR(100),
    Contact_Email VARCHAR(100),
    Country VARCHAR(50)
);

-- 2. Produtos (depende de Fornecedores)
CREATE TABLE Produtos (
    Product_ID INT PRIMARY KEY,
    Product_Name VARCHAR(255),
    Category VARCHAR(50),
    Unit_Price DECIMAL(10,2),
    Cost_Price DECIMAL(10,2),
    Supplier_ID INT
);

-- 3. Clientes (tabela independente)
CREATE TABLE Clientes (
    Customer_ID INT PRIMARY KEY,
    Customer_Name VARCHAR(100),
    Email VARCHAR(100),
    Region VARCHAR(50)
);

-- 4. Vendas (depende de Produtos e Clientes)
CREATE TABLE Vendas (
    Transaction_ID INT PRIMARY KEY,
    Date_transaction DATE,
    Customer_ID INT,
    Product_ID INT,
    Units_Sold INT,
    Total_Revenue DECIMAL(10,2),
    Payment_Method VARCHAR(50),
    Region VARCHAR(50)
);
DESCRIBE produtos;

-- Adicionar FK de Produtos para Fornecedores
ALTER TABLE Produtos
ADD CONSTRAINT FK_Produtos_Fornecedores
FOREIGN KEY (Supplier_ID) 
REFERENCES Fornecedores(Supplier_ID);

-- Adicionar FK de Vendas para Clientes
ALTER TABLE Vendas
ADD CONSTRAINT FK_Vendas_Clientes
FOREIGN KEY (Customer_ID) 
REFERENCES Clientes(Customer_ID);

-- Adicionar FK de Vendas para Produtos
ALTER TABLE Vendas
ADD CONSTRAINT FK_Vendas_Produtos
FOREIGN KEY (Product_ID) 
REFERENCES Produtos(Product_ID);