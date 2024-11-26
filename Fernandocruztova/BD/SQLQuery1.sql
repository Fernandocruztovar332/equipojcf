create database SERVITAXI;

use SERVITAXI

CREATE TABLE Usuarios (
    id_usuario int PRIMARY KEY  identity not null,
    nombre VARCHAR(50) NOT NULL,
    apellidos VARCHAR(60) NOT NULL,
    telefono VARCHAR(16) NOT NULL,
    contraseña VARCHAR(15) NOT NULL
	)


create table Unidad(
	id_U int primary key identity not null,
	placa varchar(15) not null,
	marca varchar(50) not null,
	modelo varchar(50) not null,
	id_Uimg varchar(100) not null


)


create table Conductor(
	id_C int primary key identity not null,
	nombreC varchar(50) not null,
	apPC varchar(25) not null,
	apMC varchar(25) not null,
	telefono varchar(16) not null,
	contraseñaC varchar(15) not null,
	licenciaC varchar(50) not null,
	vencimientoLC date not null,
	id_U int NOT NULL REFERENCES Unidad(id_U)


)

create table Viaje(
	id_V int primary key identity not null,
	origenV varchar(255) not null,
	destinoV varchar(255) not null,
	fecha_hora datetime not null,
	id_U int NOT NULL REFERENCES Unidad(id_U),
	id_C int NOT NULL REFERENCES Conductor(id_C),
	id_usuario int NOT NULL REFERENCES Usuarios(id_usuario)

)
