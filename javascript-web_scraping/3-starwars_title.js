#!/usr/bin/node
const request = require('request');
const myArgs = process.argv.slice(2);
const url = `https://swapi-api.hbtn.io/api/films/${myArgs[0]}`;
request(url, function(error, response, body) {
  if (!error) {
    console.log(JSON.parse(response.body).title);
  } else {
    console.log(404);
  }
});
