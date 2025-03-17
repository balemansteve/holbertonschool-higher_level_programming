-- List all records, sorted by score in descending order

SELECT score, name
FROM second_table
WHERE name IS NOT NULL
ORDER BY score DESC;