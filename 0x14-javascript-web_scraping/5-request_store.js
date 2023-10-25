#!/usr/bin/node

const url = process.argv[2];
const path = process.argv[3];
// const format = 'utf8'

const request = require('request');
const fs = require('fs');
const writeStream = fs.createWriteStream(path);

request(url, (err, res, body) => {
  if (err) {
    console.log(err);
  }
  writeStream.write(body);
  writeStream.end();
});
