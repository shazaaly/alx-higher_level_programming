-- a script to lists all genres of the show Dexter
-- The tv_shows table contains only one record where title = Dexter (but the id can be different)
-- Each record should display: tv_genres.name
-- Results must be sorted in ascending order by the genre name

SELECT name
FROM tv_genres
JOIN tv_shows_genres
ON tv_genres.id = tv_shows_genres.genre_id
JOIN tv_shows
ON tv_shows.id = tv_shows_genres.show_id
WHERE tv_shows.title = 'Dexter'
GROUP BY name
ORDER BY name ASC;

