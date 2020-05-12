#!/usr/bin/node
const firstList = require('./100-data').list;
console.log(firstList);
console.log(firstList.map((item) => item * firstList.indexOf(item)));
