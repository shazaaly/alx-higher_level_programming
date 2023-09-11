#!/usr/bin/node
const size = parseInt(process.argv[2]);
if (!size || isNaN(size)) {
  console.log('Missing size');
}
if (size < 0) {
  // do nothing
}
for (let i = 0; i < size; i++) {
  for (let j = 0; j < size; j++) {
    process.stdout.write('X');
  }
  process.stdout.write('\n');
}
