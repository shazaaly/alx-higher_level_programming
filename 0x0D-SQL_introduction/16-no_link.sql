-- a script that lists all records of the table second_table
-- Results should display the score and the name (in this order)
-- Records should be listed by descending score

SELECT score, name
FROM `second_table`
WHERE `name` != ""
ORDER BY score DESC;

