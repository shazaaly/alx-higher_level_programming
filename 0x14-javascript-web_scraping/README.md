# JavaScript Web Scraping Tasks

This repository contains a collection of JavaScript scripts for various web scraping tasks. These scripts are designed to perform different operations, such as reading and writing files, making HTTP requests, and interacting with the Star Wars API. Below, you will find an overview of each task and how to use them.

## Task 0: Readme

### Description
This script reads and prints the content of a file.

### Usage
```
./0-readme.js <file_path>
```
- `<file_path>`: The path to the file you want to read.

## Task 1: Write Me

### Description
This script writes a string to a file.

### Usage
```
./1-writeme.js <file_path> "<string_to_write>"
```
- `<file_path>`: The path to the file where you want to write the string.
- `<string_to_write>`: The string you want to write to the file.

## Task 2: Status Code

### Description
This script displays the status code of a GET request to a URL.

### Usage
```
./2-statuscode.js <URL>
```
- `<URL>`: The URL to request using a GET method.

## Task 3: Star Wars Movie Title

### Description
This script prints the title of a Star Wars movie based on the episode number.

### Usage
```
./3-starwars_title.js <movie_id>
```
- `<movie_id>`: The episode number of the Star Wars movie.

## Task 4: Star Wars Wedge Antilles

### Description
This script prints the number of movies where the character "Wedge Antilles" is present.

### Usage
```
./4-starwars_count.js <API_URL>
```
- `<API_URL>`: The API URL of the Star Wars API.

## Task 5: Loripsum

### Description
This script gets the contents of a webpage and stores it in a file.

### Usage
```
./5-request_store.js <URL> <file_path>
```
- `<URL>`: The URL of the webpage to request.
- `<file_path>`: The path to the file where the webpage content will be stored.

## Task 6: How Many Completed?

### Description
This script computes the number of tasks completed by user ID.

### Usage
```
./6-completed_tasks.js <API_URL>
```
- `<API_URL>`: The API URL to retrieve task information.

## Task 7: Who Was Playing in This Movie?

### Description
This script prints all characters of a Star Wars movie based on the movie ID.

### Usage
```
./100-starwars_characters.js <movie_id>
```
- `<movie_id>`: The movie ID (e.g., 3 for "Return of the Jedi").

## Task 8: Right Order

### Description
This script prints all characters of a Star Wars movie in the order specified in the API response.

### Usage
```
./101-starwars_characters.js <movie_id>
```
- `<movie_id>`: The movie ID (e.g., 3 for "Return of the Jedi").

---

Feel free to explore these scripts for your web scraping and data manipulation needs. Each task serves a different purpose and provides useful functionalities for working with web data. You can run these scripts in a Node.js environment.

**Repository:**
- GitHub repository: [alx-higher_level_programming](repository_link)
- Directory: 0x14-javascript-web_scraping
