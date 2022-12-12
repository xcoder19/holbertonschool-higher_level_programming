#!/usr/bin/node
const myArgs = process.argv.slice(2);

const request = require('request');

request(myArgs[0], function (error, response, body) {
  if (!error) {
    let count = 0;
    JSON.parse(response.body).results.forEach(element => {
      element.characters.forEach((char) => {
        if (char.includes('18')) {
          count++;
        }
      });
    });
    console.log(count);
  } else {
    console.log(404);
  }
});
