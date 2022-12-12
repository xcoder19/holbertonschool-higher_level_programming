#!/usr/bin/node
const request = require('request');
const myArgs = process.argv.slice(2);
request(myArgs[0], function (error, response, body) {
  if (!error) {
    const obj = {};
    const arr = [];
    JSON.parse(body).forEach(task => {
      if (!arr.includes(task.userId)) {
        arr.push(task.userId);
      }
    });
    for (let id = 1; id <= arr.length; id++) {
      let count = 0;
      JSON.parse(body).forEach(element => {
        if (element.userId === id && element.completed) {
          count++;
        }
      });
      if (count > 0) { obj[id] = count; }
    }

    console.log(obj);
  } else {
    console.log(404);
  }
});
