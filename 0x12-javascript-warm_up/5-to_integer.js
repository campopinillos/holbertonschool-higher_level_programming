#!/usr/bin/node
const myNum = parseInt(process.argv[2]);
console.log(Number.isNaN(myNum) ? 'Not a Number' : 'My number: ' + myNum);
