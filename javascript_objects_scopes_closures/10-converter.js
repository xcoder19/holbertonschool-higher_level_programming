#!/usr/bin/node
exports.converter = function (base) {
  function converter (number) {
    return number.toString(base);
  }

  return converter;
};
