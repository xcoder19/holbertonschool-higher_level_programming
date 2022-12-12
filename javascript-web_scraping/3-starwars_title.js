#!/usr/bin/node

const request = require('request');
const url = 'https://swapi-api.hbtn.io/api/films/';
request(url, function (error, response, body) {
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
