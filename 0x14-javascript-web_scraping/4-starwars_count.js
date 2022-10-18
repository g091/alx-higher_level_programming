#!/usr/bin/node
// Script that prints the no. of movies where the character “Wedge Antilles” is present.

const request = require('request');

request(process.argv[2], function (err, response, body) {
  if (err) {
    console.log(err);
    return;
  }

  const results = JSON.parse(body).results.filter((elem) => {
    return elem.characters.filter((url) => { return url.includes('18'); }).length;
  }).length;
  console.log(results);
});
