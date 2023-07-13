CREATE TABLE `dados_app`.`avaliacao` (
`Professor` VARCHAR(50) NOT NULL , 
`Turma` VARCHAR(50) NOT NULL , 
`Horário` VARCHAR(50) NOT NULL , 
`Cod_disciplina` VARCHAR(50) NOT NULL , 
`Comentário` VARCHAR(100) NOT NULL , PRIMARY KEY (`Comentário`)
) ENGINE = MyISAM;


CREATE TABLE `dados_app`.`alunos` (
`Nome` VARCHAR(50) NOT NULL , 
`Matrícula` INT NOT NULL , 
`Curso` VARCHAR(50) NOT NULL , 
`Email` VARCHAR(50) NOT NULL , 
`Senha` VARCHAR(100) NOT NULL , PRIMARY KEY (`Matrícula`)
) ENGINE = MyISAM;


CREATE TABLE `dados_app`.`professores` (
`Nome` VARCHAR(50) NOT NULL , 
`Matrícula` VARCHAR(50) NOT NULL , 
`Departamento_codigo` VARCHAR(50) NOT NULL , PRIMARY KEY (`Matrícula`)
) ENGINE = MyISAM;


CREATE PROCEDURE quantidadeAlunos()
BEGIN
    DECLARE contagemAlunos INT;
    SELECT COUNT(*) INTO contagemAlunos FROM alunos;
    SELECT contagemAlunos;
END;

CREATE VIEW emailaluno AS
SELECT Nome, Email from alunos;
