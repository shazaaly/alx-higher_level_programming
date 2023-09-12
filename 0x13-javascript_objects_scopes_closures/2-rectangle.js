#!/usr/bin/node
class Rectangle {
  constructor (w, h) {
    if (w > 0 && h > 0) {
      this.w = w;
      this.h = h;
    }
  }
}
module.exports = Rectangle;
