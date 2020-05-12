#!/usr/bin/node
const firstList = require('./100-data').list;
const secondList = firstList.map((item) => item * firstList.indexOf(item));

console.log(firstList);
console.log(secondList);
