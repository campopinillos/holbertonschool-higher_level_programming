#!/usr/bin/node
const myArgs = process.argv;
if (myArgs.lenght === 2) {
  console.log('No argument');
} else if (myArgs.lenght === 3) {
  console.log('Argument found');
} else {
  console.log('Arguments found');
}
