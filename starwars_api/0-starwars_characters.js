#!/usr/bin/node
const request = require('request');
const filmId = process.argv[2];
const url = `https://swapi-api.hbtn.io/api/films/${filmId}/`;

request(url, (error, response, body) => {
  if (error) {
    console.log(error);
    return;
  }
  const characters = JSON.parse(body).characters;
  printCharacters(characters, 0);
});

function printCharacters (characters, index) {
  if (index >= characters.length) {
    return;
  }
  request(characters[index], (error, response, body) => {
    if (error) {
      console.log(error);
      return;
    }
    console.log(JSON.parse(body).name);
    printCharacters(characters, index + 1);
  });
}
