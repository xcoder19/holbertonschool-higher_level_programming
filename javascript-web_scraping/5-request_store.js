#!/usr/bin/node
const request = require('request');
const myArgs = process.argv.slice(2);
const fs = require('fs');
request(myArgs[0], function (error, response, body) {
  if (!error) {
    try {
      fs.writeFileSync(myArgs[1], body);
    } catch (err) {
      console.log(err);
    }
  } else {
    console.log(404);
  }
});
