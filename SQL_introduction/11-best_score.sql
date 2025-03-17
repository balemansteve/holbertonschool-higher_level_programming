-- List records with a score greater than or equal to 10, sorted in descending order

SELECT score, name
FROM second_table
WHERE score >= 10
ORDER BY score DESC; 