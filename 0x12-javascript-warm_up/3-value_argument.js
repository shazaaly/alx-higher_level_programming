#!/usr/bin/node
let count = 0;
while (typeof process.argv[count + 2] !== 'undefined') {
  count++;
}
if (count === 0) {
  console.log('No argument');
} else {
  console.log(process.argv[2]);
}
