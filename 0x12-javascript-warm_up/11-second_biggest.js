#!/usr/bin/node
const arrayIni = process.argv;
arrayIni.splice(0, 2);
const arrayNum = arrayIni.map(Number);
const index = arrayNum.indexOf(Math.max(...arrayNum));
arrayNum.splice(index);
console.log(Math.max(...arrayNum));
