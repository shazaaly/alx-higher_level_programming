#!/usr/bin/node
const request = require('request');
const url = process.argv[2];

request(url, (err, res, body) => {
  let count = 0;

  const cont = JSON.parse(body);
  const results = cont.results;
  results.forEach(elem => {
    if (elem.characters.includes('https://swapi-api.alx-tools.com/api/people/18/')) {
      count++;
    }
  });
  console.log(err || count);
});
