#!/usr/bin/node
const request = require('request');
const url = 'https://swapi-api.hbtn.io/api/films/';
let people = [];
let WedgeAntilles = [];
request(url, (error, response, body) => {
  if (!error) {
    for (const films of JSON.parse(body).results) {
      people = people.concat(films.characters);
    }
    WedgeAntilles = people.filter(x => x.includes('18'));
    console.log(WedgeAntilles.length);
  } else {
    console.log(error);
  }
});
