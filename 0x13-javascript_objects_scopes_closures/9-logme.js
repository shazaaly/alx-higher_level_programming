#!/usr/bin/node
let counter = 0;

exports.logMe = function (item) {
  function tracker () {
    console.log(counter + ':' + item);
    counter++;
  }
  return tracker();
};
