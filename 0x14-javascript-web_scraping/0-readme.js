#!/usr/bin/node
// a script that reads and prints the content of a file.
const fs = require('fs');
const filePath = process.argv[2];
const fileEncoding = 'utf-8';

fs.readFile(filePath, fileEncoding, (err, data) => {
  if (err) {
    console.log(err);
  }
  console.log(data);
});
