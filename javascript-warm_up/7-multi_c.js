#!/usr/bin/node
const myArgs = process.argv.slice(2);

let i = 0;
if (parseInt(myArgs[0])) {
  while (i < parseInt(myArgs[0])) {
    console.log('C is fun');
    i++;
  }
} else {
  console.log('Missing number of occurrences');
}
