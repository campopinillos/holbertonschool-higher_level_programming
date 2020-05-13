#!/usr/bin/node
const request = require('request');
const fs = require('fs');
const url = process.argv[2];
request(url).pipe(fs.WriteStream(process.argv[3], 'utf-8'));
