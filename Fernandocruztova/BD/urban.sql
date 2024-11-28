create database URBAN;



CREATE TABLE Usuarios (
    id_usuario int PRIMARY KEY  identity not null,
    nombre VARCHAR(50) NOT NULL,
    apellidos VARCHAR(60) NOT NULL

	)

CREATE table loginusuario(
id_usuario int not null references Usuarios(id_usuario),
telefonocoreo varchar(80) not null,
pasword varchar(10) not null,
)

