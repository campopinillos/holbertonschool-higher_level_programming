#!/usr/bin/node
const request = require('request');
const fs = require('fs');
request(process.argv[2]).pipe(fs.writeFile(process.argv[3], 'utf-8', err => {
  if (err) console.log(err);
}));
