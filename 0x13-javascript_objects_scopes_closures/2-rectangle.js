#!/usr/bin/node
class Rectangle {
  constructor (w, h) {
    if (!w || !h || w < 0 || h < 0) {
      // empty object

    } else {
      this.w = w;
      this.h = h;
    }
  }
}
module.exports = Rectangle;
