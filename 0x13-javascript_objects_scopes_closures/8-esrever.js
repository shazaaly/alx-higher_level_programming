#!/usr/bin/node

exports.esrever = function (list) {
  const reversed = [];
  const len = list.length;
  let i = len - 1;
  while (i > 0) {
    reversed.push(list[i]);

    i--;
  }
  return reversed;
};
