#!/usr/bin/node
const myList = require('./100-data').list;
const newList = myList.map((index, el) => el * index);
console.log(newList);
