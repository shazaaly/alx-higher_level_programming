#!/usr/bin/node
const count = parseInt(process.argv[2]);
if (!count || isNaN(count)) {
  console.log('Missing number of occurrences');
}
if (count < 0) {
  // No code needed here

}
for (let i = 0; i < count; i++) {
  console.log('C is fun');
}
