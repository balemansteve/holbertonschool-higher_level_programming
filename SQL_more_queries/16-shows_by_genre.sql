-- List TV shows and their genres using RIGHT JOINs, ordered by show title and genre name

SELECT tv_shows.title, tv_genres.name
FROM tv_genres
RIGHT JOIN tv_show_genres ON tv_genres.id = tv_show_genres.genre_id
RIGHT JOIN tv_shows ON tv_shows.id = tv_show_genres.show_id
ORDER BY tv_shows.title, tv_genres.name;