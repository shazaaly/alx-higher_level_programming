#!/usr/bin/node
const fs = require('fs');
const path = process.argv[2];
const string = process.argv[3];
fs.writeFile(path, string, function (err) {
  if (err) {
    console.log(err);
  }
});
