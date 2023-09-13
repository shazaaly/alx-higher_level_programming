#!/usr/bin/node

const { list } = require('./100-data');

const myList = require('./100-data').list;
const newList = myList.map((index, el) => el * index);
console.log(list);
console.log(newList);
