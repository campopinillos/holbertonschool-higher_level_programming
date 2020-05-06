#!/usr/bin/node
const myNum = parseInt(process.argv[2]);
console.log(isNaN(myNum) ? 'Not a Number' : myNum);
