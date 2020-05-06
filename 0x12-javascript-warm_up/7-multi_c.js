#!/usr/bin/node
const times = process.argv[2];
if (times > 0) {
  for (let i = 0; i < times; i++) {
    console.log('C is fun');
  }
} else {
  console.log('Missing number of occurrences');
}
