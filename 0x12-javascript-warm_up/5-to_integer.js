#!/usr/bin/node

const converted = parseInt(process.argv[2]);
if (!isNaN(converted)) {
  console.log('My number: ' + converted);
} else {
  console.log('Not a number');
}
