-- a script that lists all shows, and all genres linked to that show, from the database


SELECT title, name
FROM tv_shows
LEFT  JOIN tv_shows_genres
ON tv_shows.id = tv_shows_genres.show_id
LEFT JOIN tv_genres
ON tv_genres.id = tv_shows_genres.genre_id
ORDER BY tv_shows.title ASC, tv_genres.name ASC;

