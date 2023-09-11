#!/usr/bin/node
const a = parseInt(process.argv[2]);
const b = parseInt(process.argv[3]);

function add (a, b) {
  if (typeof a === 'undefined' || typeof b === 'undefined') {
    console.log('NaN');
    return;
  }
  console.log(a + b);
}
add(a, b);
