import os
import sys
from io import BytesIO,StringIO
import mysql.connector
import streamlit as st
import pandas as pd
from PIL import Image, ImageEnhance

# Estabelecer conexão como MySQL Server

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="dados_app"
)

mycursor = mydb.cursor()
print("Conexão Estabelecida")

# Criar App Streamlit

def main():
    st.title("Análises UnB");

    # Coisas do display para fazer o CRUD
    option = st.sidebar.selectbox("Selecione a operação",("Login-Aluno","Perfil-Aluno","Atualizar conta-Aluno","Deletar conta-Aluno","Login-Professor","Perfil-Professor","Atualizar conta-Professor","Deletar conta-Professor","Criar Avaliação","Avaliações","Atualizar Avaliação","Deletar Avaliação", "View", "Procedure"))
    # Fazer operações do CRUD
    if option == "Login-Aluno":
        st.subheader("Aluno, insira seus dados")
        nome=st.text_input("Nome")
        matricula=st.text_input("Matrícula")
        curso=st.text_input("Curso")
        email=st.text_input("Email")
        senha=st.text_input("Senha")

        imagem = st.file_uploader("Carregue uma foto sua", type=['jpg', 'png', 'jpeg'])
        imagem_binaria = imagem.read()

        if st.button("Login"):
            sql = "INSERT INTO alunos(Nome,Matrícula,Curso,Email,Senha,imagem) values(%s,%s,%s,%s,%s,%s)"
            val = (nome,matricula,curso,email,senha,imagem_binaria)
            mycursor.execute(sql,val)
            mydb.commit()
            st.success("Conta criada com sucesso!")

    elif option == "Perfil-Aluno":
        st.subheader("Alunos")
        mycursor.execute("SELECT * FROM alunos")
        result = mycursor.fetchall()
        for row in result:
           st.write(row)

    elif option == "Atualizar conta-Aluno":
        st.subheader("Insira seus novos dados")
        nome=st.text_input("Insira seu novo nome")
        matricula=st.text_input("Insira sua matrícula")
        curso=st.text_input("Insira seu novo curso")
        email=st.text_input("Insira seu novo email")
        senha=st.text_input("Insira sua nova senha")
        if st.button("Atualizar"):
            sql="UPDATE alunos SET Nome=%s,Curso=%s,Email=%s,Senha=%s WHERE Matrícula=%s"
            val = (nome,curso,email,senha,matricula)
            mycursor.execute(sql,val)
            mydb.commit()
            st.success("Conta atualizada com sucesso!")

    elif option == "Deletar conta-Aluno":
        st.subheader("Delete uma conta")
        matricula=st.text_input("Insira sua matrícula")
        if st.button("Deletar"):
            sql="DELETE FROM alunos WHERE Matrícula=%s"
            val=(matricula,)
            mycursor.execute(sql,val)
            mydb.commit()
            st.success("Conta deletada com sucesso!")

    elif option == "Login-Professor":
        st.subheader("Professor, insira seus dados")
        nome=st.text_input("Nome")
        matricula=st.text_input("Matrícula")
        c_departamento=st.text_input("Código do departamento")
        if st.button("Login"):
            sql = "INSERT INTO professores(Nome,Matrícula,Departamento_codigo) values(%s,%s,%s)"
            val = (nome,matricula,c_departamento)
            mycursor.execute(sql,val)
            mydb.commit()
            st.success("Conta criada com sucesso!")

    elif option == "Perfil-Professor":
        st.subheader("Professores")
        mycursor.execute("SELECT * FROM professores")
        result = mycursor.fetchall()
        for row in result:
           st.write(row)

    elif option == "Atualizar conta-Professor":
        st.subheader("Professor, insira seus novos dados")
        nome=st.text_input("Insira seu novo nome")
        matricula=st.text_input("Insira sua matrícula")
        c_departamento=st.text_input("Insira seu novo código do departamento")
        if st.button("Atualizar"):
            sql="UPDATE professores SET Nome=%s,Departamento_codigo=%s WHERE Matrícula=%s"
            val = (nome,c_departamento,matricula)
            mycursor.execute(sql,val)
            mydb.commit()
            st.success("Conta atualizada com sucesso!")

    elif option == "Deletar conta-Professor":
        st.subheader("Professor, delete uma conta")
        matricula=st.text_input("Insira sua matrícula")
        if st.button("Deletar"):
            sql="DELETE FROM professores WHERE Matrícula=%s"
            val=(matricula,)
            mycursor.execute(sql,val)
            mydb.commit()
            st.success("Conta deletada com sucesso!")

    elif option == "Criar Avaliação":
        st.subheader("Aluno, insira os dados da avaliação")
        prof=st.text_input("Professor")
        turma=st.text_input("Turma")
        horario=st.text_input("Horário")
        c_disciplina=st.text_input("Código de disciplina")
        comentario=st.text_input("Comentário")

        if st.button("Criar"):
            sql = "INSERT INTO avaliacao(Professor,Turma,Horário,Cod_disciplina,Comentário) values(%s,%s,%s,%s,%s)"
            val = (prof,turma,horario,c_disciplina,comentario)
            mycursor.execute(sql,val)
            mydb.commit()
            st.success("Avaliação criada com sucesso!")

    elif option == "Avaliações":
        st.subheader("Avaliações")
        mycursor.execute("SELECT * FROM avaliacao")
        result = mycursor.fetchall()
        for row in result:
           st.write(row)

    elif option == "Atualizar Avaliação":
        st.subheader("Usuário, insira os novos dados da avaliação")
        prof=st.text_input("Novo professor")
        turma=st.text_input("Nova turma")
        horario=st.text_input("Novo horário")
        c_disciplina=st.text_input("Novo código de disciplina")
        comentario=st.text_input("Comentário")
        if st.button("Atualizar"):
            sql="UPDATE avaliacao SET Professor=%s,Turma=%s,Horário=%s,Cod_disciplina=%s WHERE Comentário=%s"
            val = (prof,turma,horario,c_disciplina,comentario)
            mycursor.execute(sql,val)
            mydb.commit()
            st.success("Avaliação atualizada com sucesso!")

    elif option == "Deletar Avaliação":
        st.subheader("Usuário, delete uma avaliação")
        comentario=st.text_input("Insira o comentário da avaliação")
        if st.button("Deletar"):
            sql="DELETE FROM avaliacao WHERE Comentário=%s"
            val=(comentario,)
            mycursor.execute(sql,val)
            mydb.commit()
            st.success("Avaliação deletada com sucesso!")

    elif option == "View":
        st.subheader("Email dos alunos")
        mycursor.execute("SELECT * FROM emailaluno")
        result = mycursor.fetchall()
        for row in result:
           st.write(row)

    elif option == "Procedure":
        st.subheader("Quantidade de alunos")
        mycursor.execute("CALL quantidadeAlunos()")
        result = mycursor.fetchall()
        for row in result:
           st.write(row)


if __name__ == "__main__":
    main()