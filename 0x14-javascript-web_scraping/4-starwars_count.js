#!/usr/bin/node
const request = require('request');
const url = 'https://swapi-api.hbtn.io/api/films/';
let WedgeAntilles = [];
request(url, (error, response, body) => {
  if (!error) {
    for (const films of JSON.parse(body).results) {
      WedgeAntilles = WedgeAntilles.concat(films.characters);
    }
    WedgeAntilles = WedgeAntilles.filter(x => x.includes('18'));
    console.log(WedgeAntilles.length);
  } else {
    console.log(error);
  }
});
