#!/usr/bin/node
const request = require('request');
const myArgs = process.argv.slice(2);

request(myArgs[0], function (error, response, body) {
  if (!error) {
    console.log(`code: ${response.statusCode}`);
  } else {
    console.log(404);
  }
});
