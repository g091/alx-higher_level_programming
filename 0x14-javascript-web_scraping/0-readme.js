#!/usr/bin/node
// Script that reads and prints the content of a file.

const fs = require('fs');
const file = process.argv[2];

fs.readFile(file, 'utf-8', function (err, result) {
  if (err) {
    console.log(err);
  } else {
    console.log(result);
  }
});
