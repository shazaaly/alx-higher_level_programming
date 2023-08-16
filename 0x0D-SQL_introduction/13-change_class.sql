--  a script that removes all records with a score <= 5 in second_table
-- database hbtn_0c_0 in your MySQL server.

DELETE
FROM `second_table`
WHERE score <= 5;

