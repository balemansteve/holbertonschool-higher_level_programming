-- Count the number of records per score and sort them in descending order

SELECT score, COUNT(*)
FROM second_table
GROUP BY score
ORDER BY number DESC;