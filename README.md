## Analises-UnB
Trabalho final da disciplina de Banco de Dados
Desenvolvido por: Roberto Rodrigues Macedo Júnior
Tecnologias usadas: Python, Streamlit, MySQL, WampServer

## Descrição
O projeto é um aplicativo web que busca desenvolver um banco de dados para fazer avaliação de disciplinas e professores. O trabalho visa fornecer uma ferramenta de manipulação de dados, que atenda aos seguintes requisitos: 3 CRUDs de entidades diferentes, uma camada de persistência e uso de views e procedures.

## WampServer
A base de dados foi construída a partir do MySQL, utilizando o PhpMyAdmin, e o servidor WampServer para colocar a aplicação no ar. Para baixar, siga as instruções em https://www.wampserver.com/en/ .

## Executando o projeto
É necessário criar uma pasta para o trabalho, execute no prompt de comando o comando: python -m venv venv

Após, execute os comandos:
cd venv/Scripts
activate 

Nisso, já estará dentro do ambiente virtual.

Depois disso, crie uma pasta crud.py e copie e cole o código que está na pasta crud_py aqui no GitHub.

Deve-se também instalar o mysql.connector , com o comando:
pip install mysql-connector-python

E o streamlit, pelo comando:
pip install streamlit

Quanto ao servidor WAMP, instale e ative ele indo na pasta dele e abrindo o aplicativo wampmanager, que está dentro da pasta wamp64.

Com ele ativado, pode ir em qualquer navegador e acessar a URL: localhost/phpmyadmin , para assim poder mexer no banco de dados MySQL.

Nele, crie um banco de dados chamado dados_app, e crie as tabelas relacionadas no arquivo CreateTable.sql, que está no GitHub.

Para rodar, esteja dentro do ambiente virtual e na pasta do trabalho. Após, deve executar o comando: streamlit run crud.py

Acredito que com isso já dê pra executar a aplicação.
