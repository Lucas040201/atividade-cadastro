<h3 align="center">Ac 02</h3>

## 📝 Sumário

- [Como Rodar](#como)
- [Banco de dados](#banco)

## 🧐 Como Rodar <a name = "como"></a>

<p> Para rodar este projeto apenas digite no terminal docker-compose up.</p>

## 🔧 Começando <a name = "banco"></a>

<p>O docker ira subir o banco de dados, portanto, é necessário apenas criar o banco de dados com os seguintes comandos:</p>

<p>Para acessar o container de mysql:</p>

'''

    docker exec -it ac02_db_1  /bin/bash

'''
<p>Após isso, logue no mysql e digite a senha assim que solicitar.</p>
'''

    mysql -uroot -p
    
'''

<p>Para criar o banco de dados utilize os seguintes comandos. Apenas copie e cole.</p>
'''

    CREATE DATABASE atividade;

    USE atividade;

    CREATE TABLE usuario(
        id_usuario INT  NOT NULL AUTO_INCREMENT,
        nome VARCHAR(100),
        email VARCHAR(100),
        endereco VARCHAR(100),

        PRIMARY KEY (id_usuario)
    );
'''