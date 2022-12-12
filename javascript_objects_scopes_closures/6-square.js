#!/usr/bin/node
const SquareX = require('./5-Square.js');
class Square extends SquareX {
  charPrint (c) {
    if (c !== undefined) {
      let square = '';
      for (let i = 0; i < this.width; i++) {
        square += c;
      }
      for (let j = 0; j < this.height; j++) {
        console.log(square);
      }
    } else {
      super.print();
    }
  }
}

module.exports = Square;
