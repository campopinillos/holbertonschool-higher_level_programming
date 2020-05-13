#!/usr/bin/node
const request = require('request');
const fs = require('fs');
const url = process.argv[2];

request(url, (error, response, body) => {
  if (response) {
    fs.writeFileSync(process.argv[3], body, 'utf-8');
  } else {
    console.log(error);
  }
});
