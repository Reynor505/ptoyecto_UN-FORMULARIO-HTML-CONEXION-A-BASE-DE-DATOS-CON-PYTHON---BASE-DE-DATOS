CREATE DATABASE IF NOT EXISTS fakenews_db;

USE fakenews_db;

-- Borra la tabla anterior (si ya habias ejecutado la version pasada)
DROP TABLE IF EXISTS noticias;

CREATE TABLE noticias (
    id         INT AUTO_INCREMENT PRIMARY KEY,
    titulo     VARCHAR(150) NOT NULL,
    red_social VARCHAR(30)  NOT NULL,
    enlace     VARCHAR(255) NOT NULL,
    estado     VARCHAR(20)  NOT NULL,
    fecha      DATE         NOT NULL
);
