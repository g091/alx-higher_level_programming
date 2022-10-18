#!/usr/bin/node
// Script that gets the contents of a webpage and stores it in a file.

const request = require('request');
const fs = require('fs');
const url = process.argv[2];
const path = process.argv[3];

request(url, function (error, response, body) {
  if (error) {
    console.error(error);
  }
  try {
    fs.writeFile(path, body, 'utf8', function (err, result) { if (err) console.log(err); });
  } catch (err) {
    console.log(err);
  }
});
