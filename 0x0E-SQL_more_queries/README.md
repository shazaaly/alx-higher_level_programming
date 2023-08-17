0x0E. SQL - More queries
# SQL Queries for TV Show Database

This repository contains a series of SQL scripts that interact with the `hbtn_0d_tvshows` database. Each script performs a specific task related to querying and retrieving data from the database. The database contains information about TV shows, genres, and their relationships.

To use these scripts, follow the instructions below:

1. **Import the Database:**
   - Before running the scripts, make sure you have the `hbtn_0d_tvshows` database imported into your MySQL server. You can use the provided database dump for this purpose.

2. **Running the Scripts:**
   - Open a terminal and navigate to the directory containing the SQL scripts.
   - Use the `mysql` command to execute a script, passing the necessary arguments such as the hostname, username, and password.

3. **Script Descriptions:**

   - `10-genre_id_by_show.sql`: Lists all shows with at least one genre linked.
   - `11-genre_id_all_shows.sql`: Lists all shows and their genres.
   - `12-no_genre.sql`: Lists shows without a linked genre.
   - `13-count_shows_by_genre.sql`: Lists genres and the number of shows linked to each.
   - `14-my_genres.sql`: Lists genres of the show "Dexter".
   - `15-comedy_only.sql`: Lists all Comedy shows.
   - `16-shows_by_genre.sql`: Lists all shows and their linked genres.

4. **Notes:**
   - Some scripts may require specific conditions or constraints to be met in the database, as indicated in their descriptions.

Please note that these scripts are designed for educational and illustrative purposes. They provide insights into SQL querying and database interactions. For real-world applications, additional considerations and optimizations may be necessary.

For any questions or clarifications, feel free to reach out to the repository owner.

**Repository Information:**

- Directory: 0x0E-SQL_more_queries

**Disclaimer:**
The database and data used in these scripts are fictional and are intended for learning purposes only. No actual TV show or copyrighted content is represented here.
All 
