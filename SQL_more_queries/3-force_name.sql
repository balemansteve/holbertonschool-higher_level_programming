-- Create a table with a non-null constraint on the 'name' column

CREATE TABLE IF NOT EXISTS force_name(id INT, name VARCHAR(256) NOT NULL);