#!/usr/bin/node
const myArgs = process.argv.slice(2);

if (parseInt(myArgs[0])) {
  const size = parseInt(myArgs[0]);
  let square = '';
  for (let i = 0; i < size; i++) {
    square += 'X';
  }
  for (let j = 0; j < size; j++) {
    console.log(square);
  }
} else {
  console.log('Missing size');
}
