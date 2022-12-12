#!/usr/bin/node
const myArgs = process.argv.slice(2);
const fs = require('fs');

try {
  const data = fs.readFileSync(`${myArgs[0]}`, 'utf8');
  console.log(data);
} catch (err) {
  console.log(err);
}
