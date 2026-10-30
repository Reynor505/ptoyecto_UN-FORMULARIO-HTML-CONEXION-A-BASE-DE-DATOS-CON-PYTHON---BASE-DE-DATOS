CREATE DATABASE IF NOT EXISTS fakenews_db;

USE fakenews_db;

-- Borra las tablas de versiones anteriores (si existen)
DROP TABLE IF EXISTS noticias;
DROP TABLE IF EXISTS reportes;

CREATE TABLE reportes (
    id         INT AUTO_INCREMENT PRIMARY KEY,
    nombre     VARCHAR(50)  NOT NULL,
    apellido   VARCHAR(50)  NOT NULL,
    fecha      DATE         NOT NULL,
    red_social VARCHAR(30)  NOT NULL,
    reporte    TEXT         NOT NULL
);
