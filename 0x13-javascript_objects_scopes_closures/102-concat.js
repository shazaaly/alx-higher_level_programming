#!/usr/bin/node
const fileA = process.argv[2];
const fileB = process.argv[3];
const dest = process.argv[4];

const fs = require('fs');

const fileAContent = fs.readFileSync(fileA, 'utf-8');
const fileBContent = fs.readFileSync(fileB, 'utf-8');
const concatenated = fileAContent + '\n' + fileBContent;

fs.writeFileSync(concatenated, dest);
