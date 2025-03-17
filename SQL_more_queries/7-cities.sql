-- Create a database and a table with a foreign key referencing 'states'

CREATE DATABASE IF NOT EXISTS hbtn_0d_usa;

CREATE TABLE IF NOT EXISTS hbtn_0d_usa.cities (
    `id` INT NOT NULL PRIMARY KEY AUTO_INCREMENT UNIQUE,
    `state_id` INT NOT NULL,
    FOREIGN KEY (`state_id`) REFERENCES states (`id`),
    `name` VARCHAR(256) NOT NULL
);