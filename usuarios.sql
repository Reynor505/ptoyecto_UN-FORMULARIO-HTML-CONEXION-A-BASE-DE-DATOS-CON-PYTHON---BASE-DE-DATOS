CREATE DATABASE usuario_db

USE usuario_db;

CREATE TABLE registros (
    id     INT AUTO_INCREMENT PRIMARY KEY,
    nombre VARCHAR(100) NOT NULL,
    correo VARCHAR(120) NOT NULL UNIQUE,
    fecha  DATE NOT NULL
);
