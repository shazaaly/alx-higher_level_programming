#!/usr/bin/node

exports.logMe = function (item) {
  let counter = 0;
  function tracker () {
    console.log(counter + ':' + item);
    counter++;
  }
  return tracker;
};
