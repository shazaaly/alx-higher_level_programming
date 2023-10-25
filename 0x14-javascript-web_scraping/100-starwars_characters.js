#!/usr/bin/node

const request = require('request');
url = 'https://swapi-api.alx-tools.com/api/films';
const id = process.argv[2];
let fname = '';
request(url, (err, res, body) => {
  movies = JSON.parse(body);
  movies.results.map(movie => {
    movie.characters.map(ch => {
      if (ch === `https://swapi-api.alx-tools.com/api/people/${id}/`) {
        request(ch, (err, res, body) => {
          fname = JSON.parse(body).name;
          console.log(fname);
        });
      }
    });
  });
});
