#!/usr/bin/node
// Script that prints the title of a Star Wars movie where the episode no. matches a given integer.

const request = require('request');
const episode = process.argv[2];
const URL = 'https://swapi-api.hbtn.io/api/films/';

request(URL + episode, function (error, response, body) {
  if (error) {
    console.error(error);
  }
  console.log(JSON.parse(body).title);
});
