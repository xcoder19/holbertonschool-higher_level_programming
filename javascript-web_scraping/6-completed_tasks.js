#!/usr/bin/node
const request = require('request');
const myArgs = process.argv.slice(2);
request(myArgs[0], function (error, response, body) {
  if (!error) {
    const obj = {};
    for (let id = 1; id <= 10; id++) {
      let count = 0;
      JSON.parse(body).forEach(element => {
        if (element.userId === id && element.completed) {
          count++;
        }
      });
      obj[id] = count;
    }
    console.log(obj);
  } else {
    console.log(404);
  }
});
