#!/usr/bin/node

const request = require('request');
const id = process.argv[2];

url = `https://swapi-api.alx-tools.com/api/films/${id}`;
request(url, (err, res, body) => {
  movies = JSON.parse(body);
  const chars = movies.characters;
  for (let index = 0; index < chars.length; index++) {
    const element = chars[index];
    request(element, (err, res, body) => {
      if (err) {
        console.log(err);
      }
      const data = JSON.parse(body);
      console.log(data.name);
    });
  }
});
