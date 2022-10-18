#!/usr/bin/node
// Scriipt that computes the no. of tasks completed by user id.

const request = require('request');
const API_URL = process.argv[2];
const result = {};

request(API_URL, function (error, response, body) {
  if (error) {
    console.error(error);
  }

  if (response.statusCode === 200) {
    JSON.parse(body).forEach(el => {
      if (el.completed === true) {
        if (result[el.userId] === undefined) {
          result[el.userId] = 0;
        }
        result[el.userId]++;
      }
    });
  }

  console.log(result);
});
