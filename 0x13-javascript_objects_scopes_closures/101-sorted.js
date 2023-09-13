#!/usr/bin/node

const dict = require('./101-data').dict;

const dictCopy = dict;
const newDict = {};

for (userID in dictCopy) {
  occurence = dictCopy[userID];
  if (!newDict[occurence]) {
    newDict[occurence] = [];
  }
  newDict[occurence].push(userID);
}
console.log(newDict);
