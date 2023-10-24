#!/usr/bin/node

const request = require('request');
const id = process.argv[2];
const url = `https://swapi-api.alx-tools.com/api/films/${id}`;
request(url, (err, res, body) => {
  const movie = JSON.parse(body);
  console.log(err || movie.title);
});
