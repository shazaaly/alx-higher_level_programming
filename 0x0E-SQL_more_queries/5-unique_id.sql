-- Write a script that creates the table   on your MySQL server.

-- unique_id description:
-- id INT with the default value 1 and must be unique
-- name VARCHAR(256)

CREATE TABLE IF NOT EXISTS `unique_id` (
    id INT NOT NULL UNIQUE DEFAULT 1,
    name VARCHAR(256)
);

