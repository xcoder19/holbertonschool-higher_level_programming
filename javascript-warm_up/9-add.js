#!/usr/bin/node
const myArgs = process.argv.slice(2);
function add (a, b) {
  return a + b;
}
if (parseInt(myArgs[0]) && parseInt(myArgs[1])) {
  console.log(add(parseInt(myArgs[0]), parseInt(myArgs[1])));
}
