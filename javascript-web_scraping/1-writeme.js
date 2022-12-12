#!/usr/bin/node
const myArgs = process.argv.slice(2);
const fs = require('fs');

try {
  fs.writeFileSync(myArgs[0], myArgs[1]);
} catch (err) {
  console.log(err);
}
