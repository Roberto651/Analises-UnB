CREATE DATABASE dados_app;
USE dados_app;

CREATE TABLE `dados_app`.`avaliacao` (
`Professor` VARCHAR(50) NOT NULL , 
`Turma` VARCHAR(50) NOT NULL , 
`Horário` VARCHAR(50) NOT NULL , 
`Cod_disciplina` VARCHAR(50) NOT NULL , 
`Comentário` VARCHAR(100) NOT NULL , PRIMARY KEY (`Comentário`)
);

CREATE TABLE `dados_app`.`alunos` (
`Nome` VARCHAR(50) NOT NULL , 
`Matrícula` INT NOT NULL , 
`Curso` VARCHAR(50) NOT NULL , 
`Email` VARCHAR(50) NOT NULL , 
`Senha` VARCHAR(100) NOT NULL ,
`imagem` BINARY , PRIMARY KEY (`Matrícula`)
);

CREATE TABLE `dados_app`.`professores` (
`Nome` VARCHAR(50) NOT NULL , 
`Matrícula` VARCHAR(50) NOT NULL , 
`Departamento_codigo` VARCHAR(50) NOT NULL , PRIMARY KEY (`Matrícula`)
);

CREATE TABLE `dados_app`.`turma` (
`Professor` VARCHAR(50) NOT NULL , 
`Cod_disciplina` INT NOT NULL , 
`Turma` VARCHAR(50) NOT NULL , 
`Horário` VARCHAR(50) NOT NULL , 
`Local` VARCHAR(50) NOT NULL ,
`Vagas totais` VARCHAR(50) NOT NULL ,
`Vagas ocupadas` VARCHAR(50) NOT NULL , PRIMARY KEY (`Horário`, `Local`)
);

CREATE TABLE `dados_app`.`departamento` (
`Nome` VARCHAR(50) NOT NULL , 
`Código` VARCHAR(50) NOT NULL , PRIMARY KEY (`Código`)
);

CREATE TABLE `dados_app`.`disciplina` (
`Nome` VARCHAR(50) NOT NULL , 
`Código` VARCHAR(50) NOT NULL , 
`Departamento_codigo` VARCHAR(50) NOT NULL , PRIMARY KEY (`Código`)
);

CREATE TABLE `dados_app`.`denuncia` (
`Avaliação` VARCHAR(50) NOT NULL , 
`Denúncia` VARCHAR(50) NOT NULL , PRIMARY KEY (`Avaliação`, `Denúncia`)
);

CREATE PROCEDURE quantidadeAlunos()
BEGIN
    DECLARE contagemAlunos INT;
    SELECT COUNT(*) INTO contagemAlunos FROM alunos;
    SELECT contagemAlunos;
END;

CREATE VIEW emailaluno AS
SELECT Nome, Email from alunos;
