#!/usr/bin/node
const request = require('request');
const url = process.argv[2];
request(url, (req, res) => {
  console.log('code: ' + res.statusCode);
});
