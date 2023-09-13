#!/usr/bin/node
const fs = require('fs');

const fileA = fs.readFileSync(process.argv[2]).toString();
const fileB = fs.readFileSync(process.argv[3]).toString();
fs.writeFileSync(process.argv[4], fileA + fileB);
