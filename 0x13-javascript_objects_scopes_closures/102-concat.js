#!/usr/bin/node
const fs = require('fs');

const fileA = process.argv[2];
const fileB = process.argv[3];
const dest = process.argv[4];

const fileAContent = fs.readFileSync(fileA.toString());
const fileBContent = fs.readFileSync(fileB.toString());
fs.writeFileSync(dest, fileAContent, fileBContent);
