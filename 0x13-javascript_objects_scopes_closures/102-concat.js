#!/usr/bin/node
const fileA = process.argv[2];
const fileB = process.argv[3];
const dest = process.argv[4];

const fs = require('fs');

const fileAContent = fs.readFileSync(fileA.toString());
const fileBContent = fs.readFileSync(fileB.toString());
fs.writeFileSync(dest, fileAContent, fileBContent);
